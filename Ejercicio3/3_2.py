#importamos numpy para poder crear la matriz
import numpy as np
import random

#3.2.1
array = np.random.randint(100 , size=(3, 4))


#3.2.2
for i in array:
    if(i>0 and i%5==0):
        array[i]=i
    else:
        array[i]=-1
print(array)