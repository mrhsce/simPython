from Entity import Entity


class Dispose(Entity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, is_record):
        super(Dispose, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name
        self.count = 0
        self.is_record = is_record

    def takeCustomer(self):
        self.count += 1
        print "Entity :" + self.name + " takes one customer"

    def releaseCustomer(self):
        pass

    def connect(self, other):
        pass
