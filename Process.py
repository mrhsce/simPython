from Entity import Entity
from statisticalDistributions import *


class Process(Entity):

    def __init__(self, Type, id, inputPointer, outputPointer, name, customerDelayStatDis):
        super(Process, self).__init__(Type, id, inputPointer, outputPointer)
        self.name = name
        self.queue = 0
        if customerDelayStatDis == 0:
            self.customerDelayStatDis = UniformDis(1, 10)
        else:
            self.customerDelayStatDis = customerDelayStatDis

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
        pass

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)

    def setStatDis(self, customerDelayStatDis):
        self.customerDelayStatDis = customerDelayStatDis
