from abc import ABCMeta, abstractmethod
from statisticalDistributions import *
import copy

class Entity(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, simSystem, Type, id, inputPointer, outputPointer):
        self.type = Type
        self.simSystem = simSystem
        self.id = id
        self.inputPointer = copy.deepcopy(inputPointer)
        self.outputPointer = copy.deepcopy(outputPointer)

    def getType(self):
        return self.type

    @abstractmethod
    def connect(self, other):
        pass





