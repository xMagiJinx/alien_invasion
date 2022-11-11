import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """rain stuff"""

    def __init__(self, rain_game):
        """Init the raindrop"""
        super().__init__()
        self.screen = rain_game.screen
        self.settings = rain_game.settings

        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_offscreen(self):
        """Check if raindrop is at bottom of screen"""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """Move the raindrop down"""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
