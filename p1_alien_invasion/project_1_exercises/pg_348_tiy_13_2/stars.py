import sys
import pygame
from random import randint
from pygame.sprite import Sprite

from p1_alien_invasion.project_1_exercises.pg_348_tiy_13_1.settings2 import Settings
from p1_alien_invasion.project_1_exercises.pg_348_tiy_13_1.star import Star

class StarryNight:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("A sky full of stars")

        self.stars = pygame.sprite.Group()

        self._create_starry_sky()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            # self.stars.update_colliding_stars()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_starry_sky(self):
        """Create the fleet of stars."""
        # Create a star and find the number of stars in a row.
        # Spacing between each star is equal to one star width.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (1 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fit on the screen.
        available_space_y = (self.settings.screen_height - 1 * star_height)
        number_rows = available_space_y // (1 * star_height)

        # Create the full sky of stars.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create a star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 10 * star_width * star_number
        star.rect.x = randint(0, star.x)
        star.y = star.rect.height + 10 * star.rect.height * row_number
        star.rect.y = randint(0, star.y)
        self.stars.add(star)
        # collisions = pygame.sprite.groupcollide(
        #     star.rect.x, star.rect.y, True, True)
        # if collisions:
        #     for stars in collisions.values():
        #         self.stars.remove(stars)



    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    sn = StarryNight()
    sn.run_game()
