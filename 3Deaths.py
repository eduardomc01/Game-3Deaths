import pygame
from pygame.locals import *

WIDTH = 1300
HEIGHT = 500


# Clases
# ---------------------------------------------------------------------
class Agentes(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/persona.png", True)
        #self.image = pygame.image.load("imagenes/persona.png")
        self.image = pygame.transform.scale(self.image,(80,80))
        self.speed = 3
        self.rect = self.image.get_rect()
        self.equipo = []

    def dibujar(self,actor):
        actor.blit(self.image,self.rect)

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

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Proyecto IA - 3Deaths")
    #fondo = pygame.image.load('imagenes/piso2.jpg')
    background_image = load_image('imagenes/piso2.jpg')
    agentes = Agentes()

    while True:
        key = pygame.key.get_pressed()
        screen.blit(background_image,(0,0))
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                pygame.quit()

        if key[K_LEFT]:
            if agentes.rect.left == 0:
                pass
            else:
                agentes.rect.left -= agentes.speed
                if key[K_UP]:
                    if agentes.rect.top == 0:
                        pass
                    else:
                        agentes.rect.top -= agentes.speed

                elif key[K_DOWN]:
                    if agentes.rect.top == 429:
                        pass
                    else:
                        agentes.rect.top += agentes.speed

        elif key[K_RIGHT]:
            if agentes.rect.left == 1209:
                pass
            else:
                agentes.rect.left += agentes.speed
                if key[K_UP]:
                    if agentes.rect.top == 0:
                        pass
                    else:
                        agentes.rect.top -= agentes.speed

                elif key[K_DOWN]:
                    if agentes.rect.top == 429:
                        pass
                    else:
                        agentes.rect.top += agentes.speed

        elif key[K_UP]:
            if agentes.rect.top == 0:
                pass
            else:
                agentes.rect.top -= agentes.speed

        elif key[K_DOWN]:
            if agentes.rect.top == 429:
                pass
            else:
                agentes.rect.top += agentes.speed

        agentes.dibujar(screen)
        pygame.display.update()

        pygame.display.flip()
    return 0

if __name__ == '__main__':


    main()