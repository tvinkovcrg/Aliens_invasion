import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Загальний клас, що керує ресурсам та поведінкою гри"""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """Розпочати головний цикл гри"""
        while True:
            # Слідкувати за подіями миші та клавіатури
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Реагувати на натискання клавіш та події миші"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагування на натискання клавіш"""
        # Переміщуємо корабель вправо при натисканні стрілочки
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # Переміщуємо корабель вліво при натисканні стрілочки
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагування на відпускання клавіш"""
        # Припиняємо переміщення корабля при відпусканні клавіші
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Оновити зображення на екрані та перемкнутися на новий екран"""
        # Наново перемалювати екран на кожній ітерації циклу
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Показувати останній намальований екран
        pygame.display.flip()


if __name__ == '__main__':
    # Створити екземпляр гри та запустити гру
    ai = AlienInvasion()
    ai.run_game()
