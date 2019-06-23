# Modulos
# ----------------------------------------------------------------------------
import pygame
from pygame.locals import *
import sys
import random
from ProgramaRetos import *

#----------------------------------------------------------------------------


# Global
#--------------------------------------------------------------------------
WIDTH = 1300   #1300
HEIGHT = 650

# ---------------------------------------------------------------------


# Clases
# ---------------------------------------------------------------------
class Agentes(pygame.sprite.Sprite):

    def __init__(self, i, n, c, vida, pensar):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/grupo.png")
        self.image = pygame.transform.scale(self.image,(100,50))
        self.speed = 3

        self.rect = self.image.get_rect()

        self.i = i
        self.n = n
        self.c = c
        self.vida = vida
        self.pensar = pensar

        self.equipo = []


    def load_image(self, filename, transparent=False):
        image = pygame.image.load(filename)
        image = image.convert()
        return image


    def AgregarPersonajes(self, agentes, equipo, screen):
        for i in range(3):
            agentes.equipo.append(Agentes(random.randint(1,10),random.randint(1,10),random.randint(1,10), 500, 300))


    def ActualizarAtributos(self, screen, agentes):
        if(agentes.i != 0):
            print(agentes.i, agentes.n, agentes.c, agentes.vida, agentes.pensar)
            self.barras1(screen, agentes.vida, agentes.pensar)
        else:
            for n in agentes.equipo:
                self.ActualizarAtributos(screen, n)


    def RestartVida(self, screen, agentes, Rvida):
        agentes.vida -= Rvida
        if(agentes.vida == 0):
            miFuente = pygame.font.SysFont("Arial", 50)
            miTexto = miFuente.render("GAME OVER",0,(255, 0, 0))
            screen.blit(miTexto,(850, 530))
        else:
            for n in agentes.equipo:
                self.RestartVida(screen, n, Rvida)


    def RestarPensar(self, screen, agentes, Rpensar):
        agentes.pensar -= Rpensar
        if(agentes.pensar == 0):
            miFuente = pygame.font.SysFont("Arial", 50)
            #miTexto = miFuente.render("GAME OVER",0,(255, 0, 0))
            #screen.blit(miTexto,(850, 530))
        else:
            for n in agentes.equipo:
                self.RestarPensar(screen, n, Rpensar)


    def nivelEnJuego1(self, screen, agentes):
        nivel1 = pygame.image.load('imagenes/barda1.png')
        screen.blit(nivel1,(0,50))
        transparent = pygame.Surface((0,0),pygame.SRCALPHA)

        bloque1 = pygame.Rect(260,60,100,50)
        bloque2 = pygame.Rect(630,60,100,50)
        bloque3 = pygame.Rect(1040,60,100,50)

        pygame.draw.rect(screen,(0,0,0), transparent.get_rect())

        if(bloque1.colliderect(agentes)):
            self.RestartVida(screen, agentes, 1)
            print("\n bloque 1 nivel 1")

        elif(bloque2.colliderect(agentes)):
            print("\n bloque 2 nivel 1")

        elif(bloque3.colliderect(agentes)):
            print("\n bloque 3 nivel 1")

    def nivelEnJuego2(self, screen, agentes):
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


    def nivelEnJuego3(self, screen, agentes):
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


    def barras1(self, screen, vida, pensar):
        color1 = (255, 0, 0, 0)
        rect1 = (1, 550, vida, 50) #el tercer parametro es la vida 500 = 100%
        pygame.draw.rect(screen, color1, rect1, 0)

        color2 = (40, 210, 250)
        rect2 = (1, 520, pensar, 20)
        pygame.draw.rect(screen, color2, rect2, 0)

    '''
    def barras2(screen,agentes):

        color1 = (255,0,0,0)
        rect1 = (10,570,400, 10)
        color2 = (40, 210, 250)
        rect2 = (10,580,400, 10)
        width = 0

        pygame.draw.rect(screen, color1, rect1, width)
        pygame.draw.rect(screen, color2, rect2, width)

    def barras3(screen,agentes):

        color1 = (255,0,0,0)
        rect1 = (10,610, 400, 10)
        color2 = (40, 210, 250)
        rect2 = (10,620, 400, 10)
        width = 0

        pygame.draw.rect(screen, color1, rect1, width)
        pygame.draw.rect(screen, color2, rect2, width)
    '''

    def MovimientoTeclas(self, agentes, sonidoCaminando):
        key = pygame.key.get_pressed()
        if (key[K_LEFT] or key[K_a]):
            if agentes.rect.left == 0:
                pass
            else:
                sonidoCaminando.play()
                agentes.rect.left -= agentes.speed
                if (key[K_UP] or key[K_w]):
                    if agentes.rect.top == 0:
                        pass
                    else:
                        sonidoCaminando.play()
                        agentes.rect.top -= agentes.speed

                elif (key[K_DOWN] or key[K_s]):
                    if agentes.rect.top == 429:
                        pass
                    else:
                        sonidoCaminando.play()
                        agentes.rect.top += agentes.speed

        elif (key[K_d] or key[K_RIGHT]):
            if agentes.rect.left == 1240:
                pass
            else:
                sonidoCaminando.play()
                agentes.rect.left += agentes.speed
                if (key[K_w] or key[K_UP]):
                    if agentes.rect.top == 0:
                        pass
                    else:
                        sonidoCaminando.play()
                        agentes.rect.top -= agentes.speed

                elif (key[K_s] or key[K_DOWN]):
                    if agentes.rect.top == 429:
                        pass
                    else:
                        sonidoCaminando.play()
                        agentes.rect.top += agentes.speed

        elif (key[K_w] or key[K_UP]):
            if agentes.rect.top == 0:
                pass
            else:
                sonidoCaminando.play()
                agentes.rect.top -= agentes.speed

        elif (key[K_s] or key[K_DOWN]):
            if agentes.rect.top == 432:
                pass
            else:
                sonidoCaminando.play()
                agentes.rect.top += agentes.speed

        elif key[K_ESCAPE]:
            pygame.quit()
            sys.exit()
            return 0


    def MouseClick(self, screen, agentes, sonidoSusurrando, retos):
        if(pygame.mouse.get_pressed()[0]):
            self.RestarPensar(screen, agentes, 1)
            sonidoSusurrando.play()
'''
            if (evento.button == 1):
                self.RestarPensar(screen, agentes, 50)
                sonidoSusurrando.play()
                print("boton izquierdo")

            elif (evento.button == 2):
                print("boton enmedio")

            elif (evento.button == 3):
                print("boton derecho")
'''

def main():
    pygame.init()
    agentes = Agentes(0,0,0,0,0)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Proyecto IA - 3Deaths")
    background = agentes.load_image('imagenes/fondo.png')
    bandaDatos = agentes.load_image('imagenes/datos.png')
    sonidoCaminando = pygame.mixer.Sound("sonidos/trotar.wav")
    sonidoSusurrando = pygame.mixer.Sound("sonidos/susurro.wav")
    sonidoMuerte = pygame.mixer.Sound("sonidos/morir.wav")

    agentes.AgregarPersonajes(agentes, agentes.equipo, screen)

    while True:

        screen.blit(bandaDatos,(0,400))
        screen.blit(background,(0,0))
        screen.blit(agentes.image, agentes.rect)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                return 0



            if(evento.type == pygame.KEYUP):
                sonidoCaminando.stop()

            elif(evento.type == pygame.MOUSEBUTTONUP):
                sonidoSusurrando.stop()

        agentes.MouseClick(screen, agentes, sonidoSusurrando, retos)

        print("------------------")
        agentes.ActualizarAtributos(screen, agentes)
        print("------------------")

        agentes.MovimientoTeclas(agentes, sonidoCaminando)

        agentes.nivelEnJuego1(screen, agentes)
        agentes.nivelEnJuego2(screen, agentes)
        agentes.nivelEnJuego3(screen, agentes)

        pygame.display.update()
        pygame.display.flip()

    #return 0

# ---------------------------------------------------------------------


# Main
#----------------------------------------------------------------------
if __name__ == '__main__':

    main()
