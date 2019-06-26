class Grupo():
    energia = 200
    def mejorEleccionI(self, agentes):
        datos=[]
        maxI=[]
        prom =0
        for i in agentes.equipo:
            maxI.append(i.i)
            prom += i.i / len(agentes.equipo)
            pensar = self.energia-i.pensar
        self.energia = self.energia - pensar
        datos.append(max(maxI))
        datos.append(prom)
        datos.append(pensar)

        return datos

    def mejorEleccionN(self, agentes):
        datos=[]
        maxN=[]
        prom =0
        for i in agentes.equipo:
            maxN.append(i.n)
            prom += i.n / len(agentes.equipo)
            pensar = self.energia-i.pensar
        self.energia = self.energia - pensar
        datos.append(max(maxN))
        datos.append(prom)
        datos.append(pensar)

        return datos
    def mejorEleccionC(self, agentes):
        datos=[]
        maxC=[]
        prom =0
        for i in agentes.equipo:
            maxC.append(i.c)
            prom += i.c / len(agentes.equipo)
            pensar = self.energia-i.pensar
        self.energia = self.energia - pensar
        datos.append(max(maxC))
        datos.append(prom)
        datos.append(pensar)

        return datos
