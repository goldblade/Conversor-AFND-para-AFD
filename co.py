#!/usr/bin/python
# Clase AFN para transformar un AFN en un AFD

class AFN:
    def __init__(self,AFN):
        self.AFN = AFN
        self.SimbolosDelLenguaje =  self.LenguajeDeAFN()
        self.AFD = self.ToAFD()
    def Transaccion(self,e,t):
        return filter(lambda s:s[0]==t,filter(lambda s:s[0]==e,self.AFN)[0])[0][1]

    def EstadoInicial(self):
        # retorna una lista con el unico estado inicial
        return filter(lambda s:len(s)>=4 and s[3]=='>',self.AFN) #simpre tendria que ser uno por definicion de automatas

    def LenguajeDeAFN(self):
        # simbolos del lenguaje del AFN
        return [l[0] for l in  filter(lambda s:len(s)==2,self.AFN[-1])];

    def EstadosTratados(self):
        return [e[0] for e in  self.AFD] # los estados de llegada que fueron tratados

    def EstadosNoTratados(self):
        return map(lambda e:e[1],filter(lambda s:s[0] in self.SimbolosDelLenguaje and s[1] not in self.EstadosTratados(),self.AFD[-1]))

    def ToAFD(self):
        self.AFD =[]
        vecEstTmp= self.EstadoInicial()

        while len(vecEstTmp) <> 0:
            self.AFD.append( vecEstTmp[0])
            for estado in self.EstadosNoTratados(): #se recorren todos los estados que no fueron tratados
                TransaccionDelAFD=[] #en este vector se calculara los  las transacciones del AFD resultantes
                for simbolo in self.SimbolosDelLenguaje: # recorro para todos los simbolos del lenguaje
                    nuevoEstado=[]                       # defino nuevoEstado para armar el nuevo estado del AFD
                    for e in estado:                     # calculo la union con los conjuntos de llegada de todos los estados
                        for t in self.Transaccion([e],simbolo):
                            if t not in nuevoEstado:
                                nuevoEstado.append(t)
                        nuevoEstado.sort()

                    TransaccionDelAFD.append([simbolo,nuevoEstado])

                vecEstTmp.append([estado]+TransaccionDelAFD)

            vecEstTmp.pop(0)

        #busco los estados de Aceptacion y le pongo el *
        estasdosDeAceptacion = [l[0][0] for l in filter(lambda s:len(s)>=4 and s[-1]=='*',self.AFN)] #estados de Aceptacion
        for e in self.AFD:
            Aceptacion = False
            for ea in estasdosDeAceptacion :
                        if not Aceptacion:
                            Aceptacion =  ea in e[0]
            if Aceptacion and '*' not in e: e.append('*')

        return self.AFD

AUT = AFN(
        [
        [ [1], ['a',[1]] ,['b',[1,2]],'>'],
        [ [2], ['a',[] ] ,['b',[3]  ]],
        [ [3], ['a',[3]] ,['b',[3]  ],'*']
        ]#tabla de trancicion marcando con una -> el estado inicial y con * los estados favorables
        )

for l in  AUT.AFD:
    print l