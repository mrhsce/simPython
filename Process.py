from Entity import Entity
from Event import Event


class Process(Entity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, customerDelayStatDis):
        super(Process, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name
        self.queue = 0
        self.customerDelayStatDis = customerDelayStatDis

    def takeCustomer(self):
        e = Event(self, self.releaseCustomer, 0,
                                        int(round(self.simSystem.getTime() + self.customerDelayStatDis.generate())))
        self.simSystem.addEvent(e)
        print "Process Entity: " + self.name + " has taken one Customer"

    def releaseCustomer(self):
        print "Process Entity: " + self.name + " has released one Customer"
        self.outputPointer[0].takeCustomer()

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)

    def setStatDis(self, customerDelayStatDis):
        self.customerDelayStatDis = customerDelayStatDis
