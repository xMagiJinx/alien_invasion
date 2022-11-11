class Settings:
    """Store all settings for star homework"""

    def __init__(self):
        """Init settings"""
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (255,255,255)

        self.ship_speed = 3
        self.ship_limit = 3

        self.bullet_speed = 6.0
        #going sideways so now the width is longer than height
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        # make aliens appear at random
        self.alien_appear = .02
        self.alien_speed = .5
