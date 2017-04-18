
trainCategory = ['a','b','a','a','c','c','a','d']
numTrainDocs = 8
typeSet = set(trainCategory)
pTypesDict = {i:(trainCategory.count(i)/float(numTrainDocs)) for i in typeSet}
print(pTypesDict['a'])