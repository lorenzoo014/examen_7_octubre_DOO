
l=[18, 50, 210, 80, 145, 333, 70, 30]

lista_aux = []


def seleccionar(diccionario):
    for element in diccionario:
        if(element%10 ==0 and element<200):
            lista_aux.append(element)
        elif(element>300):
            break
        return lista_aux
print(seleccionar(l))