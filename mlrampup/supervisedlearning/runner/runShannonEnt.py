import numpy as np
from mlrampup.supervisedlearning.classifier import decideTree as dt
import logging

logger = logging.getLogger('tofile')


def main():
   dataSet = [['yes'],['yes'],['no'],['no'],['no']]
   logger.info("Entropy : %f", dt.calcShannonEntropy(dataSet))

   dataSet[0][0] = 'maybe'
   logger.info("Entropy : %f", dt.calcShannonEntropy(dataSet))

if __name__ == '__main__':
    main()
