from numpy import *
import operator
import logging

logger = logging.getLogger('tofile')

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis = 1)
    distances = sqDistance ** 0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteILabel = labels[sortedDistIndices[i]]
        classCount[voteILabel] = classCount.get(voteILabel,0)+1

    error = ''
    try:
        sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1),  reverse = True)
    except Exception as e:
        logger.error('Failed to sort', exc_info=True)

    return sortedClassCount[0][0]



    

