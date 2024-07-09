import pygame


class Ship:
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізувати корабель та задати його початкову позицію"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Завантажувати зображення корабля
        self.image = pygame.image.load('images/player_ship.bmp')
        self.rect = self.image.get_rect()

        # Започатковувати кожен новий корабель внизу по центру екрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Зберегти десяткове значення при позиції корабля по горизонталі
        self.x = float(self.rect.x)

        # Індикатори руху
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Оновити поточну позицію корабля на основі індикатора руху"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # Оновити об'єкт rect з self.x
        self.rect.x = self.x

    def blitme(self):
        """ """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Відцентрувати корабель на екрані"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
