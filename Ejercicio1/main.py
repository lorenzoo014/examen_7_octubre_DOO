from Apartado1 import Apartado_1
from Apartado2 import *

def primer_apartado():
    print("APARTADO_1:\n")
        #-----------PRIMER PUNTO-----------#
    print("1.Define una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python.")
    print("La lista es la siguiente:")
    lista = Apartado_1.elementos()
    print(lista)
    print("")
    #-----------SEGUNDO PUNTO-----------#
    print("2.Selecciona cada dos elementos (uno si otro no) desde el final de la lista.")
    print(Apartado_1.cada_dos(lista))
    print("")
    #-----------TERCER PUNTO-----------#
    print("3.Cambia solamente la posición del primer elemento con el último elemento de la lista.")
    print("     lista original:")
    print(lista)
    print("     lista cambiada:")
    print(Apartado_1.cambia_elementos(lista))
    print("")
    #-----------CUARTO PUNTO-----------#
    print("4.Elimina el último elemento de la lista modificada en el paso anterior.")
    print(Apartado_1.quita_ultimo(lista))
    print("")
    #-----------QUINTO PUNTO-----------#
    print("5.Crea una nueva lista con la repetición de los elemento de la lista guardada en el paso anterior.")
    print(Apartado_1.copia(lista))
    print("")

def segundo_apartado():
    print("APARTADO_2:\n")
    dic_ejemplo = {'Alumnos': ["Carlos", "Ana", "Daniela", "Martín"],

'Curso': "Big Data",

'Edad': ('22', '21', '20', '22'),

'Presencial': True

}
    print("1.Saca e imprime la edad de DANIELA utilizando los datos del diccionario declarado en el ejemplo.")    
    print(sacarEdadDaniela(dic_ejemplo))
    print("")
    print("2.Consulta si el CENTRO se encuentra entre las claves existentes en el diccionario o no.")
    print("¿Esta en el diccionario la clave Centro?")
    print(EncuentraClave(dic_ejemplo,'Centro'))
    print("")
    # print("3.Averigua de qué tipo es el valor asociado al CURSO y calcula su tamaño (longitud)")
    # print("")
    print("4.Construye un set a partir de las edades de todos los alumnos y muestra el tamaño de esa colección.")
    print(set_edades(dic_ejemplo))
    print("")

if __name__ == "__main__":
    primer_apartado()
    segundo_apartado()



