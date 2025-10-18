class GameStats():
    '''track statistics for alien invasion'''

    def __init__(self, ai_setting):
        """Initialize statistics."""
        self.ai_setting = ai_setting
        self.reset_stats()
        #Start Alien Invasion in an active state.
        self.game_active = False

        #level and score
        self.best_score = 0


        

    def reset_stats(self):
        '''Initialize statistics that can change during the game'''
        self.ships_left = self.ai_setting.ship_limit
        self.level = 1
        self.score = 0
