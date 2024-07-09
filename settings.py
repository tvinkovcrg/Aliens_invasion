class Settings:
    """Клас для збереження всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізувати налаштування гри"""
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
        self.alien_speed = 0.25
        self.fleet_drop_speed = 15
        # fleet_direction 1 meaning moving right; -1 -- left
        self.fleet_direction = 1
