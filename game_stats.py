class GameStats:
    """Відстежування статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізація статистики"""
        self.setting = ai_game.settings
        self.reset_stats()

        # Розпочати гру в неактивному стані
        self.game_active = False

    def reset_stats(self):
        """Ініціалізація статистики що може змінюватися впродовж гри"""
        self.ship_left = self.setting.ship_limit
