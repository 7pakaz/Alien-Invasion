import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_kewydown_events(event,ai_setting, screen,ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_setting, screen, stats, play_button,ship, bullets, aliens):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
        #Move to the right
        elif event.type == pygame.KEYDOWN:
            check_kewydown_events(event,ai_setting,screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        #Start the game
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, screen, stats, play_button,ship, bullets, aliens, mouse_x, mouse_y)


def check_play_button(ai_setting, screen, stats, play_button,ship, bullets, aliens, mouse_x, mouse_y):
    '''Start a new game when the player click play'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #hide cursor
        pygame.mouse.set_visible(False)
        
        #reset game statistics
        stats.reset_stats()
        stats.game_active = True

        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create a new fleet and center de ship
        create_fleet(ai_setting,screen,ship,aliens)
        ship.center_ship()


def update_screen(ai_setting,screen, stats, ship, aliens, bullets, play_button,sb):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the lloop
    screen.fill(ai_setting.bg_color)
    #redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_level()
    #Draw play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
    #make the most recently drawn screen visible
    pygame.display.flip()


def fire_bullet(ai_setting, screen, ship, bullets):
    #create a new bullet and add it to the bullets group
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullet)


def update_bullets(ai_setting, stats, screen, ship, aliens, bullets,sb):
    bullets.update()
    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting, stats, screen, ship, aliens, bullets,sb)
    

def check_bullet_alien_collisions(ai_setting, stats, screen, ship, aliens, bullets, sb):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        #Destroy existin bullets and create new fleet.
        bullets.empty()
        ai_setting.next_level()
        check_level(stats)
        sb.level_number()
        print(stats.score)
        sleep(0.5)
        create_fleet(ai_setting, screen, ship, aliens)


def get_number_aliens_x(ai_setting, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_setting.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x


def get_number_rows(ai_setting, ship_height, alien_height):
    avalaible_space_y = ai_setting.screen_height - (4*alien_height) - ship_height
    number_aliens_y = int(avalaible_space_y/(alien_height*2))
    return number_aliens_y
    

def create_alien(ai_setting, screen, aliens, alien_number,row):
    """Create an alien and place it in the row."""
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * row * alien_height
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_setting, screen, ship, aliens):
    '''Create a full fleet of aliens'''
    #create an alien and find the number of aliens in a row.
    alien = Alien(ai_setting, screen)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height ,alien.rect.height)

    #Create a first row of aliens.
    for row in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, aliens, alien_number, row)


def update_aliens(ai_setting, stats, screen, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
    and then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(aliens, ai_setting)
    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets)
    aliens.update()
    #look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, screen, ship, aliens, bullets)


def ship_hit(ai_setting, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left
        stats.ships_left -= 1
        # Empty the list of aliens and bullets.
        bullets.empty()
        aliens.empty()
        #Create a new fleet and center the ship
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()
        #pause
        sleep(0.5)
    else:
        stats.game_active = False
        ai_setting.inicial_settings_fleet()
        pygame.mouse.set_visible(True)


def check_fleet_edges(aliens, ai_setting):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens, ai_setting)
            break


def change_fleet_direction(aliens, ai_setting):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.y += alien.ai_setting.fleet_drop_speed
        alien.rect.y = alien.y

    ai_setting.fleet_direction  = -1 * ai_setting.fleet_direction 


def check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit
            ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
            break

def check_level(stats):
    '''levels up when the entire fleet is killed'''
    stats.score += 1
