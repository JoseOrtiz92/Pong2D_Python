from pygame.locals import *
import pygame
import sys
import os
from Pelota import *
from loadImage import *
from Palas import *
from tkinter import messagebox

width=640
height=520
imgDir="images"
soundDir="music"
intro=True

def splashScreen():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pantalla de inicio")
    fondo = load_image("splash.jpg", imgDir, alpha=False).convert()
    titulo, titulo_rect=texto("REGLAS", 180, 40, 35, [23,7,152])
    r_jueg, r_jueg_rect=texto("-Gana el que consiga 5 goles primero", 185, 80, 30, [23,7,152])
    r_jug1, r_jug1_rect=texto("-Jugador 1 mueve con W y S", 185, 120, 30, [23,7,152])
    r_jug2, r_jug2_rect=texto("-Jugador 2 mueve con arriba y abajo", 185, 160, 30, [23,7,152])

    opciones, opciones_rect=texto("Pulsa Espacio para jugar", 218, 350, 40, [0,0,0])
    opciones2, opciones2_rect=texto("Escape para salir", 218, 390, 40, [0,0,0])

    screen.blit(fondo, (0, 0))
    screen.blit(titulo, titulo_rect)
    screen.blit(r_jueg, r_jueg_rect)
    screen.blit(r_jug1, r_jug1_rect)
    screen.blit(r_jug2, r_jug2_rect)
    screen.blit(opciones, opciones_rect)
    screen.blit(opciones2, opciones2_rect)
    pygame.display.flip()
    while(intro):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    main()
                elif event.key==pygame.K_ESCAPE:
                    sys.exit()



def texto(texto, posx, posy, size, color=(255, 255, 255)):
    fuente = pygame.font.SysFont("FuenteSistema", size) #Crea un objeto de Fuente
    salida = pygame.font.Font.render(fuente, texto, 1, color) #Convierte el texto en un Sprite, el uno pertenece al antialias
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

def loadSound(nombre, soundDir):
    ruta = os.path.join(soundDir, nombre)
    try:
        sonido = pygame.mixer.Sound(ruta)
    except (pygame.error) as message:
        print(ruta)
        print("No se pudo cargar el sonido:", ruta)
        sonido = None
    return sonido

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(soundDir+"/musica.ogg")
    pygame.mixer.music.play(loops=0)

    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Pong para 2 jugadores")

    fondo=load_image("fondo.jpg", imgDir, alpha=False).convert()
    sonidoGolpe=loadSound("pelota.ogg", soundDir)
    sonidoPunto=loadSound("punto.ogg", soundDir)

    bola=Pelota(sonidoGolpe, sonidoPunto)
    jugador1=Palas(15)
    jugador2=Palas(625)

    reloj=pygame.time.Clock() #Creamos un reloj que controla el tiempo de juego
    pygame.key.set_repeat(1, 12)  # Activa repeticion de teclas, primer argumento tiempo de retraso segundo argumento, seungo argumento tiempo entre cada envio en milisegundos
    pygame.mouse.set_visible(False) #Desactiva el cursor dentro de la ventana del juego

    puntos = [0, 0]
    while True:
        #Condicion de victoria
        if(puntos[0]==5):
            messagebox.showinfo("Victoria", "Ganador el jugador 1")
            sys.exit()
        elif(puntos[1]==5):
            messagebox.showinfo("Victoria", "Ganador el jugador 2")
            sys.exit()

        reloj.tick(60)#Seleccionamos los fps en este caso 60

        jugador1.humano()#Actualizamos la posicion de la paleta del jugador 1 y 2
        jugador2.humano()
        puntos=bola.actualizar()#Al inicio del bucle actualizamos la posicion de la bola

        bola.colision(jugador1)#Control de colisiones de la bola
        bola.colision(jugador2)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:#Cuando se pulsa una tecla
                if event.key==K_UP: #Si se pulsa la tecla arriba
                    jugador2.rect.centery-=5
                elif event.key==K_DOWN: #Si se pula la tecla abajo
                    jugador2.rect.centery+=5
                elif event.key==K_w:
                    jugador1.rect.centery-=5
                elif event.key==K_s:
                    jugador1.rect.centery+=5
            elif event.type==pygame.KEYUP: #Cuando se suelta una tecla
                if event.key==K_UP: #Si se suelta la tecla arriba
                    jugador2.rect.centery+=0
                elif event.key==K_DOWN: #Si se suelta la tecla abajo
                    jugador2.rect.centery+=0
                elif event.key==K_w:
                    jugador1.rect.centery+=0
                elif event.key==K_s:
                    jugador1.rect.centery+=0
        #Nombre de jugadores
        n_jug1, n_jug1_rect=texto("Jugador 1", width/4, height/2, 60) #Texto, posicionx, posiciony, tamaño
        n_jug2, n_jug2_rect=texto("Jugador 2", width-width/4, height/2, 60)

        #Sistema de puntuacion
        p_jug1, p_jug1_rect = texto(str(puntos[0]), width / 4, 40, 60)
        p_jug2, p_jug2_rect = texto(str(puntos[1]), width - width / 4, 40, 60)

        #Actualiza la pantalla por cada iteracion del bucle
        screen.blit(fondo, (0, 0))
        screen.blit(p_jug1, p_jug1_rect)
        screen.blit(p_jug2, p_jug2_rect)
        screen.blit(n_jug1, n_jug1_rect)
        screen.blit(n_jug2, n_jug2_rect)
        screen.blit(bola.image, bola.rect)
        screen.blit(jugador1.image, jugador1.rect)
        screen.blit(jugador2.image, jugador2.rect)
        #Guarda los cambios
        pygame.display.flip()

if __name__ == "__main__":
    splashScreen()
