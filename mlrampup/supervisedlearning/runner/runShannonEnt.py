import numpy as np
from mlrampup.supervisedlearning.utils import dataProcessor as dp
import logging

logger = logging.getLogger('tofile')


def main():
   dataSet = [['yes'],['yes'],['no'],['no'],['no']]
   logger.info("Entropy : %f", dp.calcShannonEntropy(dataSet))

   dataSet[0][0] = 'maybe'
   logger.info("Entropy : %f", dp.calcShannonEntropy(dataSet))

if __name__ == '__main__':
    main()
