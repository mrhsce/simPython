from Entity import Entity
from abc import ABCMeta, abstractmethod


class Create(Entity):

    def __init__(self, entity_type, name, create_type):
        super(Create, self).__init__(entity_type)
        self.name = name
        self.create_type = create_type

    def do(self):
        self.create_type.do()


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
c = Create("Entity1", "create1", r)
