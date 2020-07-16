import numpy.matlib 
import numpy as np

def DotProduct(N, listA, listB):

    
    print(np.dot(listA, listB))


DotProduct(10, np.random.randint(1,1000,10), np.random.randint(1,1000,10))

DotProduct(100, np.random.randint(1,1000,100), np.random.randint(1,1000,100))




