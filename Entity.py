from abc import ABCMeta, abstractmethod
from statisticalDistributions import *


class Entity(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, simSystem, Type, id, inputPointer, outputPointer):
        self.type = Type
        self.simSystem = simSystem
        self.id = id
        self.inputPointer = inputPointer
        self.outputPointer = outputPointer        

    def getType(self):
        return self.type

    @abstractmethod
    def connect(self, other):
        pass


"""
class Queue(Entity):

    def __init__(self, Type, id, delegator, inputId, outputId, name):
        super(Queue, self).__init__(Type, id, delegator, inputId, outputId)
        self.name = name

    def do(self):
        pass

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
        pass

    def conect(self, other):
        pass
"""








