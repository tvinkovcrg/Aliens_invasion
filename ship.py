import pygame

class Ship:
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізувати корабель та задати його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #
        self.image = pygame.image.load('images/player_ship.bmp')
        self.rect = self.image.get_rect()

        #
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ """
        self.screen.blit(self.image, self.rect)