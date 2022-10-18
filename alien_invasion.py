import sys
import pygame
from setting import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and resources"""
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        """Start main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()
            #watches for events from keyboard and mouse

            self.screen.fill(self.setting.bg_color)

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
