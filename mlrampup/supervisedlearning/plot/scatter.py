import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import itertools as itr
import numpy as np

def scatter(matdata, x=0, y=1, s =20 , c=None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    colors = itr.cycle(["r","g","b","w","c","m","y","k"])
    uniqueColorLabel = np.unique(c)
    colorInput = None
    if c is not None :
        colorMap = {i : next(colors) for i in  uniqueColorLabel}
        #Nan data will display as white
        colorInput = [colorMap[i] if i is not None else "w" for i in c]
        recs = []
        #add legend
        for label in uniqueColorLabel:
            recs.append(mpatches.Rectangle((0,0),1,1,fc=colorMap[label]))
        plt.legend(recs,uniqueColorLabel,loc = 2)
    ax.scatter(matdata[:,x],matdata[:,y],s, colorInput)
    plt.show()