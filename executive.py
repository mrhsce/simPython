""" This is the main part of the engine that using all the other parts runs the simulation """
from clock import *
import Singleton

@Singleton
class SimSystem(object):
    
    def __init__(self, simName,statisticsCollector=0):        
        self.entityList = []
        self.simName = simName
        self.time = 0
        self.logger = statisticsCollector
        
    def add(self, entity):
        self.entityList.append(entity)
        
    def run(self):
        for i in self.entityList:
            if(i.getType() == "Dispose"):
                
                
   
    
        

    

