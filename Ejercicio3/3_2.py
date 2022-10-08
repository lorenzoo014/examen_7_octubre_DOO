#importamos numpy para poder crear la matriz
import numpy as np


#3.2.1
array = np.random.randint(100 , size=(3, 4))


#3.2.2
for i in range(array.size):
    if(array[i]>0 and array[i]%5==0):
        array[i]=[i]
    else:
        array[i]=-1
print(array)