#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
from pygame.locals import *

# Constantes

WIDTH = 555
HEIGHT = 550

# Clases
# ---------------------------------------------------------------------

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
    pygame.display.set_caption("Pruebas Pygame")
    background_image = load_image('fondo-azul-calabozo.png')

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        screen.blit(background_image, (0, 0))
        pygame.display.flip()

    return 0

if __name__ == '__main__':

    pygame.init()

    main()
