import matplotlib.pyplot as plt

def getNumLeafs(tree):
    numLeaf = 0
    firstStr = list(tree.keys())[0]
    followDict = tree[firstStr]
    for key in followDict.keys():
        if type(followDict[key]).__name__ == 'dict':
            numLeaf += getNumLeafs(followDict[key])
        else:
            numLeaf += 1

    return numLeaf

def getTreeDepth(tree):
    depth = 0
    firstStr = list(tree.keys())[0]
    followDict = tree[firstStr]
    for key in followDict.keys():
        if type(followDict[key]).__name__ == 'dict':
            thisDepth = 1+getTreeDepth(followDict[key])
        else:
            thisDepth = 1
        if thisDepth > depth :
            depth = thisDepth

    return depth

def createPlot(tree):
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks=[],yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon = False, **axprops)
    plotTree.totalW = float(getNumLeafs(tree))
    plotTree.totalD = float(getTreeDepth(tree))
    plotTree.xOff = -0.5/plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(tree, (0.5,1.0), '')
    plt.show()

arrow_args = dict(arrowstyle = "<-")
decisionNode = dict(boxstyle="sawtooth",fc = "0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',xytext=centerPt, textcoords='axes fraction', va="center"
                            , ha="center", bbox = nodeType, arrowprops = arrow_args)

def plotMidTest(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)

def plotTree(tree, parentPt, nodeText):
    numLeaf = getNumLeafs(tree)
    depth = getTreeDepth(tree)
    firstStr = list(tree.keys())[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeaf))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidTest(cntrPt,parentPt,nodeText)
    plotNode(firstStr,cntrPt,parentPt,decisionNode)
    secondDict = tree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key],cntrPt,str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
            plotMidTest((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD