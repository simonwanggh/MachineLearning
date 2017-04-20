from numpy import *
from itertools import *
from functools import *
import logging

logger = logging.getLogger('tofile')

'''
    trainMatrix - matrix of document : [['1', '2' ......],
                                        ['3', '0'.......],
                                             .........
                                       ]
                 each line corresponds to a document, the number is times the corresponding word found
    trainCategory - list of marked document  : ['atype', 'atype', 'btype', 'ctype' ]
'''
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    typeSet = set(trainCategory)
    pTypesDict = {i:(trainCategory.count(i)/float(numTrainDocs)) for i in typeSet}

    docZiped = zip(trainCategory,trainMatrix)
    docZipSorted = sorted(docZiped, key = lambda doc:doc[0])



    pFactors = {} #{'atype': (matrix([[2, 3]]), 5), 'btype': (matrix([[3, 3]]), 6)}
    for k, g in groupby(docZipSorted, lambda doc:doc[0]):
        reduceInit = (matrix(ones(numWords)),numWords)
        pFactors[k] = reduce(lambda x,y:(x[0]+ matrix(y[1]), x[1] + sum(y[1])), g, reduceInit)

    mapRespProp = map(lambda item:{item:pFactors[item][0]/pFactors[item][1]}, pFactors)
    def listToDict(x, y):
        x.update(y)
        return x
    mapRespPropDict = reduce(listToDict,mapRespProp,{}) #{'atype': matrix([[ 0.4,  0.6]]), 'btype': matrix([[ 0.5,  0.5]])}

    return mapRespPropDict, pTypesDict

'''
    dataSet - [['1', '2' ......],
                ['3', '0'.......],
                    .........
            ]
'''
def createVocabList(dataSet):
    vocabSet = set([])
    for doc in dataSet:
        vocabSet = vocabSet | set(doc)
    return list(vocabSet)

'''
    for one document
'''
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            logger("the word: s% is not in my Vocalulary!" % word)
    return returnVec
'''
    for document matrix
'''
def setOfWords2Matrix(vocabList, inputDocs):
    return [setOfWords2Vec(vocabList, doc) for doc in inputDocs]

'''
    vecBeClassified - a vector identified by vocabulary - [1,0,1,1.........]
    wordPropDict - trained module {'bad': matrix([[ 0.01960784,  0.05882353,  0.03921569,  0.01960784,  0.01960784,
          0.03921569,  0.01960784,  0.01960784,  0.03921569,  0.01960784,
          0.01960784,  0.01960784,  0.01960784,  0.01960784,  0.03921569,
          0.01960784,  0.01960784,  0.01960784,  0.01960784,  0.03921569,
          0.01960784,  0.01960784,  0.03921569,  0.03921569,  0.03921569,
          0.05882353,  0.01960784,  0.03921569,  0.03921569,  0.03921569,
          0.07843137,  0.03921569]]), 'good': matrix([[ 0.03571429,  0.01785714,  0.01785714,  0.03571429,  0.03571429,
          0.01785714,  0.03571429,  0.03571429,  0.01785714,  0.03571429,
          0.03571429,  0.03571429,  0.03571429,  0.03571429,  0.01785714,
          0.03571429,  0.03571429,  0.03571429,  0.03571429,  0.03571429,
          0.03571429,  0.07142857,  0.01785714,  0.05357143,  0.01785714,
          0.03571429,  0.03571429,  0.01785714,  0.03571429,  0.01785714,
          0.01785714,  0.01785714]])}
    classPropDict - trained module {'good': 0.5, 'bad': 0.5}
'''
def classify(vecBeClassified, wordPropDict, classPropDict):
    propList = [(item, sum(array(vecBeClassified)*array(wordPropDict[item][0])) + log(classPropDict[item])) for item in classPropDict.keys()]
    return max(propList, key = lambda i:i[1])[0]

