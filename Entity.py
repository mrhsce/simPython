from executive import SimSystem
from abc import ABCMeta, abstractmethod


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

    def __del__(self):
        Entity.idList.remove(self.id)


class Queue(Entity):

    def __init__(self, Type, id, delegator, inputId, outputId):
        super(Queue, self).__init__(Type, id, delegator, inputId, outputId)

        pass

    def do(self):
        pass

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
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


class Decide(Entity):

    def __init__(self, Type, id, delegator, inputId, outputId):
        super(Decide, self).__init__(Type, id, delegator, inputId, outputId)

        pass    

    def do(self):
        pass

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
        pass


class Create(Entity):

    def __init__(self, Type, id, delegator, inputId, outputId, name, create_type):
        super(Create, self).__init__(Type, id, delegator, inputId, outputId)
        self.name = name
        self.create_type = create_type

    def do(self):
        self.create_type.do()

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
        pass


class CreateType(object):
    __metaclass__ = ABCMeta

    def __init__(self, time_unit, first_creation, entity_per_arrival, max_arrival):
        self.time_unit = time_unit
        self.first_creation = first_creation
        self.entity_per_arrival = entity_per_arrival
        self.max_arrival = max_arrival

    @abstractmethod
    def do(self):
        print "Error: your child class must have start method!!"


class ConstantType(CreateType):

    def __init__(self, time_unit, first_creation, entity_per_arrival, max_arrival):
        super(ConstantType, self).__init__(time_unit, first_creation, entity_per_arrival, max_arrival)

    def do(self):
        pass


class RandomType(CreateType):

    def __init__(self, time_unit, first_creation, entity_per_arrival, max_arrival):
        super(RandomType, self).__init__(time_unit, first_creation, entity_per_arrival, max_arrival)

    def do(self):
        pass
    
r = RandomType("h", 0, 1, -1)
c = Create("Entity1", 0, 0, 0 , 0, "create1", r)
del c
