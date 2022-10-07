
import copy
#-----------Ejercicio_1.1-----------#
lista = []
tupla = (1,2,3)
lista.append(5)
lista.append("hola")
lista.append(True)
lista.append(tupla)
print(lista)

#-----------Ejercicio_1.2-----------#
posicion=-1
for i in range(2,5,2):
    print(lista[posicion])
    posicion = posicion-i


#-----------Ejercicio_1.3-----------#
elemento_ultimo = lista[-1]
lista[-1]=lista[0]
lista[0]=elemento_ultimo
print(lista)

#-----------Ejercicio_1.4-----------#
lista.pop()
print(lista)

#-----------Ejercicio_1.5-----------#
lista2 = lista.copy()

