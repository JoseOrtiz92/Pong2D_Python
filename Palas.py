import pygame
from pygame.locals import *
from loadImage import *
width = 640
height = 520
dir="images"
class Palas(pygame.sprite.Sprite):
    "Define el comportamiento de las palas de ambos jugadores"
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("pala.png", dir, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = height / 2

    def humano(self):
        # Controlar que la palas no salga de la pantalla
        if self.rect.bottom >= height:
            self.rect.bottom = height
        elif self.rect.top <= 0:
            self.rect.top = 0