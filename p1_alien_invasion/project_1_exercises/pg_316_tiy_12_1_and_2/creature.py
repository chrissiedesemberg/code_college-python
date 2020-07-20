import pygame

class Creature:
    """A little monster"""

    def __init__(self, dm_game):
        """Create a monster and put it in the middle of the page"""
        self.screen = dm_game.screen
        self.screen_rect = dm_game.screen.get_rect()

        # Load the creature image and get its rect
        self.image = pygame.image.load('images/creature.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the creature in the middle of the screen"""
        self.screen.blit(self.image, self.rect)
