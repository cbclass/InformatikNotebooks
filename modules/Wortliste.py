#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:43:28 2024

@author: class
"""

class Wortliste:
    
    def __init__(self,listenname):
        self.__name=listenname
        self.__worte=[]
        
    def fuegeWortHinzu(self,wort):
        if wort not in self.__worte:
            self.__worte.append(wort)
            
    def entferneWort(self,wort):
        if wort in self.__worte:
            self.__worte.remove(wort)
            
    def gibtDieWorteAus(self):
        print(f'die Worte der Liste {self.__name} sind:')
        for w in self.__worte:
            print(w)
            
    def __str__(self):
        return f"Die Liste {self.__name} hat {len(self.__worte)} Worte."