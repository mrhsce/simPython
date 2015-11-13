"""Here a functionality is constructed that based on the speed defined by the user advances the time of the system and
    then notifies the executer"""
import time    

class ClockInterface:
    def __init__(self):
        self.time = 0 
        self.running = True 
    def increment(self):
        self.time += 1  
    def stop(self):
        self.running = False        

def runFunc(txt):
    print txt

def clockGenarator(interface,frequency,runFunc):
    runFunc(interface.time)
    time.sleep(1.0/frequency)    
    while(interface.running):
        interface.increment()
        runFunc(interface.time)
        time.sleep(1.0/frequency)  
         
        