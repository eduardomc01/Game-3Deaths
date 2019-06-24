
class ArbolRetos():
    def __init__(self, nivel, heuristica, otro, x, y):
        self.nivel = nivel
        self.heuristica = heuristica
        self.otro = otro
        self.posx = x
        self.posy = y

        self.hijos = []

    def AgregarRetos(self, retos):
        for i in range(4):
            retos.hijos.append(ArbolRetos(i,0,0,0,0))

    def ImprimirRetos(self, retos, ident):
        #if(retos.nivel != None):
        print(ident, retos.nivel, retos.heuristica, retos.otro, retos.posx, retos.posy)
        #else:
        for n in retos.hijos:
            self.ImprimirRetos(n, ident + "-")


retos = ArbolRetos(None,None,None,None,None)

retos.AgregarRetos(retos)
retos.ImprimirRetos(retos, "-")

input("Detener!")
