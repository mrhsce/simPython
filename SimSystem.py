from Process import Process
from Create import Create
from Dispose import Dispose
from Decide import Decide
from PriorityQueue import PriorityQueue
from statisticalDistributions import *


class SimSystem:

    def __init__(self, simName, statisticsCollector=0):
        self.entityList = []
        self.eventList = PriorityQueue()
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
            if i.getType() == "Create":
                i.createCustomer()
        print "The simulation has started"

        while self.eventList.len() > 0:
            nextEvent = self.eventList.pop()
            self.time = nextEvent.execTime
            if nextEvent.params == 0:
                nextEvent.funcName()   # If does not execute use the object name before
            else:
                nextEvent.funcName()

        # Here all the data should be colected for later printing
        print "Execution has been finished"


def generateCreateEntity(simSystem, entityType, entityID, name, statDis=UniformDis(1, 10), inputPointer=[], outputPointer=[]):
    c = Create(simSystem, entityType, entityID, inputPointer, outputPointer, name, statDis)
    return c


def generateDecideEntity(simSystem, entityType, entityID, name, expression, inputPointer=[], outputPointer=[]):
    d = Decide(simSystem, entityType, entityID, inputPointer, outputPointer, name, expression)
    return d


def generateDisposeEntity(simSystem, entityType, entityID, name, isRecord, inputPointer=[], outputPointer=[]):
    d = Dispose(simSystem, entityType, entityID, inputPointer, outputPointer, name, isRecord)
    return d


# def generateQueueEntity(simSystem, entityType, entityID, name, inputPointer=0, outputPointer=0):
#    q = Queue(simSystem, entityType, entityID, inputPointer, outputPointer, name)
#    return q


def generateProcessEntity(simSystem, entityType, entityID, name, customerStatDis=UniformDis(1, 10), inputPointer=[], outputPointer=[]):
    p = Process(simSystem, entityType, entityID, inputPointer, outputPointer, name, customerStatDis)
    return p
