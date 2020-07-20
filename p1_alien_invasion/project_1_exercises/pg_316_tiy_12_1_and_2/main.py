
import sys
import pygame
from p1_alien_invasion.project_1_exercises.pg_316_tiy_12_1_and_2.settings import Settings
from p1_alien_invasion.project_1_exercises.pg_316_tiy_12_1_and_2.creature import Creature


class DancingMonsterGame:
    """Overall class to manage game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Little Character")
        self.creature = Creature(self)
        # Set the background color.
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self._update_screen()
            # Make the most recently drawn screen visible
            pygame.display.flip()

    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.creature.blitme()  # Ship


if __name__ == '__main__':
    # Make a game instance, and run the game.
    dmg = DancingMonsterGame()
    dmg.run_game()