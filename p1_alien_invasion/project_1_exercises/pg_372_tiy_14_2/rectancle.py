import pygame
from pygame.sprite import Sprite


class Target(Sprite):
    """A class to represent a single target in the target."""

    def __init__(self, stb):
        """Initialize the target and set its starting position."""
        super().__init__()
        self.screen = stb.screen
        self.settings = stb.settings
        self.screen_rect = self.screen.get_rect()

        #Create Rect
        size = width, height = 40, 40
        color = (0, 0, 255)
        self.image = pygame.Surface(size)
        self.image.fill(color)

        # Build the button's rect object and center it
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright

    def check_edges(self):
        """Return True if target is at edge of screen."""
        if self.rect.top <= self.screen_rect.top or self.rect.bottom >= \
                self.screen_rect.bottom:
            return True

    def update(self):
        """Move the target up or down."""
        self.rect.y += (self.settings.target_speed * self.settings.target_direction)
