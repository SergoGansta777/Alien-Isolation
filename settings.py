import pygame

class Settings():
    """The class for storage all settings in the game."""
    def __init__(self):
        """Initialize the settings of the game."""
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (74, 101, 138)


        self.bg = pygame.image.load('images/fon.jpg')
        # self.tmp_bg = pygame.transform.scale(self.tmp_bg, (self.screen_width, self.screen_height))

        # Настройки корабля
        self.ship_speed_factor = 2.5
        self.ship_size = (120, 144)


        # Параметры снарядов
        self.bullet_speed_factor = 3
        self.bullet_width = 45
        self.bullet_height = 55
        self.bullet_color = 68, 69, 210