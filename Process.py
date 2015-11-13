from Entity import Entity


class Process(Entity):

    def __init__(self, kind):
        super(Process, self).__init__(kind)

    def do(self):
        pass

    def takeCustomer(self):
        pass

    def releaseCustomer(self):
        pass
