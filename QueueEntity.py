from abc import ABCMeta, abstractmethod
from Entity import Entity


class QueueEntity(Entity):
    __metaclass__ = ABCMeta
    
    def __init__(self, simSystem, Type, id, inputPointer, outputPointer):
        super(QueueEntity, self).__init__(simSystem, Type, id, inputPointer, outputPointer)

    @abstractmethod
    def takeCustomer(self):
        pass

    @abstractmethod
    def releaseCustomer(self):
        pass
