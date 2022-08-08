import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button

import game_funcions as gf




def run_game():
    """Initializes the game environment"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)

    # Создание кнопки Play
    play_button = Button(ai_settings, screen, "Play")

    # Создание корабля
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль и группы пришельцев
    bullets = Group()
    aliens = Group()

    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()
