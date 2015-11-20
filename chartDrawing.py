import numpy as np
from matplotlib import pyplot as plt


def drawWaiteForAnyCustomer(xList, yList,name):
    fig = plt.figure()
    width = .5
    ind = np.arange(len(yList))
    plt.bar(ind, yList)
    plt.xticks(ind + width / 2, xList)
    # fig.autofmt_xdate()

    plt.savefig("results/"+name+"_waitingPerCustomer.pdf")


def drawFrequencyForAnyWaiteData(xList, yList, name):
    fig = plt.figure()
    width = .5
    ind = np.arange(len(yList))
    plt.bar(ind, yList)
    plt.xticks(ind + width / 2, xList)
    # fig.autofmt_xdate()

    plt.savefig("results/"+name+"_FrequencyPerWaitAmount.pdf")
