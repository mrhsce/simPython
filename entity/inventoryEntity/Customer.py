from Event import Event
from InventoryEntity import InventoryEntity


class Customer(InventoryEntity):
    def __init__(self, simSystem, Type, id, name, inputPointer, outputPointer):
        super(Customer, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name
        self.orderAmountStatDist = 0
        self.orderFreqStatDist = 0

    def start(self):
        print self.name + " has been started"
        e = Event(self, self.giveOrder,int(round(self.orderAmountStatDist.generate())),
                          int(round(self.simSystem.getTime() + self.orderFreqStatDist.generate())))
        self.simSystem.addEvent(e)

    def acceptOrder(self, amount):
        print self.name + " order containing "+str(amount)+" items has been recieved"

    def giveOrder(self, amount):
        self.inputPointer[0].takeOrder(amount,self)
        e = Event(self, self.giveOrder,int(round(self.orderAmountStatDist.generate())),
                          int(round(self.simSystem.getTime() + self.orderFreqStatDist.generate())))
        self.simSystem.addEvent(e)

    def connect(self, other):
       self.outputPointer.append(other)
       print "reached here"
       other.inputPointer.append(self)

    def setStatDis(self, orderAmountStatDist,orderFreqStatDist):
        self.orderAmountStatDist = orderAmountStatDist
        self.orderFreqStatDist = orderFreqStatDist

    def takeOrder(self, amount,pointer):
        pass



