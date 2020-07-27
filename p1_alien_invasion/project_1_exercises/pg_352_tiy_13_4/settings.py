class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Drop settings
        self.drop_speed = 2
        self.fleet_drop_speed = 1
        # fleet_direction of 1 represents down
        self.fleet_direction = 1
