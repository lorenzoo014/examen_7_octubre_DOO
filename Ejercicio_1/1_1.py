import copy
class Apartado_1():

#-----------Ejercicio_1.1-----------#
    @staticmethod
    def elementos(lista=[]):
        tupla = (1,2,3)
        lista.append(5)
        lista.append("hola")
        lista.append(True)
        lista.append(tupla)
        return lista

#-----------Ejercicio_1.2-----------#
    @staticmethod
    def cada_dos(lista=[]):
        posicion=-1
        for i in range(2,5,2):
            lista2 =[]
            lista2.append(lista[posicion])
            posicion = posicion-i
        return lista2


#-----------Ejercicio_1.3-----------#
    @staticmethod
    def cambia_elementos(lista=[]):   
        elemento_ultimo = lista[-1]
        lista[-1]=lista[0]
        lista[0]=elemento_ultimo
        return lista

#-----------Ejercicio_1.4-----------#
    @staticmethod
    def quita_ultimo(lista=[]):
        lista.pop()
        return lista

#-----------Ejercicio_1.5-----------#
    @staticmethod
    def copia(lista=[]):
        lista2 = lista.copy()

