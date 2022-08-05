import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_fleet_edges(ai_settings, aliens):
    """Reacts when the alien reaches the edge of the screen"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Lowers the entire fleet and changes direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine amount of rows"""
    available_space_y = (ai_settings.screen_height -
                         (2 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of the aliens' ships"""
    available_space_x = ai_settings.screen_width - 3 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creates a new alien and places in on the screen"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.5 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship,  aliens):
    """Creates a fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Создание первого ряда пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Создание пришельца и размещения в ряду
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def bullet_update(bullets):
    """Updates the positionf of the bullet and eliminate the old bullets"""
    bullets.update()

    # Удаление пуль, вышедшие за границы экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Shot bullet if max don't achivied"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responds to key process"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_q:
        sys.exit()

    if event.key == pygame.K_SPACE:
        # Создание новой пули и включение ее в группу
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Respond to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    """Processing click keys and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_aliens(ai_settings, aliens):
    """Checks if the fleet has reached the edge of the screen
     and then updates the positions of al aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Updates the image and displays a new screen"""

    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg, (0, 0))

    # Все пули выводяться позади изображений корабля
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Отображение последнего прорисованного экрана
    pygame.display.flip()