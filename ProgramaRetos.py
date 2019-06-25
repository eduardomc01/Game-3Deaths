
T_Inteligencia = []
P_Pensar = []

class ArbolRetos():
    def __init__(self, nivel, p, t, x, y):
        self.nivel = nivel
        self.p = p
        self.t = t
        self.posx = x
        self.posy = y

        self.hijos = []

    def AgregarRetos(self, p, t):
        retos.hijos.append(ArbolRetos(10,p,t,0,0))

    def ReiniciarRetos(self, retos):
        for i in retos.hijos:
            retos.hijos.pop()

    def ImprimirRetos(self, retos, ident):
        #if(retos.nivel != None):
        print(ident, retos.nivel, retos.p, retos.t, retos.posx, retos.posy)

        #else:
        for n in retos.hijos:
            self.ImprimirRetos(n, ident + "-")

retos = ArbolRetos(None,None,None,None,None)

#retos.AgregarRetos(retos)
#retos.ImprimirRetos(retos, "-")
#input("Detener!")
