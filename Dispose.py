from Entity import Entity
from SimSystem import SimSystem


class Dispose(Entity):

    def __init__(self, kind, name, is_record):
        super(Dispose, self).__init__(kind)
        self.name = name
        self.is_record = is_record

    def do(self):
        while SimSystem.is_sim_running():
            pass

