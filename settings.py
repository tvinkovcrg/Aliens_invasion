class Settings:
    """Клас для збереження всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізувати постійні налаштування гри"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (90, 160, 230)

        # Ship settings
        self.ship_speed = 1
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.75
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.3
        self.fleet_drop_speed = 15
        # fleet_direction 1 meaning moving right; -1 -- left
        self.fleet_direction = 1

        # How faster will game be
        self.speedup_scale = 1.1

        # How fast will aliens cost grow
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Ініціалізація змінних налаштувань"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.3

        # fleet_direction 1 представляє напрямок праворуч; -1 -- ліворуч
        self.fleet_direction = 1

        # Getting points
        self.alien_points = 50

    def increase_speed(self):
        """Збільшення налаштувань швидкості та вартості прибульців."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
