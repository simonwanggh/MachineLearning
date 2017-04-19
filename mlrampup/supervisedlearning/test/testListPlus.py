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
print(np.matrix([1,2]))

print("C:" + str(c))
d = {}
from itertools import *
from functools import *
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
        return x+np.matrix(y[1])
    d[k] = reduce(lam,gl,np.matrix([0,0]))

print(d)






#print(sum([1,1]))
