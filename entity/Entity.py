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





