# -*- coding: utf-8 -*-
#informació de cada paraula



class Paraula:
    
    def __init__(self, _longitud):
        
        self.contingut = ""
        self.longitud = _longitud
        self.colisions={}
        self.domini=[]
        
        #això només ho necessitem per facilitar-nos el fet de mostrar-ho gràficament després
        self.posicio=[]
        self.horitzontal = True

    def afegirContingut(self, _contingut):
        
        self.contingut = _contingut
    
    def getContingut(self):
        return self.contingut
        
    def afegirLongitud(self, _longitud):
        
        self.longitud= _longitud
        
    def afegirColisions(self, clau, valor):
        
        if clau in self.colisions:
            self.colisions[clau].append(valor)
        else:
            self.colisions[clau] = valor
        
    def getColisions(self):
        return self.colisions
        
    def mostralongituds(self):
        print(self.longitud)
        
    def afegeixdomini(self, _domini):
        self.domini = _domini
    
    def getdomini(self):
        return self.domini
    
    def getIDcolisions(self):
        return self.colisions.keys()
    
    def setPosicio(self, _posicio):
        self.posicio = _posicio
        
    def getPosicio(self):
        return self.posicio
        
    def setHoritzontal(self, _horitzontal):
        self.horitzontal = _horitzontal
        
    def getHoritzontal(self):
        return self.horitzontal