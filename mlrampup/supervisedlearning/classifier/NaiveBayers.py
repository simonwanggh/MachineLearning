from numpy import *
from itertools import *
from functools import *

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


    pFactors = {}
    for k, g in groupby(docZipSorted, lambda doc:doc[0]):
        pFactors[k] = reduce(lambda x,y:(x[1]+y[1], sum(x[1],y[1])), g)
