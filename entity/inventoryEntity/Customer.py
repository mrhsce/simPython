from InventoryEntity import InventoryEntity


class Customer(InventoryEntity):
    def __init__(self, simSystem, Type, id, inputPointer, outputPointer):
        super(Customer, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.orderStatDist = 0

    def takeOrder(self, amount):
        pass

    def giveOrder(self, amount):
        pass

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)

    def setStatDis(self, orderStatDist):
        self.orderStatDist = orderStatDist

