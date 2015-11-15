from Singleton import *
import heapq


class Event(object):

    def __init__(self, entityPointer, funcName, params, execTime):
        self.entityPointer = entityPointer
        self.funcName = funcName
        self.params = params
        self.execTime = execTime


@Singleton
class EventList:
    def __init__(self):
        self.queue = PriorityQueue()


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
