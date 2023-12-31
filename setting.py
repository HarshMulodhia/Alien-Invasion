class Settings() :
    """A Class to store all settings for alien invasion"""

    def __init__(self) :
        """Initialize the game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        #Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 100

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
