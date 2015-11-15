""" This is the main part of the engine that using all the other parts runs the simulation """
from clock import *
import Singleton
from Event import *


@Singleton
class SimSystem(object):
    
    def __init__(self, simName,statisticsCollector=0):        
        self.entityList = []
        self.eventList = EventList()
        self.simName = simName
        self.time = 0
        self.logger = statisticsCollector
        
    def addEntity(self, entity):
        self.entityList.append(entity)        
    
    def addEvent(self, event):
        self.eventList.push(event, event.execTime)    
    
    def getTime(self):
        return self.time
    
    def run(self):
        for i in self.entityList:
            if(i.getType() == "Dispose"):
                i.createCustomer()
        print "The simulation has started"
        
        while(len(self.entityList) > 0):
            nextEvent = self.eventList.pop()
            self.time = nextEvent.execTime
            if(nextEvent.params == 0):
                nextEvent.funcName()   # If does not execute use the object name before
            else:
                nextEvent.funcName()    
            
        # Here all the datas should be colected for later printing
        print "Execution has been finished"        
   
    
        

    

