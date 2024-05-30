#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:17:47 2024

@author: class
"""
import random as rnd

class Konto:
    def __init__(self,inhaber,betrag):
        self.__ktonummer=f'{inhaber[0:3]}{rnd.randint(100,999)}'
        self.__inhaber=inhaber
        if betrag<0:
            self.__guthaben=0
        else:
            self.__guthaben=betrag
        
    def einzahlen(self,betrag):
        if betrag > 0:
            self.__guthaben+=betrag
        else:
            print("Sie koennen nur einen positiven Beitrag einzahlen.")
            
    def abheben(self,betrag):
        if betrag>self.__guthaben:
            print("Es ist nicht genug Guthaben vorhanden")
        else:
            self.__guthaben-=betrag
            
    def getInhaber(self):
        return self.__inhaber
    
    def getKontostand(self):
        return self.__guthaben
            
        
    def __str__(self):
        return f"{self.__ktonummer}({self.__inhaber}): {self.__guthaben} EUR"
        