from Event import Event
from entity.queueEntity.QueueEntity import QueueEntity
from MyQueue import MyQueue
from Process import Process
from Dispose import Dispose


class ServiceCenter(QueueEntity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, numberOfCore, StatDisCores):
        super(ServiceCenter, self).__init__(simSystem, Type, id, inputPointer, outputPointer, name)
        self.simSystem.logger.init(self.id)
        self.numberOfCore = numberOfCore
        self.processList = []
        self.queue = MyQueue(simSystem, "MyQueue", id*100, [], [], name + "_Queue")
        self.dispose = Dispose(simSystem, "Dispose", id * 1000, [], [], name + "DisPose", True)
        self.dispose.setBox(self)
        for i in range(0, numberOfCore):
            temp = Process(simSystem, "Process", id*100 + (i+1), [], [], name + "Core" + str(i+1), StatDisCores)
            self.processList.append(temp)
            temp.connect(self.dispose)
            self.simSystem.addEntity(temp)
        self.queue.connect(self.processList)

        self.inn = 0
        self.outt = 0


    def takeCustomer(self):
        print "ServiceCenter Entity: " + self.name + " takes one Customer"
        self.inn += 1
        self.queue.takeCustomer()

    def releaseCustomer(self, params):
        print "ServiceCenter Entity: " + self.name + " releaseCustomer one Customer"
        self.outt += 1
        self.outputPointer[0].takeCustomer()

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)
