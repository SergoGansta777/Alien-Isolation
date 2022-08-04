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
        self.image = pygame.image.load("images/pngwing.com.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (102, 102))
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение позиции c вещественной точностью
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw a alien in current position"""
        self.screen.blit(self.image, self.rect)