class Grupo():
    def mejorEleccionI(self, agentes):
        datos=[]
        maxI=[]
        prom =0 
        for i in agentes.equipo:
            maxI.append(i.i)
            prom += i.i / len(agentes.equipo)
            pensar = i.pensar
        datos.append(max(maxI))
        datos.append(prom)
        datos.append(pensar)

        return datos

'''
    def mejorEleccionN(self, agentes):
        for i in agentes.equipo:
            print (i.i, i.n, i.c, i.vida, i.pensar)

    def mejorEleccionC(self, agentes):
        for i in agentes.equipo:
            print (i.i, i.n, i.c, i.vida, i.pensar)

    def autoFunction(self):
        auto=0
'''
