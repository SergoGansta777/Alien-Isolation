import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class relases a one alien"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and sets the position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения пришельца и назначения атрибута rect
        self.image = pygame.image.load("images/alien_ship1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 110))
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = 0

        # Сохранение позиции c вещественной точностью
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien id near screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False


    def update(self):
        """Moves alien to the right position or left position"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw a alien in current position"""
        self.screen.blit(self.image, self.rect)