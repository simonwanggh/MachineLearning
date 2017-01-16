from mlrampup.supervisedlearning.utils import fileProcessor as fp
from mlrampup.supervisedlearning.utils import dataProcessor as dp
from mlrampup.supervisedlearning.classifier import knn
import logging

logger = logging.getLogger('tofile')

def main():
    matTest, classLabelVectorTest = fp.file2matrix("C:\PythonProject\mlrampup\externalfiles\datingTestSetTest.txt",
                                                       '\t', [0, 1, 2], 3)

    matReturn, classLabelVectorReturn = fp.file2matrix("C:\PythonProject\mlrampup\externalfiles\datingTestSet.txt",
                                                       '\t', [0, 1, 2], 3)

    normalDataSet, ranges, minVals = dp.autoNorm(matReturn)

    testDataSize = len(matTest)
    #no normalized
    rightCountNoNormalized = 0;
    rightCountNormalized = 0;
    for i in range(testDataSize):
        #no normalized
        label = knn.classify0(matTest[i,:],matReturn,classLabelVectorReturn, 3)
        if label == classLabelVectorTest[i] : rightCountNoNormalized = rightCountNoNormalized + 1
        #normalized
        labelNorm = knn.classify0(dp.normalizeSample(matTest[i,:],minVals,ranges), normalDataSet,classLabelVectorReturn, 3)
        if labelNorm == classLabelVectorTest[i] : rightCountNormalized = rightCountNormalized + 1
    logging.info("No normalized , Accuracy : %f%%", float(rightCountNoNormalized)/float(testDataSize)*100)
    logging.info("Normalized , Accuracy : %f%%", float(rightCountNormalized) / float(testDataSize)*100)

if __name__ == "__main__":
    main()