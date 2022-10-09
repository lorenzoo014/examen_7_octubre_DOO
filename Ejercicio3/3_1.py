import numpy as np

#Ejercicio_1
np.random.seed(36)
matriz = np.random.randint(0,10,(6,6))
print(matriz)
print()

#Ejercicio_2
print(matriz.nbytes)

#Ejercicio_3

#desv. tipica
des_tipica = np.std(matriz)
media = np.mean(matriz)
print(des_tipica,media)

#Ejercicio_4
np.random.seed(36)
matriz_2 = np.random.normal(media, des_tipica, (6,6))
print(matriz_2)
matriz_2 = matriz_2.round()
print(matriz_2)


