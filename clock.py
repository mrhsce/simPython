"""Here a functionality is constructed that based on the speed defined by the user advances the time of the system and
    then notifies the executer"""
import time    


class ClockInterface:
    def __init__(self):
        self.time = 0 
        self.running = True
    
    def setMaxClock(self, maximum):
        self.maxClock = maximum    
    
    def increment(self):
        self.time += 1

    def reachedMax(self):
        if(self.time >= self.maxClock):
            return True
        else:
            return False        



def clockGenarator(runFunc, frequency=1, interface=ClockInterface()):
    runFunc()
    time.sleep(1.0/frequency)    
    while not interface.reachedMax():
        interface.increment()
        runFunc()
        time.sleep(1.0/frequency)  
