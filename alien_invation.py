import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scorebard import Scorebard

def run_game():
    #Initialize game setting and screen object
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    #make the play buttom
    play_button = Button(ai_setting, screen, 'PLAY GAME')

    #make a ship
    ship = Ship(ai_setting,screen)
    #Make a group to store bullets in
    bullets = Group()
    #Make a alien
    aliens = Group()

    #create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_setting) 
    sb = Scorebard(ai_setting, screen, stats) 



    #creete the fleat of aliens
    gf.create_fleet(ai_setting, screen, ship, aliens)

    #Start the main loop for the game.
    while True:
        gf.check_events(ai_setting, screen, stats, play_button,ship, bullets, aliens,sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, stats, screen, ship, aliens, bullets,sb)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets, sb)    
        gf.update_screen(ai_setting,screen, stats, ship, aliens, bullets, play_button, sb)
             


run_game()