import numpy as np
from mlrampup.supervisedlearning.classifier import decideTreeID3 as dt
import logging

logger = logging.getLogger('tofile')


def main():
   dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
   ret = dt.chooseBestFeatureToSplit(dataSet,(0,1),2)
   logger.info("Best Feature : %d  Information Gain : %f", ret[0], ret[1])

if __name__ == '__main__':
    main()
