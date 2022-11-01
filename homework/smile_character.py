import pygame


class Smile:
    def __init__(self, ed_smile):
        self.screen = ed_smile.screen
        self.screen_rect = ed_smile.screen.get_rect()

        self.image = pygame.image.load('pictures/smiley.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
