import numpy as np
print(np.matrix([1,2])+np.matrix([2,2]))

list1 = [[1,2],[1,1],[3,3]]
list2 = [6,6,6]
print(list1+list2)
list3 = [[6],[6],[6]]
print(list1+list3)

print(list(map(lambda x:x+['a']  , list1)))

print(list(zip(list2,list1)))

print(dict(zip(list2,list1)))

list4 = [9,8,7]
print(zip(list4,list1))

b = list(zip(list4,list1))
print(b)

def sortFun(item):
    return item[0]

print(sorted(b, key = sortFun))

print(sorted(zip(list4,list1), key = lambda x:x[0]))

list5 = [8,8,6]
c = sorted(zip(list5,list1), key = lambda x:x[0])

print("BBBBBBBBB")
print(sum(np.matrix([1,2])[0]))

print("C:" + str(c))
d = {}
from itertools import *
from functools import *
from numpy import *
for k, g in groupby(c, lambda x:x[0]):
    gl = list(g)
    print("========")
    t = tuple((k,list([0,0])))
    print(t[1])
    gl.append(t)
    print(gl)
    def lam( x,y):
        print("AAAAAAAAAAAA")
        print(x,y)
        return (x[0]+np.matrix(y[1]), x[1] + sum(y[1]))
    d[k] = reduce(lam,gl,(np.matrix(ones(2)),2))

print("RRRRRRRRRRRRRR")
print(d)

aa = {}
bb = {1:1}
cc = aa.update(bb)
print(aa)

print("map dict")
def mapdict(x):
    print(x)
    return {x:d[x][0]/d[x][1]}
mapdict = map(mapdict, d)
#print(list(mapdict))
def lam2(x,y):
    print(x,y)
    x.update(y)
    return x
dict1 = reduce(lam2, mapdict, {})
print(dict1)





print ([0]*3*3)

print([[0 for i in range(3)] for k in range(3)])


print(np.array([2,2])*np.array(np.matrix([2,3])[0]))

