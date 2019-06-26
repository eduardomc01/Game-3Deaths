class Retos():
    def __init__(self, t, gv, h):
        self.t = t
        self.gv = gv
        self.h = h

        self.hijos = []

    def AgregarTiempo(self, t):
        retos.hijos.append(Retos(t,0,0))

    def AgregarGvida(self, retos, gv, busq):
        nodo = self.BusquedaNodoTiempo(retos, busq)
        nodo.hijos.append(Retos(0,gv,0))

    def BusquedaNodoTiempo(self, retos, busq):
        if(retos.t != None):
            if(retos.t == busq):
                return retos
        else:
            for x in retos.hijos:
                e = self.BusquedaNodoTiempo(x, busq)
                if(e != None):
                    return e

    def tiempo_pensar(self,retos,lista):
        for x in retos.hijos:
            x.t = x.t - lista[1]*lista[2]

    def mas_optimo(self, retos):
        for x in retos.hijos:
            for y in x.hijos:
                y.h = ((x.t + y.gv)/500)*200   

    def ReiniciarRetos(self, retos):
        for i in retos.hijos:
            retos.hijos.pop()
            return self.ReiniciarRetos(retos)

    def ImprimirRetos(self, retos, ident):
        if(retos.t != None):
            print(ident, retos.t, retos.gv,retos.h)

        #else:
        for n in retos.hijos:
            self.ImprimirRetos(n, ident + "-")

retos = Retos(None,None,None)
#retos.AgregarRetos(retos)
#retos.ImprimirRetos(retos, "-")
#input("Detener!")
