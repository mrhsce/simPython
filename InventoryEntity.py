from abc import ABCMeta, abstractmethod
from statisticalDistributions import *
from Entity import Entity


class InventoryEntity(Entity):
    __metaclass__ = ABCMeta
    
    def __init__(self, simSystem, Type, id, inputPointer, outputPointer):
        super(InventoryEntity, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
    
    
    @abstractmethod
    def takeOrder(self,amount):
        pass
    
    @abstractmethod
    def giveOrder(self,amount):
        pass
            