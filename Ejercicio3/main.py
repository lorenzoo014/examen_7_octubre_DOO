from ApartadoA import *
from ApartadoB import *
def primer_apartado():
    print("PRIMER APARTADO:\n")
    print("1.Crea un array de tamaño (6x6) con elementos aleatorios entre 0 y 10 inclusive.")
    matriz = array_6_6()
    print(matriz)
    print("2.Calcula el total de bytes que ocupa la matriz.")
    print(bytes(matriz))
    print("3.Calcula la media y la desviación estándar de los valores presentes en la matriz.")
    print(des_tipica_y_media(matriz))
    print("4.Crea un nuevo array del mismo tamaño que contenga elementos aleatorios con una distribución normal"
    +"con la misma media y la misma desviación estándar que el array original.")
    print("5.Crea un nuevo vector, convirtiendo todos los valores del array creado en el paso anterior en números enteros.")




if __name__ == "__main__":
