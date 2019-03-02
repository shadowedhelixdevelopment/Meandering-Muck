class Settings:
    """A class to store all settings for Meandering Muck"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (54, 38, 32)
        # Slime Settings.
        self.slime_speed_factor = 1.5
        # Maze Settings
        self.maze_width = 25
        self.maze_height = 25
        self.maze_block_width = self.screen_width / self.maze_width
        self.maze_block_height = self.screen_height / self.maze_height
