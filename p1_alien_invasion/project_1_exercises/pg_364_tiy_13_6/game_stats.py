import pygame

class GameStats:
    """Track stats for game"""

    def __init__(self, ss):
        """Initialize stats"""

        self.settings = ss.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        """ Initizalize changable stats that can change during the game"""

        self.ships_left = self.settings.ship_limit
