import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scorebard():

    def __init__(self, ai_setting, screen, stats):
        '''Initialize button attributes'''
        self.screen = screen
        self.stats = stats
        self.ai_setting = ai_setting
        self.screen_rect = screen.get_rect()

        #set the dimension and properties of button
        self.width, self.height = 150,50
        self.level_color = (230, 230, 230)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 30)

        # Build the button's rect object and top it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        # The button message needs to be prepped only once.
        
        self.level_number()
        self.score_number()
        self.best_score_number()
        self.ship_number()


    def level_number(self):
        """Turn the level into a rendered image."""
        level= f'LEVEL: {self.stats.level}'
        self.level_image = self.font.render(level, True, self.text_color, self.level_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.centery = self.rect.centery
        self.level_image_rect.left = self.rect.left

    def score_number(self):
        """Turn the  score into a rendered image."""
        score = f'SCORE: {self.stats.score}'
        self.score_image = self.font.render(score, True, self.text_color, self.level_color)

        # Position the level below the score.
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.level_image_rect.right
        self.score_image_rect.top = self.level_image_rect.bottom + 10


    def best_score_number(self):
        """Turn the  best_score into a rendered image."""
        best_score = f'{self.stats.best_score}'
        self.best_score_image = self.font.render(best_score, True, self.text_color, self.level_color)

        # Position the level below the score.
        self.best_score_image_rect = self.best_score_image.get_rect()
        self.best_score_image_rect.top = self.screen_rect.top +15
        self.best_score_image_rect.centerx = self.screen_rect.centerx        


    def ship_number(self):
        """show how many ships are left"""
        self.ships = Group()
        for ship_amount in range(self.stats.ships_left):
            ship = Ship(self.ai_setting, self.screen)
            ship.rect.x = 10 + ship_amount * ship.rect.width
            ship.rect.y = 5 
            self.ships.add(ship)




    def show_level(self):
        #draw blank button and then draw message
        self.screen.blit(self.level_image, self.level_image_rect)
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.best_score_image, self.best_score_image_rect)
        
        #draw ships
        self.ships.draw(self.screen)
