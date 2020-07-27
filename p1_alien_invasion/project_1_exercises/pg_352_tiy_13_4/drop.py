import pygame
from pygame.sprite import Sprite


class Drop(Sprite):
    """Class to create and place aliens in game"""

    def __init__(self, rd):
        """Initialize the rain and set its starting position"""
        super().__init__()
        self.screen = rd.screen
        self.settings = rd.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/drop.bmp')
        self.rect = self.image.get_rect()

        # Start each new line near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def blitme(self):
        self.screen.blit(self.image, self.rect)