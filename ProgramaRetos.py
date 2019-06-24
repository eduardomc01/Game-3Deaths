
class ArbolRetos():
    def __init__(self, nivel, p, t, x, y):
        self.nivel = nivel
        self.p = p
        self.t = t
        self.posx = x
        self.posy = y

        self.hijos = []

    def AgregarRetos(self, p, t):
        for i in range(4):
            retos.hijos.append(ArbolRetos(i,p,t,0,0))


    def ImprimirRetos(self, retos, ident):
        #if(retos.nivel != None):
        print(ident, retos.nivel, retos.p, retos.t, retos.posx, retos.posy)

        #else:
        for n in retos.hijos:
            self.ImprimirRetos(n, ident + "-")

retos = ArbolRetos(None,None,None,None,None)

#retos.AgregarRetos(retos)
#retos.ImprimirRetos(retos, "-")

input("Detener!")
