# Modulos
# ----------------------------------------------------------------------------
import pygame
import sys
from pygame.locals import *
#----------------------------------------------------------------------------

# Global
#--------------------------------------------------------------------------
WIDTH = 1300
HEIGHT = 650

# ---------------------------------------------------------------------

# Clases
# ---------------------------------------------------------------------
class Agentes(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = load_image("imagenes/ball.png", True)
        self.image = pygame.image.load("imagenes/persona.png")
        self.image = pygame.transform.scale(self.image,(60,60))
        self.speed = 4
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


def nivelEnJuego1(screen, agentes):

    nivel1 = pygame.image.load('imagenes/barda1.png')
    #nivel1 = pygame.transform.scale(nivel1,(700,70))
    screen.blit(nivel1,(0,50))
    transparent = pygame.Surface((0,0),pygame.SRCALPHA)

    bloque1 = pygame.Rect(260,60,100,50)
    bloque2 = pygame.Rect(630,60,100,50)
    bloque3 = pygame.Rect(1040,60,100,50)

    pygame.draw.rect(screen,(0,0,0), transparent.get_rect())

    if(bloque1.colliderect(agentes)):
        print("\n bloque 1 nivel 1")

    elif(bloque2.colliderect(agentes)):
        print("\n bloque 2 nivel 1")

    elif(bloque3.colliderect(agentes)):
        print("\n bloque 3 nivel 1")


def nivelEnJuego2(screen, agentes):

    nivel2 = pygame.image.load('imagenes/barda2.png')
    screen.blit(nivel2,(0,180))
    transparent = pygame.Surface((0,0),pygame.SRCALPHA)

    bloque1 = pygame.Rect(90,190,100,50)
    bloque2 = pygame.Rect(420,190,100,50)
    bloque3 = pygame.Rect(810,190,100,50)
    bloque4 = pygame.Rect(1100,190,100,50)

    pygame.draw.rect(screen,(0,0,0), transparent.get_rect())

    if(bloque1.colliderect(agentes)):
        print("\n bloque 1 nivel 2")

    elif(bloque2.colliderect(agentes)):
        print("\n bloque 2 nivel 2")

    elif(bloque3.colliderect(agentes)):
        print("\n bloque 3 nivel 2")

    elif(bloque4.colliderect(agentes)):
        print("\n bloque 4 nivel 2")


def nivelEnJuego3(screen, agentes):

    nivel3 = pygame.image.load('imagenes/barda3.png')
    screen.blit(nivel3,(0,310))
    transparent = pygame.Surface((0,0),pygame.SRCALPHA)

    bloque1 = pygame.Rect(5,320,75,50)
    bloque2 = pygame.Rect(265,320,75,50)
    bloque3 = pygame.Rect(600,320,90,50)
    bloque4 = pygame.Rect(970,320,80,50)
    bloque5 = pygame.Rect(1230,320,100,50)

    pygame.draw.rect(screen,(0,0,0), transparent.get_rect())

    if(bloque1.colliderect(agentes)):
        print("\n bloque 1 nivel 3")

    elif(bloque2.colliderect(agentes)):
        print("\n bloque 2 nivel 3")

    elif(bloque3.colliderect(agentes)):
        print("\n bloque 3 nivel 3")

    elif(bloque4.colliderect(agentes)):
        print("\n bloque 4 nivel 3")

    elif(bloque5.colliderect(agentes)):
        print("\n bloque 5 nivel 3")


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
        nivelEnJuego1(screen, agentes)
        nivelEnJuego2(screen, agentes)
        nivelEnJuego3(screen, agentes)

        agentes.dibujar(screen)
        pygame.display.update()
        pygame.display.flip()

    #return 0

# ---------------------------------------------------------------------


# Main
#----------------------------------------------------------------------
if __name__ == '__main__':

    main()
