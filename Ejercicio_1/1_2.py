

dic_ejemplo = {'Alumnos': ["Carlos", "Ana", "Daniela", "Martín"],

'Curso': "Big Data",

'Edad': ('22', '21', '20', '22'),

'Presencial': True

}

valor =list(dic_ejemplo.values())[2][2]
print(valor)

#vamos a sacar la edad de Daniela
def sacarEdadDaniela(diccionario):
    print("La edad de Daniela:")
    valor =list(diccionario.values())[2][2]
    print(valor)



def EncuentraClave(diccionario ,clave):
    claves = list(diccionario.keys())
    # True if clave in claves else False
    if clave in claves:
        return True
    else: 
        return False

# sacarEdadDaniela(dic_ejemplo)
EncuentraClave(dic_ejemplo,"Centro")