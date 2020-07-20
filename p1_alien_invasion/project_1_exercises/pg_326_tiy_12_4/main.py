import sys
import pygame
from p1_alien_invasion.project_1_exercises.pg_326_tiy_12_4.rocket import Rocket
from p1_alien_invasion.project_1_exercises.pg_326_tiy_12_4.settingss import Settings

class Rocketship:
    """Class for rocket ship game"""

    def __init__(self):
        """General initialization of game"""

        pygame.init()

        self.settings = Settings()

        # Screen settings
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rocket 12-4")
        self.bg_color = self.settings.bg_color

        # rocket settings
        self.rocket = Rocket(self)

    def run_game(self):
        """Loop for the game"""

        while True:
            # Check for key presses
            self.check_events()
            # update image location on screen
            self.rocket.update()
            self.update_screen()

            # Make game visible
            pygame.display.flip()

    def check_events(self):
        """Respond to keypresses in game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    r = Rocketship()
    r.run_game()


