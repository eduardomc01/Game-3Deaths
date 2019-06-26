# Modulos
# ----------------------------------------------------------------------------
import pygame
from pygame.locals import *

import programaGrupo

import programaRetos
from programaRetos import *

import sys
import random
#import time

#----------------------------------------------------------------------------

# Global
#--------------------------------------------------------------------------
WIDTH = 1300   #1300
HEIGHT = 650
GAME_OVER = [False]
GAME_OVER_LOCURA = [False]
# ---------------------------------------------------------------------

# Clases
# ---------------------------------------------------------------------
class Agentes(pygame.sprite.Sprite, programaGrupo.Grupo, programaRetos.Retos):

    def __init__(self, i, n, c, vida, pensar):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/grupo.png")
        self.image = pygame.transform.scale(self.image,(100,50))
        self.speed = 5

        self.rect = self.image.get_rect()

        self.i = i #inteligencia
        self.n = n #nadado
        self.c = c #correr
        self.vida = vida
        self.pensar = pensar

        self.equipo = []


    def load_image(self, filename, transparent=False):
        image = pygame.image.load(filename)
        image = image.convert()
        return image


    def AgregarPersonajes(self, agentes, equipo, screen):
        for i in range(3):
            agentes.equipo.append(Agentes(random.randint(1,10),random.randint(1,10),random.randint(1,10),500, 200))


    def ActualizarAtributos(self, screen, agentes):
        if(agentes.i != 0):
            #print(agentes.i, agentes.n, agentes.c, agentes.vida, agentes.pensar)
            self.barras1(screen, agentes.vida, agentes.pensar)
            self.VidayPensar(screen, agentes)

        else:
            for n in agentes.equipo:
                self.ActualizarAtributos(screen, n)

    def VidayPensar(self, screen, agentes):
        miFuente = pygame.font.SysFont("Arial", 20, True)

        textoPensar = miFuente.render((str(agentes.pensar)+" %"),0,(0, 0, 0))
        screen.blit(textoPensar,(220, 526))

        textoVida = miFuente.render((str(agentes.vida)+" %"),0,(0, 0, 0))
        screen.blit(textoVida,(310, 590))


    def RestartVida(self, screen, agentes, Rvida):
        agentes.vida -= Rvida
        if(agentes.i != 0):
            if(agentes.vida == 0):
                GAME_OVER.pop()
                GAME_OVER.append(True)
                #pygame.time.delay(5000)
                #miFuente = pygame.font.SysFont("Arial", 50)
                #miTexto = miFuente.render("GAME OVER",0,(255, 0, 0))
                #screen.blit(miTexto,(850, 530))
        else:
            for n in agentes.equipo:
                self.RestartVida(screen, n, Rvida)


    def RestarPensar(self, screen, agentes, Rpensar):
        agentes.pensar -= Rpensar
        if(agentes.i != 0):

            if(agentes.pensar == 0):
                GAME_OVER_LOCURA.pop()
                GAME_OVER_LOCURA.append(True)

        else:
            for n in agentes.equipo:
                self.RestarPensar(screen, n, Rpensar)


    def nivelEnJuego1(self, screen, agentes):
        nivel1 = pygame.image.load('imagenes/barda1.png')
        screen.blit(nivel1,(0,50))
        transparent = pygame.Surface((0,0),pygame.SRCALPHA)

        bloque1 = pygame.Rect(250,100,103,10)
        bloque2 = pygame.Rect(630,100,103,10)
        bloque3 = pygame.Rect(1040,100,103,10)

        if(bloque1.colliderect(agentes)):

            t = [3000, 1000, 5000]
            for i in range(3):
                self.AgregarTiempo(t.pop())

            v = [20,11,15,13,7,9,11,2,9]
            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, v.pop(), i.t)

            #self.ImprimirRetos(retos, "-")
            datos = self.mejorEleccionI(agentes)
            print("--->",datos)

            #input("S T O P")

            #pygame.time.delay(3000)
            self.RestartVida(screen, agentes, 100)

            #print("------------------")
            #retos.ImprimirRetos(retos,"-")
            #print("------------------")

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            print("\n bloque 1 nivel 1")

        Band1 = True
        rec1 = (0,115,1300,0)

        if Band1:
            borde1 = pygame.draw.rect(screen, (0,0,0,0), rec1, 0)

        if(borde1.colliderect(agentes)):
            agentes.rect.top+=5

        elif(bloque2.colliderect(agentes)):
            pygame.time.delay(10000)
            self.RestartVida(screen, agentes, 1)

            for i in range(3):
                retos.AgregarRetos(20,10)

            #print("------------------")
            #retos.ImprimirRetos(retos,"-")
            #print("------------------")

            agentes.rect.top += 60

            retos.ReiniciarRetos(retos)
            print("\n bloque 2 nivel 1")

        Band2 = True
        rec2 = (0,245,1300,0)

        if Band2:
            borde2 = pygame.draw.rect(screen, (0,0,0,0), rec2, 0)

        if(borde2.colliderect(agentes)):
            agentes.rect.top+=5

        elif(bloque3.colliderect(agentes)):
            pygame.time.delay(20000)
            self.RestartVida(screen, agentes, 1)

            for i in range(3):
                retos.AgregarRetos(5, 20)

            #print("------------------")
            #retos.ImprimirRetos(retos,"-")
            #print("------------------")

            agentes.rect.top += 60

            retos.ReiniciarRetos(retos)
            print("\n bloque 3 nivel 1")

        Band3 = True
        rec3 = (0,372,1300,0)

        if Band3:
            borde3 = pygame.draw.rect(screen, (0,0,0,0), rec3, 0)

        if(borde3.colliderect(agentes)):
            agentes.rect.top+=5


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

            pygame.time.delay(2000)
            agentes.rect.top += 101
            #print("\n bloque 1 nivel 2")

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
        color2 = (40, 210, 250)
        rect2 = (144, 526, pensar, 22)
        pygame.draw.rect(screen, color2, rect2, 0)

        color1 = (255, 0, 0, 0)
        rect1 = (98, 584, vida, 31) #el tercer parametro es la vida 500 = 100%
        pygame.draw.rect(screen, color1, rect1, 0)

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
                agentes.rect.left -= agentes.speed
                if (key[K_UP] or key[K_w]):
                    if agentes.rect.top == 0:
                        pass
                    else:
                        sonidoCaminando.play()
                        agentes.rect.top -= agentes.speed

                elif (key[K_DOWN] or key[K_s]):
                    print(agentes.rect.top)
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
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
            return 0


    def MouseClick(self, screen, agentes, sonidoSusurrando):
        if(pygame.mouse.get_pressed()[0]):
            self.RestarPensar(screen, agentes, 1)
            sonidoSusurrando.play()


    def verificarFinDelJuego(self, screen, gameover, gameoverlocura):
        if(GAME_OVER[0] == True):
            screen.blit(gameover,(400,100))
            pygame.time.wait(900)

        elif(GAME_OVER_LOCURA[0] == True):
            screen.blit(gameoverlocura,(150,100))
            pygame.time.wait(900)


    def logotiposExtra(self, screen):
        screen.blit(pygame.image.load('imagenes/vidaypensar.png'),(0,0))
        #screen.blit(pygame.transform.scale(pygame.image.load('imagenes/vidaypensar.png'),(50,50)),(0,0))
        #screen.blit(pygame.transform.scale(pygame.image.load('imagenes/vida.png'),(75,75)),(5,545))

        '''
        elif(pygame.mouse.get_pressed()[2]):

            pygame.display.set_mode((200, 200))
            pygame.display.set_caption("Instrucciones del JUEGO")

            while True:
                for evento in pygame.event.get():
                    if evento.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        return 0
        '''
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

    color = (0,0,0,0)
    rec1 = (0,0,1300,0)
    rec2 = (0,0,1,650)
    rec3 = (0,650,1300,0)
    rec4 = (1299,0,0,650)
    width = 0

    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #,RESIZABLE vuelve la pantalla manipulable

    pygame.display.set_caption("Proyecto IA - 3Deaths")

    background = agentes.load_image('imagenes/fondo.png')

    footer = agentes.load_image('imagenes/footer.png')
    #bandaInfo = agentes.load_image('imagenes/info.png')

    gameover = pygame.image.load('imagenes/gameOver.png')
    gameoverlocura = pygame.image.load('imagenes/locura.png')

    sonidoCaminando = pygame.mixer.Sound("sonidos/trotar.wav")
    sonidoSusurrando = pygame.mixer.Sound("sonidos/susurro.wav")
    sonidoMuerte = pygame.mixer.Sound("sonidos/morir.wav")

    pygame.mixer.music.load("sonidos/solve_puzzle.wav")
    pygame.mixer.music.play(100)

    agentes.AgregarPersonajes(agentes, agentes.equipo, screen)

    while True:

        pygame.mixer.music.rewind()
        screen.blit(footer,(0,0))
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


        agentes.MouseClick(screen, agentes, sonidoSusurrando)

        agentes.MovimientoTeclas(agentes, sonidoCaminando)

        agentes.nivelEnJuego1(screen, agentes)
        agentes.nivelEnJuego2(screen, agentes)
        agentes.nivelEnJuego3(screen, agentes)

        agentes.verificarFinDelJuego(screen, gameover, gameoverlocura)

        #borde1 = pygame.draw.rect(screen, color, rec1, width)
        borde2 = pygame.draw.rect(screen, color, rec2, width)
        borde3 = pygame.draw.rect(screen, color, rec3, width)
        borde4 = pygame.draw.rect(screen, color, rec4, width)

        #blocks_hit_list = pygame.sprite.spritecollide(agentes, borde1, True)

        '''
        if(borde1.colliderect(agentes)):
            agentes.rect.top+=5
        '''

        agentes.logotiposExtra(screen)

        print("------------------")
        agentes.ActualizarAtributos(screen, agentes)
        print("------------------")

        pygame.display.update()
        pygame.display.flip()

        #return 0

# ---------------------------------------------------------------------


# Main
#----------------------------------------------------------------------
if __name__ == '__main__':

    main()
