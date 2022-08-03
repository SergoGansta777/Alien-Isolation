import sys

import pygame

from bullet import Bullet

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



def update_screen(ai_settings, screen, ship, bullets):
    """Updates the image and displays a new screen"""

    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg, (0, 0))

    # Все пули выводяться позади изображений корабля
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Отображение последнего прорисованного экрана
    pygame.display.flip()