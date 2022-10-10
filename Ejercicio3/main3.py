from ApartadoA import *
from ApartadoB import *
def primer_apartado():
    print("PRIMER APARTADO:\n")
    print("1.Crea un array de tamaño (6x6) con elementos aleatorios entre 0 y 10 inclusive.")
    matriz = array_6_6()
    print(matriz)
    print("")
    print("2.Calcula el total de bytes que ocupa la matriz.")
    print(bytes(matriz))
    print("")
    print("3.Calcula la media y la desviación estándar de los valores presentes en la matriz.")
    print(des_tipica_y_media(matriz))
    print("")
    print("4.Crea un nuevo array del mismo tamaño que contenga elementos aleatorios con una distribución normal"
    +"con la misma media y la misma desviación estándar que el array original.")
    print(misma_matriz_media_des_tipica(matriz))
    print("")
    print("5.Crea un nuevo vector, convirtiendo todos los valores del array creado en el paso anterior en números enteros.")
    print(matriz_ints(matriz))
    print("")
def segundo_apartado():
    print("SEGUNDO APARTADO\n")
    print("1.Crea un array de tamaño (3x4) de todos los números enteros entre 0 y 100 que sean múltiplos de 9.")
    array = matriz_3_4()
    print("")
    print("2.Filtra todos los valores del vector creado en el paso anterior de la siguiente manera:"+
"Si son valores positivos y múltiplos de 5 se conservan sin cambios"+
"En el caso contratio se sustituyen con el valor -1")
    filtrado(array)
    print("")



if __name__ == "__main__":
    segundo_apartado()
