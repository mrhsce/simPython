from SimSystem import SimSystem


class Entity(object):

    def __init__(self, kind):
        self.kind = kind
        pass

    def do(self):
        while SimSystem.is_sim_running():
            pass
