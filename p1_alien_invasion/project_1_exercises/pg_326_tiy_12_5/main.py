import sys
import pygame
from pygame.locals import *


class KeyDown:
    """Print keys pressed game"""

    def __init__(self):
        """Initialize game"""
        pygame.init()
        pygame.font.init()

        # Screen settings
        self.screen = pygame.display.set_mode((600, 400))
        self.screen_width = 600
        self.screen_height = 400

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(
                    f"\nYou have pressed the following button: '{pygame.key.name(event.key)}'")
                elif event.type == pygame.KEYUP:
                    print("Go ahead and press another button")






if __name__ == '__main__':
    # Make a game instance, and run the game.
    show_key = KeyDown()
    show_key.run_game()