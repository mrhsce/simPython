from Entity import *


def generateCreateEntity(entityType, entityID, delegator, inputId, outputId, name, statDis):
    c = Create(entityType, entityID, delegator, inputId, outputId, name, statDis)
    return c


def generateDecideEntity(entityType, entityID, delegator, inputId, outputId, name):
    d = Decide(entityType, entityID, delegator, inputId, outputId, name)
    return d


def generateDisposeEntity(entityType, entityID, delegator, inputId, outputId, name, isRecord):
    d = Dispose(entityType, entityID, delegator, inputId, outputId, name, isRecord)
    return d


# def generateQueueEntity(entityType, entityID, delegator, inputId, outputId, name):
#    q = Queue(entityType, entityID, delegator, inputId, outputId, name)
#    return q


def generateProcessEntity(entityType, entityID, delegator, inputId, outputId, name):
    p = Process(entityType, entityID, delegator, inputId, outputId, name)
    return p
