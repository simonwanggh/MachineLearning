from mlrampup.supervisedlearning.classifier import knn
from mlrampup.supervisedlearning.utils import fileProcessor as fp


def main():
    ''' Simple test
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    a = knn.classify0([1.1, 1.2], group, labels, 4)
    '''


    ''' Test read from file '''
    matReturn, classLabelVectorReturn = fp.file2matrix("C:\PythonProject\mlrampup\externalfiles\datingTestSet.txt" , '\t', [0,1,2], 3 )
    b = knn.classify0([26575, 10.650102, 0.866627], matReturn, classLabelVectorReturn, 12)
    print(b)

if __name__ == "__main__":
    main()