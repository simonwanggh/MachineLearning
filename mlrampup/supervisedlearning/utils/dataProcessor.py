import numpy as np
#when we user knn, some field with largest variant will effect the result greatly.
#so we should normalize it to 0~1
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normalDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normalDataSet = dataSet - np.tile(minVals, (m,1))
    normalDataSet = normalDataSet/np.tile(ranges, (m,1))
    return normalDataSet, ranges, minVals


def normalizeSample(sample, minVals, ranges):
    sampleDiff = sample - minVals
    return sampleDiff/ranges
