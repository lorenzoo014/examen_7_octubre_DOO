import numpy as np

#Ejercicio_1
def array_6_6():
    np.random.seed(36)
    matriz = np.random.randint(0,10,(6,6))
    print(matriz)
    return matriz

#Ejercicio_2
def bytes(matriz):
    bytes = matriz.nbytes
    return bytes

#Ejercicio_3
def des_tipica_y_media(matriz):
    des_tipica = np.std(matriz)
    media = np.mean(matriz)
    print(des_tipica,media)
    return des_tipica , media

#Ejercicio_4
def misma_matriz_media_des_tipica(matriz):
    np.random.seed(36)
    matriz_2 = np.random.normal(des_tipica_y_media(matriz), (6,6))
    print(matriz_2)
    return matriz_2

def matriz_ints(matriz):
    matriz_3 = misma_matriz_media_des_tipica(matriz).round()
    return matriz_3


