from Entity import Entity


class Decide(Entity):

    def __init__(self, simSystem, Type, id, inputPointer, outputPointer, name, expression):
        super(Decide, self).__init__(simSystem, Type, id, inputPointer, outputPointer)
        self.name = name
        self.expression = expression

    def takeCustomer(self):
        print "Entity :" + self.name + " takes one customer"
        self.releaseCustomer()

    def releaseCustomer(self):
        if self.calculate():
            self.outputPointer[0].takeCustomer()
            print "Entity :" + self.name + " release one customer in True flow"

        else:
            self.outputPointer[1].takeCustomer()
            print "Entity :" + self.name + " release one customer in False flow"

    def calculate(self):
        return bool(eval(self.expression))

    def connect(self, other):
        # other is array [YesEntity , NoEntity]
        self.outputPointer.append(other[0])
        self.outputPointer.append(other[1])
        other.inputPointer.append(self)
