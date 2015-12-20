from QueueEntity import QueueEntity
import Queue


class MyQueue(QueueEntity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name):
        super(MyQueue, self).__init__(simSystem, Type, id, inputPointer, outputPointer, name)
        self.queue = Queue.Queue()

    def takeCustomer(self):
        self.queue.put(self.simSystem.getTime())
        for i in range(0,  len(self.outputPointer)):
            self.outputPointer[i].requestCustomer()

    def releaseCustomer(self):
        pass

    def releaseCustomerByDes(self, entityPtr):
        if not self.queue.empty():
            item = self.queue.get()
            entityPtr.takeCustomer()

    def connect(self, other):
        for i in range(0, len(other)):
            self.outputPointer.append(other[i])
            other[i].inputPointer.append(self)