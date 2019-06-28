# Modulos
# ----------------------------------------------------------------------------
import pygame
from pygame.locals import *

import programaGrupo

import programaRetos
from programaRetos import *

import sys
import random

#----------------------------------------------------------------------------

# Global
#--------------------------------------------------------------------------
WIDTH = 1300
HEIGHT = 650
GAME_OVER = [False]
GAME_OVER_LOCURA = [False]
# ---------------------------------------------------------------------

# Clases
# ---------------------------------------------------------------------
class Agentes(pygame.sprite.Sprite, programaGrupo.Grupo, programaRetos.Retos):

    liderAhora = ["inteligente","nadador","bombero"]
    numeroLider = 0

    def __init__(self, i, a, r, vida, pensar, lider):
        pygame.sprite.Sprite.__init__(self)
        self.lider = lider
        self.image = pygame.image.load("imagenes/"+self.lider+".png")
        self.image = pygame.transform.scale(self.image,(100,50))
        self.speed = 5

        self.rect = self.image.get_rect()

        self.i = i #inteligencia
        self.a = a #atletico
        self.r = r #resistencia
        self.vida = vida
        self.pensar = pensar

        self.equipo = []


    def AgregarPersonajes(self, agentes, equipo, screen):
        for i in range(3):
            agentes.equipo.append(Agentes(random.randint(1,10),random.randint(1,10),random.randint(1,10),500, 200, "grupo"))


    def ActualizarAtributos(self, screen, agentes):
        if(agentes.i != 0):
            #print(agentes.lider)
            self.barras1(screen, agentes.vida, agentes.pensar)
            self.VidayPensar(screen, agentes)
            self.intercambiarLider(screen,agentes)
            agentes.lider = self.liderAhora[self.numeroLider]

        else:
            for n in agentes.equipo:
                self.ActualizarAtributos(screen, n)


    def VidayPensar(self, screen, agentes):
        miFuente = pygame.font.SysFont("Arial", 20, True)

        textoPensar = miFuente.render((str(agentes.pensar)+" %"),0,(255, 255, 255))
        screen.blit(textoPensar,(220, 526))

        textoVida = miFuente.render((str(agentes.vida)+" %"),0,(255, 255, 255))
        screen.blit(textoVida,(310, 590))


    def RestartVida(self, screen, agentes, Rvida):
        agentes.vida -= Rvida
        if(agentes.i != 0):
            if(agentes.vida <= 0):
                GAME_OVER.pop()
                GAME_OVER.append(True)
        else:
            for n in agentes.equipo:
                self.RestartVida(screen, n, Rvida)


    def RestarPensar(self, screen, agentes, Rpensar):
        agentes.pensar -= Rpensar
        if(agentes.i != 0):
            if(agentes.pensar <= 0):
                GAME_OVER_LOCURA.pop()
                GAME_OVER_LOCURA.append(True)
        else:
            for n in agentes.equipo:
                self.RestarPensar(screen, n, Rpensar)


    def nivelEnJuego1(self, screen, agentes):
        nivel1 = pygame.image.load('imagenes/barda1.png')
        screen.blit(nivel1,(0,50))
        transparent = pygame.Surface((0,0),pygame.SRCALPHA)

        bloque1 = pygame.Rect(250,100,103,0)
        bloque2 = pygame.Rect(630,100,103,0)
        bloque3 = pygame.Rect(1040,100,103,0)

        if(bloque1.colliderect(agentes)):

            for i in range(3):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionI(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 1 nivel 1")

        Band0 = True
        rec0 = (0,0,1300,0)

        if Band0:
            borde0 = pygame.draw.rect(screen, (0,0,0,0), rec0, 0)

        if(borde0.colliderect(agentes)):
            agentes.rect.top+=5


        Band1 = True
        rec1 = (0,115,1300,0)

        if Band1:
            borde1 = pygame.draw.rect(screen, (0,0,0,0), rec1, 0)

        if(borde1.colliderect(agentes)):
            agentes.rect.top+=5

        elif(bloque2.colliderect(agentes)):

            for i in range(3):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionI(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 2 nivel 1")

        Band2 = True
        rec2 = (0,245,1300,0)

        if Band2:
            borde2 = pygame.draw.rect(screen, (0,0,0,0), rec2, 0)

        if(borde2.colliderect(agentes)):
            agentes.rect.top+=5

        elif(bloque3.colliderect(agentes)):

            for i in range(3):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionI(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 3 nivel 1")

        Band3 = True
        rec3 = (0,372,1300,0)

        if Band3:
            borde3 = pygame.draw.rect(screen, (0,0,0,0), rec3, 0)

        if(borde3.colliderect(agentes)):
            agentes.rect.top+=5


        Band4 = True
        rec4 = (0, 500, 1300, 0)

        if Band4:
            borde4 = pygame.draw.rect(screen, (0,0,0,0), rec4, 0)

        if(borde4.colliderect(agentes)):
            agentes.rect.top-=5

    def nivelEnJuego2(self, screen, agentes):
        nivel2 = pygame.image.load('imagenes/barda2.png')
        screen.blit(nivel2,(0,180))
        transparent = pygame.Surface((0,0),pygame.SRCALPHA)

        bloque1 = pygame.Rect(90,230,100,0)
        bloque2 = pygame.Rect(420,230,100,0)
        bloque3 = pygame.Rect(810,230,100,0)
        bloque4 = pygame.Rect(1100,230,100,0)

        pygame.draw.rect(screen,(0,0,0), transparent.get_rect())

        if(bloque1.colliderect(agentes)):

            for i in range(4):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionA(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 2 nivel 1")

        elif(bloque2.colliderect(agentes)):

            for i in range(4):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionA(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 2 nivel 2")

        elif(bloque3.colliderect(agentes)):

            for i in range(4):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionA(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 3 nivel 2")

        elif(bloque4.colliderect(agentes)):

            for i in range(4):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionA(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 4 nivel 2")

    def nivelEnJuego3(self, screen, agentes):
        nivel3 = pygame.image.load('imagenes/barda3.png')
        screen.blit(nivel3,(0,310))
        transparent = pygame.Surface((0,0),pygame.SRCALPHA)

        bloque1 = pygame.Rect(5,370,75,0)
        bloque2 = pygame.Rect(265,370,75,0)
        bloque3 = pygame.Rect(600,370,90,0)
        bloque4 = pygame.Rect(970,370,80,0)
        bloque5 = pygame.Rect(1230,370,100,0)

        pygame.draw.rect(screen,(0,0,0), transparent.get_rect())

        if(bloque1.colliderect(agentes)):

            for i in range(5):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionR(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 1 nivel 3")

        elif(bloque2.colliderect(agentes)):

            for i in range(5):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionR(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 2 nivel 3")

        elif(bloque3.colliderect(agentes)):

            for i in range(5):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionR(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 3 nivel 3")

        elif(bloque4.colliderect(agentes)):

            for i in range(5):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionR(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 4 nivel 3")

        elif(bloque5.colliderect(agentes)):

            for i in range(5):
                self.AgregarTiempo(random.randint(1000,10000))

            for i in retos.hijos:
                for j in range(len(retos.hijos)):
                    self.AgregarGvida(retos, random.randint(1,10), i.t)

            self.mas_optimo(retos)

            lista = self.mejorEleccionR(agentes)

            self.tiempo_pensar(retos, lista)

            self.hill_climbing(retos)

            pygame.time.delay(int(self.tiempos[0]))
            self.RestartVida(screen, agentes, int(self.optimos[0]/10))
            del self.tiempos[:]
            del self.optimos[:]

            agentes.rect.top += 60

            self.ReiniciarRetos(retos)
            ###############################################print("\n bloque 5 nivel 3")

    def barras1(self, screen, vida, pensar):
        color2 = (40, 210, 250)
        rect2 = (144, 526, pensar, 22)
        pygame.draw.rect(screen, color2, rect2, 0)

        color1 = (255, 0, 0, 0)
        rect1 = (98, 584, vida, 31)
        pygame.draw.rect(screen, color1, rect1, 0)

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
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
            return 0

    def MouseClick(self, screen, agentes, sonidoSusurrando):
        if(pygame.mouse.get_pressed()[0]):
            self.RestarPensar(screen, agentes, 20)
            sonidoSusurrando.play()

        if(pygame.mouse.get_pressed()[2]):
            self.numeroLider += 1
            if(self.numeroLider == 3):
                self.numeroLider = 0

    def intercambiarLider(self, screen, agentes):
        lider = pygame.image.load('imagenes/'+self.liderAhora[self.numeroLider]+'.png')
        screen.blit(pygame.transform.scale(lider,(190,100)),(400,480))

    def verificarFinDelJuego(self, screen, gameover, gameoverlocura):
        if(GAME_OVER[0] == True):
            screen.blit(gameover,(400,100))
            pygame.time.wait(1000)

        elif(GAME_OVER_LOCURA[0] == True):
            screen.blit(gameoverlocura,(150,100))
            pygame.time.wait(1000)

    def verificarGanarDelJuego(self, screen, agentes, win):
        zonaGanadora = pygame.Rect(0, 400, 1300, 100)
        if(zonaGanadora.colliderect(agentes)):
            screen.blit(pygame.transform.scale(win,(500,500)),(380,50))

    def NoPasarParedes(self, screen, agentes):

        color = (155, 155, 255)
        rect = (0, 50, 220, 0)

        if(pygame.draw.rect(screen, color, (0, 53, 220, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (390, 53, 200, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (750, 53, 270, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5


        if(pygame.draw.rect(screen, color, (1155, 53, 150, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (0, 187, 50, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (200, 187, 210, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (538, 187, 240, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (940, 187, 150, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (1230, 187, 150, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (90, 317, 170, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (350, 317, 240, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (700, 317, 255, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (700, 317, 255, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5

        if(pygame.draw.rect(screen, color, (1055, 317, 160, 0), 1).colliderect(agentes)):
            agentes.rect.top-=5


    def logotiposExtra(self, screen, barraVidaHabilidad):
        screen.blit(barraVidaHabilidad,(0,0))

def main():
    pygame.init()

    agentes = Agentes(0,0,0,0,0,"grupo")

    color = (0,0,0,0)
    rec1 = (0,0,1300,0)
    rec2 = (0,0,1,650)
    rec3 = (0,650,1300,0)
    rec4 = (1299,0,0,650)
    width = 0

    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #,RESIZABLE vuelve la pantalla manipulable

    pygame.display.set_caption("Proyecto IA - 3Deaths")

    background = pygame.image.load('imagenes/fondo.png')
    footer = pygame.image.load('imagenes/footer.png')

    N1R1 = pygame.image.load('imagenes/matematicas.png')
    N1R2 = pygame.image.load('imagenes/rompecabezas.png')
    N1R3 = pygame.image.load('imagenes/geometria.png')

    N1R4 = pygame.image.load('imagenes/llave.png')
    N1R5 = pygame.image.load('imagenes/cofre.png')
    N1R6 = pygame.image.load('imagenes/candado.png')
    N1R7 = pygame.image.load('imagenes/busear.png')

    N1R8 = pygame.image.load('imagenes/calor.png')
    N1R9 = pygame.image.load('imagenes/correr.png')
    N1R10 = pygame.image.load('imagenes/quemar.png')
    N1R11 = pygame.image.load('imagenes/quemar-manos.png')
    N1R12 = pygame.image.load('imagenes/cerillos.png')

    gameover = pygame.image.load('imagenes/gameOver.png')
    gameoverlocura = pygame.image.load('imagenes/locura.png')
    win = pygame.image.load('imagenes/win.png')

    barraVidaHabilidad = pygame.image.load('imagenes/vidaypensar.png')

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

        screen.blit(pygame.transform.scale(N1R1,(60,60)),(275,48))
        screen.blit(pygame.transform.scale(N1R2,(80,60)),(638,48))
        screen.blit(pygame.transform.scale(N1R3,(50,50)),(1060,50))

        screen.blit(pygame.transform.scale(N1R4,(185,100)),(40,170))
        screen.blit(pygame.transform.scale(N1R5,(60,60)),(440,180))
        screen.blit(pygame.transform.scale(N1R6,(60,60)),(830,180))
        screen.blit(pygame.transform.scale(N1R7,(60,60)),(1125,180))

        screen.blit(pygame.transform.scale(N1R8,(50,50)),(10,315))
        screen.blit(pygame.transform.scale(N1R9,(50,50)),(280,315))
        screen.blit(pygame.transform.scale(N1R10,(50,50)),(620,315))
        screen.blit(pygame.transform.scale(N1R11,(50,50)),(980,315))
        screen.blit(pygame.transform.scale(N1R12,(50,50)),(1230,315))

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

        agentes.NoPasarParedes(screen, agentes)

        agentes.nivelEnJuego1(screen, agentes)
        agentes.nivelEnJuego2(screen, agentes)
        agentes.nivelEnJuego3(screen, agentes)

        agentes.verificarFinDelJuego(screen, gameover, gameoverlocura)
        agentes.verificarGanarDelJuego(screen, agentes, win)


        pygame.draw.rect(screen, color, rec2, width)
        pygame.draw.rect(screen, color, rec3, width)
        pygame.draw.rect(screen, color, rec4, width)



        agentes.ActualizarAtributos(screen, agentes)
        agentes.logotiposExtra(screen, barraVidaHabilidad)

        pygame.display.update()
        pygame.display.flip()

        #return 0

# ---------------------------------------------------------------------


# Main
#----------------------------------------------------------------------
if __name__ == '__main__':

    main()
