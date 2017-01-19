from mlrampup.supervisedlearning.utils import dataProcessor as dp
'''
dataSet - 2D numpy array
featureIndex - a tuple contain indexes of features
labelIndex - index of label column
'''
def chooseBestFeatureToSplit(dataSet, featureIndexes , labelIndex = -1):
    baseEntropy = dp.calcShannonEntropy(dataSet, labelIndex)
    bestFeteature = -1
    dataSetSize = len(dataSet)
    baseInfoGain = 0.0
    for i in featureIndexes:
        featValueList = [example[i] for example in dataSet]
        uniqueValue = set(featValueList)
        newEntropy = 0.0
        for value in uniqueValue:
            splitDataSet = dp.splitDataSet(dataSet,i,value)
            prop = len(splitDataSet)/float(dataSetSize)
            newEntropy += prop * dp.calcShannonEntropy(splitDataSet,labelIndex)
        infoGain = baseEntropy - newEntropy
        if(infoGain > baseInfoGain):
            baseInfoGain = infoGain
            bestFeteature = i
    return bestFeteature,baseInfoGain