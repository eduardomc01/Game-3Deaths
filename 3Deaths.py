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
class Candidato(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/persona.png", True)
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        #self.rect.centerx = WIDTH / 2
        #self.rect.centery = HEIGHT / 2
        self.rect.top = HEIGHT / 2
        self.speed = [0.1, -0.1]
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

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Proyecto IA - 3Deaths")
    background_image = load_image('imagenes/piso2.jpg')
    candidato = Candidato()

    while True:

        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                return 0



        screen.blit(background_image, (0, 0))
        screen.blit(candidato.image, candidato.rect)



        pygame.display.flip()
    return 0

if __name__ == '__main__':
    pygame.init()


    main()
