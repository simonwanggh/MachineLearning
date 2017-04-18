from numpy import *

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
    
