import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for manage bullets fired by a ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a new bullet in position of the ship."""
        super().__init__()
        self.screen = screen

        # Создание пули в позиции (0, 0) и и назначение правлильной позиции.
        self.image_bullet = pygame.image.load("images/Lazery.png")
        self.image_bullet = pygame.transform.scale(self.image_bullet, (ai_settings.bullet_width, ai_settings.bullet_height))
        self.rect = self.image_bullet.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Позиция пули храниться в вещественном формате
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet upper """
        self.y -= self.speed_factor

        # Обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """Print bullet on the screen"""
        self.screen.blit(self.image_bullet, self.rect)
