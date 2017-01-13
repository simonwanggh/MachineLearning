from mlrampup.supervisedlearning.utils import fileProcessor as fp
from mlrampup.supervisedlearning.utils import dataProcessor as dp
from mlrampup.supervisedlearning.plot import scatter as sct
import numpy as np
import logging

logger = logging.getLogger('tofile')

def main():
    matReturn, classLabelVectorReturn = fp.file2matrix("C:\PythonProject\mlrampup\externalfiles\datingTestSet.txt" , '\t', [0,1,2], 3 )
    uniqueLabels = np.unique(classLabelVectorReturn)
    uniqueLabelMap = {uniqueLabels[i] : int(i+1) for i in range(len(uniqueLabels))}
    logger.info("data matrix size : %d" ,len(matReturn))
    logger.info("label size : %d", len(classLabelVectorReturn))
    z = [uniqueLabelMap[label] if label is not None else np.nan for label in classLabelVectorReturn]
    sct.scatter(matReturn,1,2,s=50.0*np.array(z),c=np.array(classLabelVectorReturn))
    logger.info("after normlize!")
    normMat, ranges, minVals = dp.autoNorm(matReturn)
    sct.scatter(normMat, 1, 2, s=50.0 * np.array(z), c=np.array(classLabelVectorReturn))

if __name__ == "__main__":
    main()