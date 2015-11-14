""" Here definitions and attributes of all statistical distributions that are used in the simulation are defined"""
from abc import ABCMeta, abstractmethod
import random
import np


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
        self.mean = mean
        self.std = std

    def generate(self):
        return np.random.normal(self.mean, self.std, 1)[0]


class ConstantDis(StatDis):

    def __init__(self, val):
        self.val = val

    def generate(self):
        return self.val


class TriangularDis(StatDis):

    def __init__(self, low, high, mode):
        self.low = low
        self.high = high
        self.mode = mode

    def generate(self):
        return random.triangular(self.low, self.high, self.mode)
