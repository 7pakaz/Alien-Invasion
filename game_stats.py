import json

class GameStats():
    '''track statistics for alien invasion'''

    def __init__(self, ai_setting):
        """Initialize statistics."""
        self.ai_setting = ai_setting
        self.reset_stats()
        #Start Alien Invasion in an active state.
        self.game_active = False

        #level and score
        self.read_best_score()


    def read_best_score(self):
        #read best score from json
        file_name = r'store_information\store_best_score.json'
        with open(file_name) as f_objt:
           best_score_saved = json.load(f_objt)
        self.best_score = best_score_saved


    def reset_stats(self):
        '''Initialize statistics that can change during the game'''
        self.ships_left = self.ai_setting.ship_limit
        self.level = 1
        self.score = 0
