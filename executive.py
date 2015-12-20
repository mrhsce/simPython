""" This is the main part of the engine that using all the other parts runs the simulation """
from SimSystem import *
from resultCollector import resultCollector

r = resultCollector()
s = SimSystem("sim1", "queue", r)
setSimSystem(s)
c = generateCreateEntity(1, "Create")
queue = generateMyQueueEntity(10, "my_queue")
p1 = generateProcessEntity(4, "proc1")
d = generateDisposeEntity(3, "dispose", True)
c.setMaxCount(10)

c.connect(queue)
queue.connect([p1])
p1.connect(d)

s.addEntity(c)
s.addEntity(queue)
s.addEntity(p1)
s.addEntity(d)

# r = resultCollector()
# s = SimSystem("sim1", "queue", r)
# mainStorage = generateStorageEntity(s, "Storage", 1, "mainStorage", 20, 100, )

s.run()
