class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_height = 750
        self.screen_width = 1200
        self.bg_color = (230,230,230)

        #ship setting
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60     
        self.bullets_allowed = 3   
        
        #Alien settings
        self.inicial_settings_fleet()

    def inicial_settings_fleet(self):
        #Alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    
    def next_level(self):
        self.alien_speed_factor = self.alien_speed_factor*1.1
        self.fleet_drop_speed += 5

        
        