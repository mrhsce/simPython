from abc import ABCMeta, abstractmethod
from statisticalDistributions import *


class Entity(object):
    __metaclass__ = ABCMeta
    # idList = []
    
    def __init__(self, simSystem, Type, id, inputPointer, outputPointer):
        self.type = Type
        self.simSystem = simSystem
        # assert(id not in Entity.idList)
        self.id = id
        # Entity.idList.append(id)   # Id should be unique so it is added to idList to hold it
        self.inputPointer = inputPointer
        self.outputPointer = outputPointer        

    @abstractmethod
    def takeCustomer(self):
        pass

    def getType(self):
        return self.type

    @abstractmethod
    def releaseCustomer(self):
        pass

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








