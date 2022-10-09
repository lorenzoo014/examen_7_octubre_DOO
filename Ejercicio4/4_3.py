# importamos la las librerias que necesitaremos
import pandas as pd
import numpy as np

# importamos los datos
# pd.read_csv('auto-mpg.data',delim_whitespace=True,header =None)
autos = pd.read_csv('auto-mpg.data',delim_whitespace=True,header = None)
nombres = ["mpg","cylinders","displacement","horsepower",
"weight","acceleration","model year","origin","car name"]

# reasinamos los nombres
autos.columns = nombres

print(autos.head())

# ejercicio 4.3.1

solucion431=autos[autos["weight"]>5000]
print("La solucion del 4.3.1 es:")
print(solucion431)

# ejercicio 4.3.2

# filtramos el year
frecuencias = autos[autos['model year'] == 76]

# luego contamos los elementos de cada cilindro y tomamos el maximo
solucion432=frecuencias['cylinders'].value_counts()
print("La solucion del 4.3.2 es:")
print(solucion432)

#ejercicio 4.3.3

# filtramos por modelo de año, luego seleccionamos los consumos y sacamos la media
media_70 = autos[autos['model year'] == 70]['mpg'].mean()
media_79 = autos[autos['model year'] == 79]['mpg'].mean()

# diferencia entre medias
solucion433=media_70-media_79
print("La solucion del 4.3.3 es:")
print(solucion433)
# si el numero es negativo, implica que en el año 79 consume mas, sino, en el 70 se consume mas por galon

#ejercicio 4.3.4

print("Mostramos tabla de 4.3.4 para ver que hay una variable que deberia ser continua:")
print(autos.describe(include='all')) # con esto notamos que hay una variable que deberia ser continuo...
# la convertimos a numerica con
autos['horsepower'] = pd.to_numeric(autos['horsepower'], errors='coerce')

# ahora ya podemos conseguir los nan de forma general(cualquier columna) con la siguiente instruccion
solucion434=autos[autos.isna().any(axis=1)]
print("La solucion del 4.3.4 es:")
print(solucion434)

#ejercicio 4.3.5

# ahora ya podemos conseguir los nan de forma general(cualquier columna) con la siguiente instruccion

autos_con_nan = autos[autos.isna().any(axis=1)]
solucion435=autos_con_nan
print("La solucion del 4.3.5 es:")
print(solucion434)

#ejercicio 4.3.6

solucion436=autos_con_nan['cylinders'].value_counts()
print("La solucion del 4.3.6 es:")
print(solucion436)

#ejercicio 4.3.7(te lo dejo comentado porque me da un error que no se solucionar)

# solo agregamos mas elementos dentro del filtro de la siguiente forma
#solucion437=autos[(autos['cylinders']>=6) and (autos['weight']>4000) and (autos['mpg']<=10)]
#print("La solucion del 4.3.7 es:")
#print(solucion437)