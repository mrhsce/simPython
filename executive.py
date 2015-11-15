""" This is the main part of the engine that using all the other parts runs the simulation """

from SimSystem import *


s = SimSystem("sim1")
c = generateCreateEntity(s, "Create", 1, "Cr1")
p = generateProcessEntity(s, "Process", 2, "p")
d = generateDisposeEntity(s, "Dispose", 3, "d", True)
c.connect(p)
p.connect(d)

s.addEntity(c)
s.addEntity(p)
s.addEntity(d)

s.run()


