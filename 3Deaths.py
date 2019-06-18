import pygame
import sys
from pygame.locals import *

WIDTH = 1300
HEIGHT = 500


# Clases
# ---------------------------------------------------------------------
class Agentes(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = load_image("imagenes/ball.png", True)
        self.image = pygame.image.load("imagenes/persona.png")
        self.image = pygame.transform.scale(self.image,(60,60))
        self.speed = 3
        self.rect = self.image.get_rect()
        self.equipo = []

    def dibujar(self, actor):
        actor.blit(self.image, self.rect)

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

def ParedEnJuego(screen, agentes):

    nivel1 = pygame.image.load('imagenes/barda1.png')
    nivel1 = pygame.transform.scale(nivel1,(700,70))
    screen.blit(nivel1,(0,100))

    reto = pygame.Rect(120,120,50,50)
    pygame.draw.rect(screen,(100,70,70),reto)

    if (reto.colliderect(agentes)):
        print("\n Colisiono!")
    else:
        print("Libre")




def MovimientoTeclas(agentes):
        key = pygame.key.get_pressed()

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


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    #screen.fill((255,255,255))
    pygame.display.set_caption("Proyecto IA - 3Deaths")

    background = load_image('imagenes/fondo.png')



    agentes = Agentes()

    while True:

        screen.blit(background,(0,0))


        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                pygame.quit()
                sys.exit()
                return 0

        MovimientoTeclas(agentes)
        ParedEnJuego(screen, agentes)

        agentes.dibujar(screen)
        pygame.display.update()
        pygame.display.flip()

    #return 0

if __name__ == '__main__':

    main()
