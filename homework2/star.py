import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """star stuff"""
    def __init__(self, stars):
        """Init the star"""
        super().__init__()
        self.screen = stars.screen

        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)