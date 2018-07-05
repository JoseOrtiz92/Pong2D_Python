import pygame
from pygame.locals import *
import sys
import os

def load_image(nombre, dir, alpha=False):
    ruta = os.path.join(dir, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image