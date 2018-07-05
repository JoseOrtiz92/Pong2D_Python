from pygame.locals import *
import pygame
from loadImage import *
from time import *

width = 640
height =520
dir="images"
puntos=[0,0]

class Pelota(pygame.sprite.Sprite):

    def __init__(self, sonidoGolpe, sonidoPunto):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bola.png", dir, alpha=True)
        self.rect = self.image.get_rect() #Se genera un rectangulo de la imagen de la bola
        self.rect.centerx = width / 2 #Centra la imagen
        self.rect.centery = height/ 2 #Centra la imagen
        self.speed = [4, 3] #La velocidad por la que la pelota se mueve por la ventana
        self.sonidoGolpe=sonidoGolpe
        self.sonidoPunto=sonidoPunto

    def actualizar(self):
        #Sistema de puntuacion
        if self.rect.left <= 0:
            puntos[1] += 1 #puntos para el Jugador 2
        if self.rect.right >= width:
            puntos[0] += 1 #puntos para el Jugador 1

        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
            self.sonidoPunto.play() #Reproducimos el sonido
            sleep(1)
            self.rect.centerx = width / 2  # Cuando marco punto centro la imagen otra vez
            self.rect.centery = height / 2
            self.speed = [4, 3] #Reinicio la velocidad


        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
        return puntos

    def colision(self, objetivo): #Control de colisiones ya que la pelota choca con todos los sprites
        if self.rect.colliderect(objetivo.rect):
            self.speed[0] = -self.speed[0]*1.12 #Aumenta la velocidad progresivamente
            self.sonidoGolpe.play()