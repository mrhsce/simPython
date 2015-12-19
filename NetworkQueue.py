""" This is the main part of the engine that using all the other parts runs the simulation """
from SimSystem import *
from resultCollector import resultCollector

r = resultCollector()
s = SimSystem("sim1", "queue", r)

statDis = UniformDis(45, 45)
c = generateCreateEntity(s, "Create", 1, "Create", statDis)

decide = generateDecideEntity(s, "Decide", 5, "decide", "random.randint(0,100) < 60")


statDis = UniformDis(180, 180)
s1 = generateServiceCenterEntity(s, "ServiceCenter", 4, "ServiceCenter1", 3, statDis)

statDis = UniformDis(0, 0)
s2 = generateServiceCenterEntity(s, "ServiceCenter", 6, "ServiceCenter2", 1, statDis)

statDis = UniformDis(40, 40)
s3 = generateServiceCenterEntity(s, "ServiceCenter", 7, "ServiceCenter3", 1, statDis)

d = generateDisposeEntity(s, "Dispose", 3, "dispose", True)

c.connect(decide)
decide.connect([s1, s2])
s1.connect(d)
s2.connect(d)

s.addEntity(c)
s.addEntity(decide)
s.addEntity(s1)
s.addEntity(s2)
s.addEntity(s3)
s.addEntity(d)

s.run()
