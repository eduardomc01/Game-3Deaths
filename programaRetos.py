class Retos():
    def __init__(self, nivel, t1, t2, h):
        self.nivel = nivel
        self.t1 = t1
        self.t2 = t2
        self.h = h

        self.hijos = []

    def AgregarRetos(self, t1, t2, h):
        retos.hijos.append(Retos(10,t1,t2,h))

    def ReiniciarRetos(self, retos):
        for i in retos.hijos:
            retos.hijos.pop()

    def ImprimirRetos(self, retos, ident):
        #if(retos.nivel != None):
        print(ident, retos.nivel, retos.t1, retos.t2, retos.h)

        #else:
        for n in retos.hijos:
            self.ImprimirRetos(n, ident + "-")

retos = Retos(None,None,None,None)
#retos.AgregarRetos(retos)
#retos.ImprimirRetos(retos, "-")
#input("Detener!")
