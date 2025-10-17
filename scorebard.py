import pygame.font

class Scorebard():

    def __init__(self, ai_setting, screen, stats):
        '''Initialize button attributes'''
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()

        #set the dimension and properties of button
        self.width, self.height = 200,50
        self.level_color = (230, 230, 230)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 28)

        # Build the button's rect object and top it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        # The button message needs to be prepped only once.
        
        self.level_number()


    def level_number(self):
        score_str = f'Level: {str(self.stats.score)}'
        """Turn msg into a rendered image and center text on the button."""
        self.level_image = self.font.render(score_str, True, self.text_color, self.level_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.center = self.rect.center

    
    def show_level(self):
        #draw blank button and then draw message
        self.screen.blit(self.level_image, self.level_image_rect)