from Entity import Entity


class Process(Entity):

    def __init__(self, Type, id, delegator, inputId, outputId, name):
        super(Process, self).__init__(Type, id, delegator, inputId, outputId)
        self.name = name

    def do(self):
        pass

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
        pass

    def conect(self, other):
        # other is a Process object
        self.outputId.append(other.id)
        other.inputId.append(self.id)
