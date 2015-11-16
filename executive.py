""" This is the main part of the engine that using all the other parts runs the simulation """

from SimSystem import *


s = SimSystem("sim1")
c = generateCreateEntity(s, "Create", 1, "Create")
p = generateProcessEntity(s, "Process", 2, "proc")
d = generateDisposeEntity(s, "Dispose", 3, "dispose", True)
c.setMaxCount(100)
c.connect(p)
p.connect(d)

s.addEntity(c)
s.addEntity(p)
s.addEntity(d)

s.run()


