from Entity import Entity
from Event import Event


class Process(Entity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, customerDelayStatDis):
        super(Process, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name
        self.queue = 0
        self.customerDelayStatDis = customerDelayStatDis
        self.simSystem.logger.init(self.id)

    def takeCustomer(self):
        delay = int(round(self.customerDelayStatDis.generate()))
        params={}
        params['waite'] = delay
        e = Event(self, self.releaseCustomer, params, self.simSystem.getTime() + delay)
        self.simSystem.addEvent(e)
        print "Process Entity: " + self.name + " has taken one Customer"

    def releaseCustomer(self, params):
        print "Process Entity: " + self.name + " has released one Customer"
        self.simSystem.logger.setWaiteTime(self.id, params['waite'])
        self.outputPointer[0].takeCustomer()

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)

    def setStatDis(self, customerDelayStatDis):
        self.customerDelayStatDis = customerDelayStatDis
