import numpy as np
from mlrampup.supervisedlearning.classifier import decideTreeID3 as dt

import logging

logger = logging.getLogger('tofile')

def main():
   dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no'], [0,0,'unknown']]
   featIndexLabelDict = {0:'no surfacing',1:'flippers'}
   ret = dt.creatTree(dataSet,featIndexLabelDict,-1)
   logger.info("Tree : " + str(ret))

   item1 = (1,1)
   featLabelIndexDict = {'no surfacing':0, 'flippers':1}
   logger.info("item1"+str(item1)+" yes or no : " + dt.classify(item1, featLabelIndexDict, ret ))

   item2 = (1,0)
   logger.info("item2" + str(item2) + " yes or no : " + dt.classify(item2, featLabelIndexDict, ret))

   item3 = (0,1)
   logger.info("item3" + str(item3) + " yes or no : " + dt.classify(item3, featLabelIndexDict, ret))

   item4 = (0,0)
   logger.info("item4" + str(item4) + " yes or no : " + dt.classify(item4, featLabelIndexDict, ret))
if __name__ == '__main__':
    main()