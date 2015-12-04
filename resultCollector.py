""" Here result collector exists that collects all the data related to the simulation in the runtime and then prints
        it - also chart and graph drawing functionalities are here"""
from collections import Counter


class resultCollector(object):
    def __init__(self):
        self.dic = {}

    def init(self, entityId):
        self.dic[entityId] = []

    def setWaiteTime(self, entityId, waite):
        print entityId, waite
        self.dic[entityId].append(waite)

    def getWaiteForAnyCustomerData(self, entityId):
        xList = []
        yList = []
        origin = self.dic[entityId]
        for i in range(0, len(origin)):
            xList.append(str(i))
            yList.append(origin[i])

        return xList, yList

    def getFrequencyForAnyWaiteData(self, entityId):
        # returns [(waiteTime1, freq1) ,(waiteTime2, freq2) ,(waiteTime3, freq3) ,(waiteTime4, freq4)]
        # waiteTime1 < waiteTime2 < waiteTime3 < waiteTime4
        xList = []
        yList = []

        origin = sorted(Counter(self.dic[entityId]).items(), key=lambda tup: tup[0])
        for i in range(0, len(origin)):
            xList.append(str(origin[i][0]))
            yList.append(origin[i][1])

        return xList, yList
