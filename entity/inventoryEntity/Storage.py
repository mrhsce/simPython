from InventoryEntity import InventoryEntity


class Storage(InventoryEntity):
    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, min, max, period):
        super(Storage, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.isCentral = False
        self.maxStorage = max   # The total capacity of the storage
        self.minStorage = min  # The threshold for new order
        self.refillPeriod = period  # The review for new order period

        self.storage = 0   # current storage

    def takeOrder(self, amount,pointer):
        pass

    def giveOrder(self, amount,pointer):
        pass

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)

    def make_central(self):
        self.isCentral = True
        self.storage = self.maxStorage

    def calculateOrder(self):
        if(self.storage < self.minStorage):
            return self.maxStorage - self.storage
        else:
            return 0