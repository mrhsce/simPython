
class Event(object):

    def __init__(self, entityPointer, funcName, params, execTime):
        self.entityPointer = entityPointer
        self.funcName = funcName
        self.params = params
        self.execTime = execTime
