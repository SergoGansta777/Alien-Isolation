import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Initializes the ship and clamps the starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения и получения прямоугольника
        self.image = pygame.image.load('images/Korabl.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (ai_settings.ship_size[0], ai_settings.ship_size[1]))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Сохранение вещественной координаты центра корабля
        self.center = float(self.rect.centerx)
        self.center_y = float(self.screen_rect.bottom)

        # Флаги перемещения корабля
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Updates position ship taking into account position"""

        # Обновляется атрибут center, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.center_y > self.ai_settings.ship_size[1]:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.center_y <= self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor


        # Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center
        self.rect.bottom = self.center_y

    def blitme(self):
        """Draw the ship in current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Move a ship to the center of the screen"""
        self.center = self.screen_rect.centerx
        self.center_y = self.screen_rect.bottom