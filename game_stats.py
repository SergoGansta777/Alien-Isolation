
class GameStats():
    """Tracking stats for the game"""

    def __init__(self, ai_settings):
        """Initialize the game statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """Initialize the statistics which chanfes in the game"""
        self.ships_left = self.ai_settings.ship_limit