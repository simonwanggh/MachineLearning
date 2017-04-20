from numpy import *
print(log(0.04))
print(log(0.9))

print(max(item[1] for item in [('a',1),('b',2),('c',3)]))
print(max([('a',1),('b',2),('c',3)], key=lambda x:x[1]))