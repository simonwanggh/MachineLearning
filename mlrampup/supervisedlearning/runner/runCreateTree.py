import numpy as np
from mlrampup.supervisedlearning.classifier import decideTree as dt
import logging

logger = logging.getLogger('tofile')

def main():
   dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
   featIndexLabelDict = {0:'no surfacing',1:'flippers'}
   ret = dt.creatTree(dataSet,featIndexLabelDict,-1)
   logger.info("Tree : " + str(ret))

if __name__ == '__main__':
    main()