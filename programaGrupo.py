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

    def mejorEleccionA(self, agentes):
        datos=[]
        maxN=[]
        prom =0
        for i in agentes.equipo:
            maxN.append(i.a)
            prom += i.a / len(agentes.equipo)
            pensar = self.energia-i.pensar
        self.energia = self.energia - pensar
        datos.append(max(maxN))
        datos.append(prom)
        datos.append(pensar)

        return datos
    def mejorEleccionR(self, agentes):
        datos=[]
        maxC=[]
        prom =0
        for i in agentes.equipo:
            maxC.append(i.r)
            prom += i.r / len(agentes.equipo)
            pensar = self.energia-i.pensar
        self.energia = self.energia - pensar
        datos.append(max(maxC))
        datos.append(prom)
        datos.append(pensar)

        return datos
