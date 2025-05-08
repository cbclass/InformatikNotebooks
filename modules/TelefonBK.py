# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:34:48 2017

@author: class

updated (Information Hiding, 2025)
"""


class Person:
    
    def __init__(self, name, telNr):
        self.__name=name
        self.__telNr = str(telNr)
    
    def getName(self):
        return self.__name
        
    def getTelefonNr(self):
        return self.__telNr
    
    def setTelefonNr(self, newNumber):
        self.__telNr = str(newNumber)
                
    def __eq__(self, other):
        if type(other)!=Person:
            return NotImplemented
        if self.__name==other.__name:
            return True
        else:
            return False
        
    def __hash__(self):
        return hash(self.__name)
        
    def __str__(self):
        return self.__name + ' hat die Nummer: ' + self.__telNr
            

class Telefonbuch:
    
    def __init__(self, name):
        self.__name = name
        self.__nummern = []
                
    def printTelBuch(self):
        print ('Das Telefonbuch: '+self.__name)
        for p in self.__nummern:
            print(p)
    
    def insertPerson(self,p):
        if p not in self.__nummern:
            self.__nummern.append(p)
    
    def insertInformation(self, name, nummer):
        p = Person(name, nummer)
        if p not in self.__nummern:
            self.__nummern.append(p) 
            return p
        else:
            return None
        
    def getPerson(self,name):
        for p in self.__nummern:
            if p.getName()==name:
                return p
        return None
    
                




