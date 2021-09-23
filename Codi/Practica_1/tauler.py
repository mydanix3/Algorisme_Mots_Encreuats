# -*- coding: utf-8 -*-
import paraula
#classe tauler a on llegirem el fitxer de text del tauler i el transformarem en una llista de les paraules 
#amb les diferentes restriccions (longitud i col·lisions amb altres paraules)


class Tauler:
    
    def __init__(self):
        
        self.paraules = []
        self.tauler = []
        self.diccionari = {}
        
    def llegirTauler(self, direcciofitxer):
        
        paraulaID = 0
        llargariaparaula = 0
        primerElement = True
        
        #llegim el fitxer del tauler per linies i separem cada linia a un array dels valors separats
        fila_actual = -1
        f = open(direcciofitxer, "r")
        for linia in f:
            
            fila_actual = fila_actual + 1
            items = linia.split()
            #aprofitem i contem les paraules que son a cada linia horitzontals
            for i in range(len(items)):
                #en cas que hi hagi un espai en blanc posem la casella com l'ID de la paraula
                if items[i] == '0':
                    #si es el primer element ens guardem el valor provisionalment per si despres no es una paraula
                    if primerElement:
                        primerElement = False
                        
                    items[i] = [paraulaID]
                    items[i].append(llargariaparaula)
                    
                    llargariaparaula = llargariaparaula + 1
                else:
                    #contem que una paraula pot tenir tamany 2 ja que en els diccionaris hi han paraules de tamany 2
                    if llargariaparaula >= 2:
                        p = paraula.Paraula(llargariaparaula)
                        
                        #això ens servirà per després mostrar per pantalla gràficament amb més facilitat
                        p.setPosicio([fila_actual, i-llargariaparaula])
                        p.setHoritzontal(True)
                        
                        self.paraules.append(p)
                        
                        
                        paraulaID = paraulaID + 1
                        primerElement = True 
                        llargariaparaula = 0  
                    #en el cas de que no tingui una llargaria superior 
                    else:
                        #en aquest cas vol dir que havia un espai en blanc abans i no era paraula,
                        #si fos true voldria dir que havien dos # seguits
                        if primerElement == False:
                            items[i-1] = "0"
                            primerElement = True 
                            llargariaparaula = 0  
                    
            #al acabar una linea hem de contar-ho també com si fos un # però només els casos positius.
            if llargariaparaula != 0:
                if llargariaparaula >= 2:
                    p = paraula.Paraula(llargariaparaula)
                    
                    #això ens servirà per després mostrar per pantalla gràficament amb més facilitat
                    p.setPosicio([fila_actual, i-llargariaparaula+1])
                    p.setHoritzontal(True)
                    
                    self.paraules.append(p)
                    paraulaID = paraulaID + 1
                    primerElement = True 
                    llargariaparaula = 0  
                #en el cas de que no tingui una llargaria superior 
                else:
                    #en aquest cas vol dir que havia un espai en blanc abans i no era paraula,
                    #si fos true voldria dir que havien dos # seguits
                    if primerElement == False:
                        items[i] = "0"
                        primerElement = True 
                        llargariaparaula = 0  
            self.tauler.append(items)    
            
        #print(self.tauler)
        f.close()
        #ara llegirem les paraules de les columnes, i fàcilment podrem saber amb quina paraula crea un conflicte 
        
        colisions = {}
        
        for j in range(len(self.tauler)):
            
            #podem posar [0] sense problema ja que per a que existeixi len(self.tauler) com a mínim ha d'haber una fila
            #sino len donaria 0 i no entraria aqui directament.
            for i in range(len(self.tauler[0])):
               
               casella_actual = self.tauler[i][j]
                
               if casella_actual == "#":
                   
                   if llargariaparaula >= 2:
                        p = paraula.Paraula(llargariaparaula)
                        
                        #això ens servirà per després mostrar per pantalla gràficament amb més facilitat
                        p.setPosicio([i-llargariaparaula,j])
                        p.setHoritzontal(False)
                        
                        #per cada col·lisió introduïm la seva col·lisió a l'altre paraula
                        for col in colisions.keys():
                            
                            p.afegirColisions(col, colisions[col])
                            
                            aux = []
                            aux.append(colisions[col][1])
                            aux.append(colisions[col][0])
                            
                            self.paraules[col].afegirColisions(paraulaID, aux.copy())
                            
                            aux.clear()
                            
                        self.paraules.append(p)
                        paraulaID = paraulaID + 1
                        
                        
                   llargariaparaula = 0
                   colisions.clear()
               else:
                   
                   if casella_actual != "0":
                       
                       #crearem un diccionari on la clau serà l'ID de l'altra paraula col·lisionada i dintre hi haurà una dupla 
                       #amb les posicions de la col·lisió [pos1, pos2]
                       colisions[casella_actual[0]] = [llargariaparaula]
                       colisions[casella_actual[0]].append(casella_actual[1])
         
                   llargariaparaula = llargariaparaula + 1 
                   
            if llargariaparaula >= 2:
                p = paraula.Paraula(llargariaparaula)
                
                #això ens servirà per després mostrar per pantalla gràficament amb més facilitat
                p.setPosicio([i-llargariaparaula+1,j])
                p.setHoritzontal(False)
                        
                #per cada col·lisió introduïm la seva col·lisió a l'altre paraula
                for col in colisions.keys():
                    
                    p.afegirColisions(col, colisions[col])
                    
                    aux = []
                    aux.append(colisions[col][1])
                    aux.append(colisions[col][0])
                    
                    self.paraules[col].afegirColisions(paraulaID, aux.copy())
                    
                    aux.clear()
                    
                self.paraules.append(p)
                paraulaID = paraulaID + 1
                        
                        
            llargariaparaula = 0
            colisions.clear()
                       
        # for f in self.tauler:
        #     print(f)
            
    def llegirDiccionari(self, direcciofitxer):
        f = open(direcciofitxer, "r")

        for p in f:
            if len(p)-1 not in self.diccionari:
               self.diccionari[len(p)-1] = [p[:-1]]
            else:
                self.diccionari[len(p)-1].append(p[:-1])
        f.close()
        
    def assignarDominiParaula(self):
        
        for p in self.paraules:
            p.afegeixdomini(self.diccionari[p.longitud])
    
    def BackTracking(self, LVA, LVNA, D, R, V):
        
        if not LVNA:
            return V
        
        pID = LVNA[0]
        dom = D[pID]
        
        #creem un nou diccionari amb només les restriccions que son útils fixar-nos per saber si una paraula és vàlida o no
        rest = R[pID]
        rest2 = {}
        for cID in rest.keys():
            if cID in LVA:
                rest2[cID] = rest[cID]
        
        for possiblevalor in dom:
            correcte = True
            #mirem que no hi hagi repeticions
            if possiblevalor in V:
                correcte = False
            else:
                for cID in rest2.keys():
                    paraulacol=V[cID]
                    pos1 = rest2[cID][0]
                    pos2 = rest2[cID][1]
                    if paraulacol[pos2] != possiblevalor[pos1]:
                       
                        correcte = False 
                        break
                
            if correcte:
                V1 = V.copy()
                V1[pID] = possiblevalor
                
                LVNA1 = LVNA.copy()
                LVNA1.pop(0)
                
                solucio = self.BackTracking([pID] + LVA, LVNA1, D, R, V1)
                
                if solucio and "_" not in solucio:
                        
                    return solucio
        
        return []
    
    

    def trobarSolucioBT(self):
        
        lvna = []
        v=[]
        r=[]
        d=[]
        
        for i in range(len(self.paraules)):
            lvna.append(i)
            v.append("_")
            r.append(self.paraules[i].getColisions())
            d.append(self.paraules[i].getdomini())
        
        lva = []
        
        solucio = self.BackTracking(lva, lvna, d, r, v)
        
        if not solucio:
            print("No hi ha sol·lucio amb el diccionari donat")
        else:
            for s in range(len(solucio)):
                self.paraules[s].afegirContingut(solucio[s])
                
        #return solucio
    
    
    def ForwardChecking(self, LVA, LVNA, D, R, V):
        if not LVNA:
            return V
        
        pID = LVNA[0]
        dom = D[pID]
        
        rest = R[pID]
        rest2 = {}
        
        for cID in rest:
            if cID in LVA:
                rest2[cID] = rest[cID]
        

        for possiblevalor in dom:
            correcte = True
            #mirem que no hi hagi repeticions
            if possiblevalor in V:
                correcte = False
            else:
                for cID in rest2.keys():
                    paraulacol=V[cID]
                    pos1 = rest2[cID][0]
                    pos2 = rest2[cID][1]
                    
                    if paraulacol[pos2] != possiblevalor[pos1]:                      
                        correcte = False 
                        break
                
            if correcte:
                #actualitzar dominis
                viable = True
                dominiaux = []
                D1 = D.copy()
                for cID in rest.keys():
                    dominiaux.clear()
                    pos1 = rest[cID][0]
                    pos2 = rest[cID][1]
                    character = possiblevalor[pos1]
                    for paraulaDomini in D[cID]:
                        if character == paraulaDomini[pos2]:
                            dominiaux.append(paraulaDomini)
                    if not dominiaux:
                        viable = False
                        break
                    D1[cID] = dominiaux.copy()
                    
                if viable:
                
                
                    V1 = V.copy()
                    V1[pID] = possiblevalor
                    
                    LVNA1 = LVNA.copy()
                    LVNA1.pop(0)
                    
                    solucio = self.ForwardChecking([pID] + LVA, LVNA1, D1, R, V1)
                    
                    if solucio and "_" not in solucio:
                            
                        return solucio      
    
    def trobarSolucioFC(self):
         
         
        lvna = []
        v=[]
        r=[]
        d=[]
        
        for i in range(len(self.paraules)):
            lvna.append(i)
            v.append("_")
            r.append(self.paraules[i].getColisions())
            d.append(self.paraules[i].getdomini())
        
        lva = []
        
        solucio = self.ForwardChecking(lva, lvna, d, r, v)
        
        if not solucio:
            print("No hi ha sol·lucio amb el diccionari donat")
        else:
            for s in range(len(solucio)):
                self.paraules[s].afegirContingut(solucio[s])
                
        #return solucio
    
    def ForwardCheckingRapid(self, LVA, LVNA, D, R, V):
        
        if not LVNA:
            return V
        
        
        minim = LVNA[0]
        #En aquest cas, mirarem qué valor de LVNA escollim, no escollirem sempre el que estigui al top de la llista.

                        
        if len(LVNA) > 1:
            for index in LVNA[1:]:
                if len(D[index]) < len(D[minim]):
                    minim = index
                elif len(D[index]) == len(D[minim]):
                    if(len(R[index]) > len(R[minim])):
                        minim = index
                         
                
        
        pID = minim
        dom = D[pID]
        
        #calculem si existeix la possibilitat de que es produeixi una col·lisió
        rest = R[pID]
        rest2 = {}
        for cID in rest:
            if cID in LVA:
                rest2[cID] = rest[cID]
        
        #si no hi ha colisions no cal que comprovem si la paraula dintre del domini cumplirà amb les restriccions, ho farà
        #sempre ja que la longitud d ecada paraula ja la tenim en compte abans
        for possiblevalor in dom:
            correcte = True
            #mirem que no hi hagi repeticions
            if possiblevalor in V:
                correcte = False
            else:
                for cID in rest2.keys():
                    paraulacol=V[cID]
                    pos1 = rest2[cID][0]
                    pos2 = rest2[cID][1]
                    if paraulacol[pos2] != possiblevalor[pos1]:  
                        correcte = False 
                        break
                
            if correcte:
                #actualitzar dominis
                viable = True
                dominiaux = []
                D1 = D.copy()
                for cID in rest.keys():
                    dominiaux.clear()
                    pos1 = rest[cID][0]
                    pos2 = rest[cID][1]
                    character = possiblevalor[pos1]
                    for paraulaDomini in D[cID]:
                        if character == paraulaDomini[pos2]:
                            dominiaux.append(paraulaDomini)
                    if not dominiaux:
                        viable = False
                        break
                    D1[cID] = dominiaux.copy()
                    
                if viable:
                
                
                    V1 = V.copy()
                    V1[pID] = possiblevalor
                    
                    LVNA1 = LVNA.copy()
                    LVNA1.remove(pID)
                    
                    solucio = self.ForwardCheckingRapid([pID] + LVA, LVNA1, D1, R, V1)
                    
                    if solucio and "_" not in solucio:
                            
                        return solucio
        return []
    
    
    def trobarSolucioFCRapid(self):
        
    #ordenarem les paraules en ordre de, quantes paraules hi han al diccionari amb aquesta longitud, donarem prioritat a
    #les longituds que hi tinguin menys paraules i després, dintre d'això, ordenarem del major numero de colisions a menys
        
        lvna = []
        v=[]
        r=[]
        d=[]
        
        for i in range(len(self.paraules)):
            lvna.append(i)
            v.append("_")
            r.append(self.paraules[i].getColisions())
            d.append(self.paraules[i].getdomini())
        
        lva = []
        
        solucio = self.ForwardCheckingRapid(lva, lvna, d, r, v)
        
        if not solucio:
            print("No hi ha sol·lucio amb el diccionari donat")
        else:
            for s in range(len(solucio)):
                self.paraules[s].afegirContingut(solucio[s])
                
        #return solucio
        
    
    def mostrarGraficament(self):
        
        for p in self.paraules:
            pos = p.getPosicio()
            posX = pos[0]
            posY = pos[1]
            paraula = p.getContingut()
            if p.getHoritzontal():
                for x in range(len(paraula)):
                    PosY_Actual = posY + x
                    self.tauler[posX][PosY_Actual] = paraula[x]
            else:
                for x in range(len(paraula)):
                    PosX_actual = posX + x
                    self.tauler[PosX_actual][posY] = paraula[x]
        
        for f in self.tauler:
            print(f)
        print()
        