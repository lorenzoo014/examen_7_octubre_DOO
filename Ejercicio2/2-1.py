l=[18, 50, 210, 80, 145, 333, 70, 30]

lista_aux = []


def seleccionar(diccionario):
    for element in l:
        if(element%10 ==0 and element<200):
            lista_aux.append(element)
        elif(element>300):
            break
        return lista_aux
print(seleccionar(l))

# #hacemos un bucle para recorrerlo y mostrar lo que nos dicen

# #def imprimir(lista):

# newlist = [x for x in l if x%10==0 and x<200]
# print(newlist)

# for x in l:
#     if(x>300):
#         print(exit)
#         exit()







