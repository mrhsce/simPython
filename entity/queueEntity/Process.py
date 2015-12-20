from Event import Event
from entity.queueEntity.QueueEntity import QueueEntity


class Process(QueueEntity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, customerDelayStatDis):
        super(Process, self).__init__(simSystem, Type, id, inputPointer, outputPointer, name)
        self.customerDelayStatDis = customerDelayStatDis
        self.simSystem.logger.init(self.id)
        self.busy = False

    def takeCustomer(self):
        self.busy = True
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
        self.busy = False
        self.requestCustomer()

    def requestCustomer(self):
        if self.busy == False:
            print "Process Entity: " + self.name + " requestCustomer one Customer"
            self.inputPointer[0].releaseCustomerByDes(self)

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)

    def setStatDis(self, customerDelayStatDis):
        self.customerDelayStatDis = customerDelayStatDis
