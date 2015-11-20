""" Here result collector exists that collects all the data related to the simulation in the runtime and then prints
        it - also chart and graph drawing functionalities are here"""
from collections import Counter


class resultCollector(object):
    def __init__(self):
        self.dic = {}

    def setWaiteTime(self, entityId, waite):
        print entityId, waite
        if entityId not in self.dic:
            self.dic[entityId] = [waite]
        else:
            self.dic[entityId].append(waite)

    def getWaiteForAnyCustomerData(self, entityId):
        # return an array that index of array is customer number and value of array is waiting time of customer
        return self.dic[entityId]

    def getFrequencyForAnyWaiteData(self, entityId):
        # returns [(waiteTime1, freq1) ,(waiteTime2, freq2) ,(waiteTime3, freq3) ,(waiteTime4, freq4)]
        # waiteTime1 < waiteTime2 < waiteTime3 < waiteTime4
        return sorted(Counter(self.dic[entityId]).items(), key=lambda tup: tup[0])
