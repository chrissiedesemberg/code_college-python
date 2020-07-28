class Settings:
    """A class to store all settings for target Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (255, 255, 255)

        # How quickly the game speeds up
        self.speedup_scale = 0.4

        # Ship settings
        self.ship_speed = 1.5

        # # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.bullets_limit = 3

        # target settings
        self.target_speed = 3.0
        self.target_drop_speed = 30
        # target_direction of 1 represents up; -1 represents down.
        self.target_direction = -1

    def initialize_original_settings(self):

        self.bullets_allowed = 3
        self.bullets_limit = 3

        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.target_speed = 3.0
        self.target_direction = -1

    def increase_speed(self):

        self.bullets_allowed = 3
        self.bullets_limit = 3

        self.ship_speed += self.speedup_scale
        self.bullet_speed += self.speedup_scale
        self.target_speed += self.speedup_scale
