""" This is the main part of the engine that using all the other parts runs the simulation """
from clock import *

class SimSystem(object):
    
    def __init__(self, statisticsCollector):        
        self.entityList = []
        self.isRunning = False
        self.time = 0
        self.logger = statisticsCollector
   
    def setupEntityList(self):
        pass
        
    def advanceOneClock(self):
        pass
    
    def runTerminatedByClock(self,clockNum):
        clockInterface = ClockInterface()
        clockInterface.setMaxClock(clockNum)
        clockGenarator(self.advanceOneClock,1,0)
    
    def runTerminatedByCount(self):
        pass
        

    

