from Entity import *


def generateCreateEntity(entityType, entityID, name, statDis=0, inputPointer=0, outputPointer=0):
    c = Create(entityType, entityID, inputPointer, outputPointer, name, statDis)
    return c


def generateDecideEntity(entityType, entityID, name, inputPointer=0, outputPointer=0):
    d = Decide(entityType, entityID, inputPointer, outputPointer, name)
    return d


def generateDisposeEntity(entityType, entityID, name, isRecord, inputPointer=0, outputPointer=0):
    d = Dispose(entityType, entityID, inputPointer, outputPointer, name, isRecord)
    return d


# def generateQueueEntity(entityType, entityID, name, inputPointer=0, outputPointer=0):
#    q = Queue(entityType, entityID, inputPointer, outputPointer, name)
#    return q


def generateProcessEntity(entityType, entityID, name, customerStatDis=0, inputPointer=0, outputPointer=0):
    p = Process(entityType, entityID, inputPointer, outputPointer, name, customerStatDis)
    return p
