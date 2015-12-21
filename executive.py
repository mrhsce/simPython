""" This is the main part of the engine that using all the other parts runs the simulation """
from SimSystem import *
from resultCollector import resultCollector

# Network queue part
#<<<<<<<<<<<<<<<<<<<<<<<<<
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
#>>>>>>>>>>>>>>>>>>>>>>>>


# Inventory system part
#<<<<<<<<<<<<<<<<<<<<<<<<
# r = resultCollector()
# s = SimSystem("sim1", "inventory", r)
# setSimSystem(s)
# mainStorage = generateStorageEntity(1, "Storage",20, 100,5 )
# mainStorage.setCentral(True)
# customer1 = generateCustomerEntity(2,"customer1")
# customer1.setStatDis(ConstantDis(2),ConstantDis(3))
#
# mainStorage.connect(customer1)
#
# s.addEntity(mainStorage)
# s.addEntity(customer1)
#>>>>>>>>>>>>>>>>>>>>>>>>

s.run()
