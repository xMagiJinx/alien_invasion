import sys

import pygame

from background import Background
from smile_character import Smile

class CharacterDisplay:
    def __init__(self):
        pygame.init()
        self.settings = Background()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Ed's Face")

        self.ed = Smile(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ed.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    char = CharacterDisplay()
    char.run_game()