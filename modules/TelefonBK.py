# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:34:48 2017

@author: class
"""


class Person():
    
    def __init__(self, name, telNr):
        self.name=name
        self.telNr = str(telNr)
    
    def getName(self):
        return self.name
        
    def getTelefonNr(self):
        return self.telNr
    
    def setTelefonNr(self, newNumber):
        self.telNr = str(newNumber)
                
    def __eq__(self, other):
        if type(other)!=Person:
            return False
        if self.name==other.name:
            return True
        else:
            return False
        
    def __str__(self):
        return self.name + ' hat die Nummer: ' + self.telNr
            

class Telefonbuch():
    
    def __init__(self, name):
        self.name = name
        self.nummern = []
                
    def printTelBuch(self):
        print ('Das Telefonbuch: '+self.name)
        for p in self.nummern:
            print(p)
    
    def insertPerson(self,p):
        if p not in self.nummern:
            self.nummern.append(p)
    
    def insertInformation(self, name, nummer):
        p = Person(name, nummer)
        if p not in self.nummern:
            self.nummern.append(p) 
            return p
        else:
            return None
        
    def getPerson(self,name):
        for p in self.nummern:
            if p.getName()==name:
                return p
        return None
    
                




