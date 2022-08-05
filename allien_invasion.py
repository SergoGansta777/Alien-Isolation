import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_funcions as gf



def run_game():
    """Initializes the game environment"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    # Создание корабля
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль и группы пришельцев
    bullets = Group()
    aliens = Group()

    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.bullet_update(bullets)


        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
