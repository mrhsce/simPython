from entity.queueEntity.QueueEntity import QueueEntity


class Dispose(QueueEntity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, is_record):
        super(Dispose, self).__init__(simSystem, Type, id, inputPointer, outputPointer, name)
        self.count = 0
        self.is_record = is_record
        self.box = None

    def takeCustomer(self):
        self.count += 1
        print "Dispose Entity: " + self.name + " takes one customer"
        self.releaseCustomer()

    def releaseCustomer(self):
        params={}
        params['waite'] = 0
        if len(self.outputPointer) != 0:
            self.outputPointer[0].takeCustomer()
        elif self.box != None:
            self.box.releaseCustomer(params)

    def connect(self, other):
        self.outputPointer.append(other)
        other.inputPointer.append(self)

    def setBox(self, box):
        self.box = box
