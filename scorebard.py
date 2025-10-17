import pygame.font

class Scorebard():

    def __init__(self, ai_setting, screen, stats):
        '''Initialize button attributes'''
        self.screen = screen
        self.stats = stats
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


    def level_number(self):
        """Turn the level and score into a rendered image."""
        level= f'LEVEL: {self.stats.level}'
        self.level_image = self.font.render(level, True, self.text_color, self.level_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.centery = self.rect.centery
        self.level_image_rect.left = self.rect.left

    def score_number(self):
        score = f'SCORE: {self.stats.score}'
        self.score_image = self.font.render(score, True, self.text_color, self.level_color)

        # Position the level below the score.
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.level_image_rect.right
        self.score_image_rect.top = self.level_image_rect.bottom + 10

    
    def show_level(self):
        #draw blank button and then draw message
        self.screen.blit(self.level_image, self.level_image_rect)
        self.screen.blit(self.score_image, self.score_image_rect)