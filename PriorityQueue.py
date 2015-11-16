import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    
    def isEmpty(self):
        if((self._index)>0):
            return False
        else:
            return True
    
    def pop(self):
        self._index-=1        
        return heapq.heappop(self._queue)[-1]

    def len(self):
        return self._index
