from Apartado_1 import *
from Apartado_2 import *
def primer_apartado():
    m=[18, 50, 210, 80, 145, 333, 70, 30]
    print("PRIMER APARTADO \n")
    print("1.Recorre el listado del ejemplo y realiza las siguientes operaciones: [18, 50, 210, 80, 145, 333, 70, 30]" +
"\n     Imprimir el número en caso de que sea múltiplo de 10 y menor que 200"+
"\n     Parar el programa si llega a un número mayor que 300")
    print(seleccionar(m))
def segundo_apartado():
    c=["PEP 8", "PEP 248", "PEP 257"]
    print("2.2.1 Escribe una función que devuelva el número total de carácteres en un listado de cadenas de texto"+
    '\n     y aplícala sobre el ejemplo:'
    "\n     Entrada a la función: [PEP 8, PEP 248, PEP 257]   "        
    "\n     La salida esperada: 19")
    print("La salida es:")
    print(totalcaracteres(c))





if __name__== "__main__":
    primer_apartado() 
    segundo_apartado()