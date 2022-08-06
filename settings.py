import pygame
3
class Settings():
    """The class for storage all settings in the game."""
    def __init__(self):
        """Initialize the settings of the game."""
        self.screen_width = 1920
        self.screen_height = 1280
        self.bg_color = (74, 101, 138)


        self.bg = pygame.image.load('images/fon.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))

        # Настройки пришельцев
        self.alien_speed_factor = 0.75
        self.fleet_drop_speed = 50
        # 1 - вправо, -1 - влево
        self.fleet_direction = 1

        # Настройки корабля
        self.ship_speed_factor = 2.5
        self.ship_size = (120, 144)


        # Параметры снарядов
        self.bullet_speed_factor = 4
        self.bullet_width = 45
        self.bullet_height = 55
        self.bullet_color = 68, 69, 210
        self.bullet_allowed = 4