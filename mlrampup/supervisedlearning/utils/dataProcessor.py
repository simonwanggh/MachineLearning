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



'''
dataSet - 2D numpy array

'''
def splitDataSet(dataSet, splitColumnIndex, checkValue):
    retDataSet = []
    for sample in dataSet:
        if sample[splitColumnIndex] == checkValue:
            retDataSet.append(sample)
    return retDataSet

import operator
def majorityCount(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys() : classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

