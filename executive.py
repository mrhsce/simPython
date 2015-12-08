""" This is the main part of the engine that using all the other parts runs the simulation """
from SimSystem import *
from resultCollector import resultCollector

r = resultCollector()
s = SimSystem("sim1", "queue", r)
c = generateCreateEntity(s, "Create", 1, "Create")
decide = generateDecideEntity(s, "Decide", 5, "decide", "2*(5-1) != 8")
p1 = generateProcessEntity(s, "Process", 4, "proc1")
p2 = generateProcessEntity(s, "Process", 2, "proc2")
d = generateDisposeEntity(s, "Dispose", 3, "dispose", True)
c.setMaxCount(100)

c.connect(decide)
decide.connect([p1, p2])
p1.connect(d)
p2.connect(d)

s.addEntity(c)
s.addEntity(decide)
s.addEntity(p1)
s.addEntity(p2)
s.addEntity(d)

r = resultCollector()
s = SimSystem("sim1", "queue", r)
mainStorage = generateStorageEntity(s, "Storage", 1, "mainStorage", 20, 100, )

s.run()
