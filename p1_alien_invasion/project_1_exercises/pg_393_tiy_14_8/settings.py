class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_limit = 4

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # # Bullet settings
        self.bullet_width = 20
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        # Alien settings
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = -1

        # Start game in an inactive state.
        self.game_active = False

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

    def settings_easy(self):
        self.ship_speed = 1
        self.bullet_speed = 2
        self.alien_speed = 1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 25
        self.bullets_wasted_points = 5

    def settings_medium(self):
        self.ship_speed = 2
        self.bullet_speed = 4
        self.alien_speed = 3

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50
        self.bullets_wasted_points = 10

    def settings_hard(self):
        self.ship_speed = 3
        self.bullet_speed = 4.0
        self.alien_speed = 3

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 100
        self.bullets_wasted_points = 20