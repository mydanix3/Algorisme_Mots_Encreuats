# -*- coding: utf-8 -*-

import tauler
import time

direccio_tauler_BC = "../MaterialsPractica1/crossword_CB_v2.txt"
direccio_diccionari_BC = "../MaterialsPractica1/diccionari_CB_v2.txt"

direccio_tauler_A= "../MaterialsPractica1/crossword_A_v2.txt"
direccio_diccionari_A = "../MaterialsPractica1/diccionari_A.txt"


def main():
    
    
    
    tBC = tauler.Tauler()
    
    
    llegir_tauler_start = time.time()
    
    tBC.llegirTauler(direccio_tauler_BC)

    llegir_tauler_final = time.time()
    
    llegir_tauler_total = llegir_tauler_final - llegir_tauler_start
    
    print("Temps trigat en llegir el taulell dels apartats B i C: " + str(llegir_tauler_total))

    
    llegir_diccionari_start = time.time()
    
    tBC.llegirDiccionari(direccio_diccionari_BC)
    
    llegir_diccionari_final = time.time()
    
    llegir_diccionari_total = llegir_diccionari_final - llegir_diccionari_start
    
    print("Temps trigat en llegir el diccionari dels apartats B i C: " + str(llegir_diccionari_total))
    
    
    assignar_domini_start = time.time()
    
    tBC.assignarDominiParaula()
    
    assignar_domini_final = time.time()
    
    assignar_domini_total = assignar_domini_final - assignar_domini_start
    
    print("Temps trigat en assignar el domini a les paraules dels apartats B i C: " + str(assignar_domini_total))
    

    algorisme_BT_start = time.time()
    
    tBC.trobarSolucioBT()
    
    algorisme_BT_final = time.time()
    
    algorisme_BT_total = algorisme_BT_final - algorisme_BT_start
    
    print("Temps trigat en realitzar l'algorisme BackTracking: " + str(algorisme_BT_total))
    
    tBC.mostrarGraficament()
    
    
    
    algorisme_FC_start = time.time()
    
    tBC.trobarSolucioFC()
    
    algorisme_FC_final = time.time()
    
    algorisme_FC_total = algorisme_FC_final - algorisme_FC_start
    
    print("Temps trigat en realitzar l'algorisme ForwardChecking: " + str(algorisme_FC_total))
    
    tBC.mostrarGraficament()
    
    
    
    #Ara llegim l'altre tauler i diccionari
    
    tA = tauler.Tauler()
    
    
    llegir_tauler_start = time.time()
    
    tA.llegirTauler(direccio_tauler_A)
    
    llegir_tauler_final = time.time()
    
    llegir_tauler_total = llegir_tauler_final - llegir_tauler_start
    
    print("Temps trigat en llegir el taulell de l'apartat A: " + str(llegir_tauler_total))
    
    
    llegir_diccionari_start = time.time()

    tA.llegirDiccionari(direccio_diccionari_A)
    
    llegir_diccionari_final = time.time()
    
    llegir_diccionari_total = llegir_diccionari_final - llegir_diccionari_start
    
    print("Temps trigat en llegir el diccionari de l'apartat A: " + str(llegir_diccionari_total))
    
    
    assignar_domini_start = time.time()
    
    tA.assignarDominiParaula()
    
    assignar_domini_final = time.time()
    
    assignar_domini_total = assignar_domini_final - assignar_domini_start
    
    print("Temps trigat en assignar el domini a les paraules de l'apartat A: " + str(assignar_domini_total))
    
    
    algorisme_FCR_start = time.time()
    
    tA.trobarSolucioFCRapid()
    
    algorisme_FCR_final = time.time()
    
    algorisme_FCR_total = algorisme_FCR_final - algorisme_FCR_start
    
    print("Temps trigat en realitzar l'algorisme de BackTracking amb tria de variables dinàmica: " + str(algorisme_FCR_total))
       
    tA.mostrarGraficament()
    
    
    
    
if __name__ == "__main__":
    
    main()