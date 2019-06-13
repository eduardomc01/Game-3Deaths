#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
from pygame.locals import *

# Constantes
#WIDTH = 555
#HEIGHT = 550

WIDTH = 1300
HEIGHT = 500


# Clases
# ---------------------------------------------------------------------
class Agentes(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/persona.png", True)
        self.image = pygame.transform.scale(self.image,(80,80))
        #self.rect = self.image.get_rect()
        #self.
        #self.rect.centerx = WIDTH / 2
        #self.rect.centery = HEIGHT / 2
        #self.rect.top = HEIGHT / 2
        #self.speed = [0.1, -0.1]

        self.equipo = []

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
    image = pygame.image.load(filename)
    image = image.convert()

    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image
# ---------------------------------------------------------------------

def main():
    SPEED = 50
    POSX = 0
    POSY = 0

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Proyecto IA - 3Deaths")
    background_image = load_image('imagenes/piso2.jpg')
    agentes = Agentes()

    while True:

        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                return 0

            elif eventos.type == pygame.KEYDOWN:
                print(eventos.key)
                if eventos.key == K_LEFT:
                    POSX -= SPEED
                elif eventos.key == K_RIGHT:
                    POSX += SPEED
                elif eventos.key == K_UP:
                    POSY -= SPEED
                elif eventos.key == K_DOWN:
                    POSY += SPEED


        screen.fill(pygame.Color(255,255,9)) #color de fondo
        screen.blit(background_image, (0, 0)) #imagen de background
        screen.blit(agentes.image, (POSX,POSY))


        pygame.display.flip()
    return 0

if __name__ == '__main__':
    #pygame.init()


    main()
