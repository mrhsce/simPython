from executive import SimSystem
from abc import ABCMeta, abstractmethod
from statisticalDistributions import *
from Process import *


class Entity(object):
    __metaclass__ = ABCMeta
    idList = []
    
    def __init__(self, Type, id, delegator, inputId, outputId):
        self.type = Type
        assert(id not in Entity.idList)
        self.id = id
        Entity.idList.append(id)   # Id should be unique so it is added to idList to hold it
        self.inputId = inputId
        self.outputId = outputId
        self.delegator = delegator
        self.scheduleList = []  # This list is for storing the list of works that this entity should do when it is run
        pass

    @abstractmethod
    def do(self):
        pass

    @abstractmethod
    def takeCustomer(self):
        pass

    @abstractmethod
    def releaseCustomer(self):
        pass

    @abstractmethod
    def conect(self, other):
        pass

    def __del__(self):
        Entity.idList.remove(self.id)


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


class Dispose(Entity):

    def __init__(self, Type, id, delegator, inputId, outputId, name, is_record):
        super(Dispose, self).__init__(Type, id, delegator, inputId, outputId)
        self.name = name
        self.is_record = is_record

    def do(self):
        while SimSystem.is_sim_running():
            pass

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
        pass

    def conect(self, other):
        pass


class Decide(Entity):

    def __init__(self, Type, id, delegator, inputId, outputId, name, expression):
        super(Decide, self).__init__(Type, id, delegator, inputId, outputId)
        self.name = name
        self.expression = expression

    def do(self):
        pass

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
        pass

    def calculate(self):
        return bool(eval(self.expression))

    def conect(self, other):

        # other is array [YesEntity , NoEntity]
        self.outputId.append(other[0].id)
        self.outputId.append(other[1].id)
        other.inputId.append(self.id)


class Create(Entity):

    def __init__(self, Type, id, delegator, inputId, outputId, name, createStatDis):
        super(Create, self).__init__(Type, id, delegator, inputId, outputId)
        self.name = name
        self.createStatDis = createStatDis

    def do(self):
        self.create_type.do()

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
        pass

    def conect(self, other):
        # other is a Create object
        self.outputId.append(other.id)
        other.inputId.append(self.id)

