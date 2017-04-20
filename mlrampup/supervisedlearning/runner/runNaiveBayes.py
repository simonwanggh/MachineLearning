from mlrampup.supervisedlearning.utils.postSample import *
from mlrampup.supervisedlearning.classifier.NaiveBayers import *

import logging

logger = logging.getLogger('tofile')

def main():
    listPosts, listClass = loadPostSample()
    vocabList = createVocabList(listPosts)
    trainMatrix = setOfWords2Matrix(vocabList, listPosts)
    mapRespPropDict, pTypesDict = trainNB0(trainMatrix,listClass)
    logger.info(mapRespPropDict)
    logger.info(pTypesDict)

    goodDoc = ['love','my','dalmation']
    badDoc = ['stupid', 'garbage']

    goodDocVec = setOfWords2Vec(vocabList,goodDoc)
    badDocVec = setOfWords2Vec(vocabList,badDoc)

    logger.info("Good Document : " + classify(goodDocVec,mapRespPropDict,pTypesDict) )
    logger.info("Bad Document : " + classify(badDocVec, mapRespPropDict, pTypesDict))

if __name__ == "__main__":
    main()