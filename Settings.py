class Settings:
    """the class storing all the setting in the game"""

    def __init__(self):
        """init game setings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # speed control
        self.speed = 1.5

        #setings for bullet
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
