""" Here all the entity classes, their attributes and the relationship between them is defined""" 


class Entity(object):
    def __init__(self, kind):
        self.kind = kind
        pass


class Create(Entity):
    def __init__(self, name, entity_type):
        super(Create, self).__init__(entity_type)
        self.name = name

    def print_it(self):
        print self.kind


class Dispose:
    def __init__(self):
        pass


class Process:
    def __init__(self):
        pass


class Decide:
    def __init__(self):
        pass


class Queue:
    def __init__(self):
        pass


class Customer:
    def __init__(self):
        pass


a = Create("create1", "Entity1")
a.print_it()


