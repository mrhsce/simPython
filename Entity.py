from executive import SimSystem
from abc import ABCMeta, abstractmethod
from statisticalDistributions import *
from Process import *
from Event import *


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


class Dispose(Entity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, is_record):
        super(Dispose, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name
        self.is_record = is_record

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
        pass

    def connect(self, other):
        pass


class Decide(Entity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, expression):
        super(Decide, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name
        self.expression = expression

    def takeCustomer(self):
        self.releaseCustomer()

    def releaseCustomer(self):
        if self.calculate():
            self.outputPointer[0].takeCustomer()
        else:
            self.outputPointer[1].takeCustomer()

    def calculate(self):
        return bool(eval(self.expression))

    def connect(self, other):
        # other is array [YesEntity , NoEntity]
        self.outputPointer.append(other[0])
        self.outputPointer.append(other[1])
        other.inputPointer.append(self)


class Create(Entity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, createStatDis):
        super(Create, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name

        if createStatDis == 0:
            self.createStatDis = UniformDis(1, 10)
        else:
            self.createStatDis = createStatDis

        self.count = 0
        self.maxCount = -1

    def seMaxCount(self, i):
        self.maxCount = i

    def takeCustomer(self):
        pass

    def createCustomer(self):
        if self.maxCount == -1 or self.count < self.maxCount:
            e = Event(self, self.createCustomer, 0,
                          int(round(self.simSystem.getTime() + self.createStatDis.generate())))
            self.simSystem.addEvent(e)
            self.count += 1

    def releaseCustomer(self):
        self.createCustomer()
        self.outputPointer[0].takeCustomer()

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)

    def setStatDis(self, createStatDis):
        self.createStatDis = createStatDis
