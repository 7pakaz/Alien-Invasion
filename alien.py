import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_setting, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        #Load the alien image and get its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect()

        #Start each new alien at the bottom center of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        #store a decimal value for the alien's bottom
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        '''Move the alien right'''
        self.x += self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction
        self.rect.x = self.x
  

    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image,self.rect)