import numpy as np
#when we user knn, some field with largest variant will effect the result greatly.
#so we should normalize it to 0~1
def autoNorm(dataSet): # dataSet 2-D array
    minVals = dataSet.min(0) # 0 - min value of columns
    maxVals = dataSet.max(0) # 0 - max value of columns
    ranges = maxVals - minVals
    normalDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normalDataSet = dataSet - np.tile(minVals, (m,1))
    normalDataSet = normalDataSet/np.tile(ranges, (m,1))
    return normalDataSet, ranges, minVals


def normalizeSample(sample, minVals, ranges):
    sampleDiff = sample - minVals
    return sampleDiff/ranges

from math import log
'''
2D array
the last column should be the label
sample,
[[1,1,'yes'],
 [1,1,'yes'],
 [1,0,'no' ],
 [0,1,'no' ]]
 the label index is -1 or 2

 the default label index is -1
'''
def calcShannonEntropy(dataSet,labelIndex = -1):
    numberEntities = len(dataSet)
    labelCount = {}
    for vert in dataSet:
        label = vert[labelIndex]
        if label not in labelCount.keys() :
            labelCount[label] = 1
        else:
            labelCount[label] += 1
    shannonEnt = 0.0
    for key in labelCount:
        prop = float(labelCount[key])/numberEntities
        shannonEnt -= prop * log(prop,2)
    return shannonEnt

'''
dataSet - 2D numpy array

'''
def splitDataSet(dataSet, splitColumnIndex, checkValue):
    retDataSet = []
    for sample in dataSet:
        if sample[splitColumnIndex] == checkValue:
            retDataSet.append(sample)
    return retDataSet

