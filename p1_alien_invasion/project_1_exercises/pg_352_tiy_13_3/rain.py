import sys
import pygame
from p1_alien_invasion.project_1_exercises.pg_352_tiy_13_3.settings import Settings
from p1_alien_invasion.project_1_exercises.pg_352_tiy_13_3.drop import Drop

class Raindrops:
    """ Overall class to manage game assets and behaviour. """

    def __init__(self):
        """Initialize the game and create game resources."""

        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Raindrops keep falling")
        self.drops = pygame.sprite.Group()

        self._create_drops()

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self.drops.update()
            self._update_screen()
            self._check_events()

    def _create_drops(self):
        """Create a fleet of aliens"""
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size
        available_space_y = self.settings.screen_height - (2 * drop_height)
        number_drops_y = available_space_y // (2 * drop_height)

        # Determine the number of rows of drops that fit on the screen.
        available_space_x = (self.settings.screen_width - 1 * drop_width)
        number_rows = available_space_x // (2 * drop_width)

        # Create a full fleet of drops.
        for row_number in range(number_rows):
            for drop_number in range(number_drops_y):
                self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        """Create a drop and place it in the row"""
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size
        drop.y = drop_height + 2 * drop_height * drop_number
        drop.rect.y = drop.y
        drop.rect.x = drop.rect.width + 2 * drop.rect.width * row_number
        self.drops.add(drop)

    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_q or pygame.K_ESCAPE:
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)

        pygame.display.flip()

    def drops(self):
        """Update the positions of all aliens in the fleet."""
        """
        Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.drops.update()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for drop in self.drops.sprites():
            if drop.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for drop in self.drops.sprites():
            drop.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= 1



if __name__ == '__main__':
    # Make a game instance, and run the game.
    rd = Raindrops()
    rd.run_game()
