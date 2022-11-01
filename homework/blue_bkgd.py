import sys
import pygame
from background import Background


class Blue:
    def __init__(self):
        pygame.init()
        self.background = Background()
        self.screen = pygame.display.set_mode((self.background.screen_width, self.background.screen_height))
        pygame.display.set_caption("Blue Background")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.background.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    bsg = Blue()
    bsg.run_game()
