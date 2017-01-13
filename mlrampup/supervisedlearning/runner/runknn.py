from mlrampup.supervisedlearning.classifier import knn
from mlrampup.supervisedlearning.utils import fileProcessor as fp
from mlrampup.supervisedlearning.utils import dataProcessor as dp
import numpy as np


def main():
    #Simple test
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    a = knn.classify0([1.1, 1.2], group, labels, 4)
    print("Simple tesst : "+a)


    ''' Test read from file '''
    matReturn, classLabelVectorReturn = fp.file2matrix("C:\PythonProject\mlrampup\externalfiles\datingTestSet.txt" , '\t', [0,1,2], 3 )
    b = knn.classify0([68846,9.974715,0.669787], matReturn, classLabelVectorReturn, 12)
    print("read from file : "+b)

    #after normlized
    normMat, ranges , minVals = dp.autoNorm(matReturn)
    c = knn.classify0(dp.normalizeSample([68846, 9.974715, 0.669787],minVals,range), matReturn, classLabelVectorReturn, 12)
    print("read from file and normlized : " + b)

if __name__ == "__main__":
    main()