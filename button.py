import pygame.font


class Button:
    """Кнопка"""
    def __init__(self, ai_game, msg):
        """Ініціалізація атрибутів кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create button's object 'rect' and center him
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message on button need to show only one time
        self._preg_msg(msg)

    def _preg_msg(self, msg):
        """Перетворити текст на зображення та розмістити по центру кнопки"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Намалювати порозжню кнопку, а після повідомлення"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
