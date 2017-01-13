import numpy as np
import operator
import logging

logger = logging.getLogger('tofile')

def file2matrix(filename, delimiter, featureColumns,labelColIndice):
    try:
        fr = open(filename)
        arrayLines = fr.readlines()
        numberOfLines = len(arrayLines)

        matReturn = np.zeros((numberOfLines,len(featureColumns)))
        classLabelVectorReturn = []
        index = 0
        for line in arrayLines:

            line = line.strip()
            listLine = line.split(delimiter)
            if len(listLine) < 4:
                logger.warn('Dirty Data - line number : %d', index)
                classLabelVectorReturn.append(None)
            else:
                matReturn[index,:] = [listLine[i] for i in featureColumns]
                if labelColIndice is not None : classLabelVectorReturn.append(listLine[labelColIndice])
            index = index + 1
    except Exception as e:
        logging.error('Failed to transfer', exc_info=True)

    return matReturn,classLabelVectorReturn
