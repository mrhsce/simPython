import thread
from clock import *
from duplicity.asyncscheduler import threading

thread1Interface = ClockInterface()
thread1 = thread.start_new_thread(clockGenarator, (threa1Interface, 100, runFunc))

while True:
    # print threa1Interface.time
    if threa1Interface.time == 10:
       threa1Interface.stop()

