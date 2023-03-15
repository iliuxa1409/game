class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0
        self.recall_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def remember_high_score(self):
        filename = 'high_score.txt'
        with open(filename, 'w') as file_object:
            file_object.write(str(self.high_score))

    def recall_high_score(self):
        filename = 'high_score.txt'
        with open(filename, 'r') as file_object:
            hs = file_object.read()
            self.high_score = int(hs)

