class Settings():
    """A class to store al settings for Catch."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Keeper Settings
        self.keeper_speed_factor = 1.5

        # Ball Settings
        self.ball_drop_speed = 10
