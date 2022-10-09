

dic_ejemplo = {'Alumnos': ["Carlos", "Ana", "Daniela", "Martín"],

'Curso': "Big Data",

'Edad': ('22', '21', '20', '22'),

'Presencial': True

}

# valor =list(dic_ejemplo.values())[2][2]
# print(valor)

#vamos a sacar la edad de Daniela
def sacarEdadDaniela(diccionario):
    print("La edad de Daniela:")
    valor =list(diccionario.values())[2][2]
    print(valor)



def EncuentraClave(diccionario ,clave):
    claves = list(diccionario.keys())
    # True if clave in claves else False
    if clave in claves:
        print("True")
        return True
    else: 
        print("False")
        return False
def set_edades(diccionario):
    mi_set = set(list(diccionario.values())[2])
    tamaño = mi_set.__len__()
    return mi_set , tamaño
# valores = dic_ejemplo.values()
# print(valores)
# def Valor(diccionario,clave):


# sacarEdadDaniela(dic_ejemplo)
# print(EncuentraClave(dic_ejemplo,"Centro"))