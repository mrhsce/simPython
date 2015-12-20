from abc import ABCMeta, abstractmethod

from entity.Entity import Entity


class QueueEntity(Entity):
    __metaclass__ = ABCMeta

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name):
        super(QueueEntity, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name

    @abstractmethod
    def takeCustomer(self):
        pass

    @abstractmethod
    def releaseCustomer(self):
        pass
