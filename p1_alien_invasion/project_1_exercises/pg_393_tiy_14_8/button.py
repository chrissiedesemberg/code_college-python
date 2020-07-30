import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # The button message needs to be prepped only once.
        if msg == "Easy":
            self.rect.midleft = self.screen_rect.midleft
            self.button_color = (0, 255, 0)
            self.settings.settings_easy()
        elif msg == "Medium":
            self.rect.center = self.screen_rect.center
            self.button_color = (255, 255, 0)
            self.settings.settings_medium()
        else:
            self.rect.midright = self.screen_rect.midright
            self.button_color = (255, 0, 0)
            self.settings.settings_hard()
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


