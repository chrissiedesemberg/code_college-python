import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ss):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ss.screen
        self.settings = ss.settings
        self.screen_rect = self.screen.get_rect()

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        if self.rect.top <= self.screen_rect.top or self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self):
        """Move the alien up or down."""
        self.y += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.y = self.y
