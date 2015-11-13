""" Here definitions and attributes of all statistical distributions that are used in the simulation are defined"""
from abc import ABCMeta, abstractmethod
import random


class StatDis(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def generate(self):
        pass


class UniformDis(StatDis):

    def __init__(self, minVal, maxVal):
        self.minVal = minVal
        self.maxVal = maxVal

    def generate(self):
        return random.uniform(self.minVal, self.maxVal)


class NormalDis(StatDis):

    def __init__(self, mean, std):
        pass

    def generate(self):
        pass
