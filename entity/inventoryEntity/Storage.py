from Event import Event
from InventoryEntity import InventoryEntity


class Storage(InventoryEntity):
    def __init__(self, simSystem, Type, id, name, min, max, period, inputPointer, outputPointer):
        super(Storage, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name
        self.isCentral = False
        self.maxStorage = max   # The total capacity of the storage
        self.minStorage = min  # The threshold for new order
        self.refillPeriod = period  # The review for new order period

        self.storage = 0   # current storage

    def setCentral(self,isCentral):
        if(isCentral):
            self.isCentral = True
        else:
            self.isCentral = False

    def start(self):
        print self.name + " has been started"
        self.refillStorage()

        for i in self.outputPointer:
            i.start()

    def takeOrder(self, amount,pointer):
        print self.name + " is going to give an order"
        self.storage =- amount
        self.giveOrder(amount,pointer)

    def giveOrder(self, amount,pointer):
        print self.name + " has given an order"
        pointer.acceptOrder(amount)

    def acceptOrder(self, amount):
        print self.name + " has taken an order"
        self.storage += amount

    def connect(self, other):
        self.outputPointer.append(other) #TODO transform it to list
        other.inputPointer.append(self)  #TODO transform it to list

    def make_central(self):
        self.isCentral = True
        self.storage = self.maxStorage

    def calculateOrder(self):
        if(self.storage < self.minStorage):
            return self.maxStorage - self.storage
        else:
            return 0

    def refillStorage(self):

        e = Event(self, self.refillStorage,0,
                          int(round(self.simSystem.getTime() + self.refillPeriod)))
        self.simSystem.addEvent(e)

        amount = self.calculateOrder()
        if(amount > 0):
            if(not self.isCentral):
                self.inputPointer.takeOrder(amount,self)
            else:
                self.storage = self.maxStorage
            print self.name + " has been filled"

