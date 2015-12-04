from InventoryEntity import InventoryEntity


class Customer(InventoryEntity):
    def __init__(self, simSystem, Type, id, inputPointer, outputPointer):
        super(Customer, self).__init__(simSystem, Type, id, inputPointer, outputPointer)

    def takeOrder(self, amount):
        pass

    def giveOrder(self, amount):
        pass

    def connect(self, other):
        pass
