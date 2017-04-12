from mlrampup.supervisedlearning.utils import dataProcessor as dp
'''
dataSet - 2D numpy array
featureIndex - a tuple contain indexes of features
labelIndex - index of label column
'''
def chooseBestFeatureToSplit(dataSet, featureIndexes , labelIndex = -1):
    baseEntropy = calcShannonEntropy(dataSet, labelIndex)
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
            newEntropy += prop * calcShannonEntropy(splitDataSet,labelIndex)
        infoGain = baseEntropy - newEntropy
        if(infoGain > baseInfoGain):
            baseInfoGain = infoGain
            bestFeteature = i
    return bestFeteature,baseInfoGain


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


def creatTree(dataSet, featIndexLabelDict,  labelIndex = -1):
    labels = featIndexLabelDict.copy()
    classList = [example[labelIndex] for example in dataSet]
    if classList.count(classList[0]) == len(classList) :#all are the same class
        return classList[0]
    if len(labels) == 0 :# all features are travsed
        return dp.majorityCount(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet,labels.keys(),labelIndex)[0]
    bestFeatLabel = labels[bestFeat]
    del labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
         myTree[bestFeatLabel][value] = creatTree(dp.splitDataSet(dataSet,bestFeat,value),labels,labelIndex)

    return myTree


def classify(item, labelDict, tree):
    itemList = list(item)
    for key in tree.keys():
        branch = tree[key]
        index = labelDict[key]
        if type(branch).__name__ != 'dict':
            return 'unknown'
        for field in branch.keys():
            fieldBranch = branch[field]
            if field == item[index]:
                if type(fieldBranch).__name__ == 'dict':
                    return classify(item, labelDict, fieldBranch)
                else:
                    return fieldBranch

    return 'unknown'

