
class GameStats:
    """Track stats for game"""

    def __init__(self, stb):
        """Initialize stats"""

        self.settings = stb.settings
        self.reset_stats()

        # Start game inactive
        self.game_active = False

    def reset_stats(self):
        """ Initizalize changable stats that can change during the game"""
        self.bullets_left = self.settings.bullets_limit
