from Decide import Decide
from Process import Process
from queueEntity.Dispose import Dispose

from PriorityQueue import PriorityQueue
from chartDrawing import *
from entity.queueEntity.Create import Create
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
        print "The simulation has started"
        for i in self.entityList:
            if i.getType() == "Create":
                i.createCustomer()

        while self.eventList.isEmpty() != True:
            nextEvent = self.eventList.pop()
            self.time = nextEvent.execTime
            if nextEvent.params == 0:
                nextEvent.funcName()   # If does not execute use the object name before
            else:
                nextEvent.funcName(nextEvent.params)

        # Here all the data should be colected for later printing
        for i in self.entityList:
            if i.getType() == "Process":
                tmp = self.logger.getWaiteForAnyCustomerData(i.id)
                drawWaiteForAnyCustomer(tmp[0], tmp[1],i.name)

                tmp2 = self.logger.getFrequencyForAnyWaiteData(i.id)
                drawFrequencyForAnyWaiteData(tmp2[0], tmp2[1],i.name)


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
