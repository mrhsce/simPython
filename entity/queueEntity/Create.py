from Event import Event
from entity.queueEntity.QueueEntity import QueueEntity


class Create(QueueEntity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, createStatDis):
        super(Create, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name
        self.createStatDis = createStatDis

        self.count = 0
        self.maxCount = -1

        print "Creator Entity: " + self.name + " has been initialized "

    def setMaxCount(self, i):
        self.maxCount = i

    def takeCustomer(self):
        pass

    def createCustomer(self):
        if self.maxCount == -1 or self.count < self.maxCount:
            print "Creator Entity: " + self.name + " has Created " + str(self.count + 1) + " customer(s)"
            e = Event(self, self.releaseCustomer, 0,
                          int(round(self.simSystem.getTime() + self.createStatDis.generate())))
            self.simSystem.addEvent(e)
            self.count += 1

    def releaseCustomer(self):
        print "Creator Entity: " + self.name + " has released one Customer"
        self.createCustomer()
        self.outputPointer[0].takeCustomer()

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)

    def setStatDis(self, createStatDis):
        self.createStatDis = createStatDis
