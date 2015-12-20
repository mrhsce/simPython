""" This is the main part of the engine that using all the other parts runs the simulation """
from SimSystem import *
from resultCollector import resultCollector

r = resultCollector()
s = SimSystem("sim1", "queue", r)
setSimSystem(s)

statDis = UniformDis(45, 45)
c = generateCreateEntity(1, "create", statDis)
c.setMaxCount(10)
decide = generateDecideEntity(5, "decide", "random.randint(0,100) < 60")


statDis = UniformDis(180, 180)
s1 = generateServiceCenterEntity(4, "ServiceCenter1", 3, statDis)

statDis = UniformDis(0, 0)
s2 = generateServiceCenterEntity(6, "ServiceCenter2", 1, statDis)

statDis = UniformDis(40, 40)
s3 = generateServiceCenterEntity(7, "ServiceCenter3", 1, statDis)

d = generateDisposeEntity(12, "dispose", True)

c.connect(decide)
decide.connect([s1, s2])
s1.connect(s3)
s2.connect(s3)
s3.connect(d)


s.addEntity(c)
s.addEntity(decide)
s.addEntity(s1)
s.addEntity(s2)
s.addEntity(s3)
s.addEntity(d)

s.run()
