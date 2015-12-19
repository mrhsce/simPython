from Event import Event
from entity.queueEntity.QueueEntity import QueueEntity


class ServiceCenter(QueueEntity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, numberOfCore, customerDelayStatDis):
        super(ServiceCenter, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.simSystem.logger.init(self.id)
        self.numberOfCore = numberOfCore
        self.customerDelayStatDis = customerDelayStatDis
        self.name = name

    def takeCustomer(self):
        delay = int(round(self.customerDelayStatDis.generate()))
        params={}
        params['waite'] = delay
        e = Event(self, self.releaseCustomer, params, self.simSystem.getTime() + delay)
        self.simSystem.addEvent(e)
        print "ServiceCenter Entity: " + self.name + " has taken one Customer"

    def releaseCustomer(self, params):
        print "ServiceCenter Entity: " + self.name + " has released one Customer"
        self.simSystem.logger.setWaiteTime(self.id, params['waite'])
        self.outputPointer[0].takeCustomer()

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)

    def setStatDis(self, customerDelayStatDis):
        self.customerDelayStatDis = customerDelayStatDis
