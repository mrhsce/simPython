
class SimSystem(object):
    running = False

    @staticmethod
    def strat_sim():
        SimSystem.running = True

    @staticmethod
    def stop_sim():
        SimSystem.running = False

    @staticmethod
    def is_sim_running():
        return SimSystem.running

