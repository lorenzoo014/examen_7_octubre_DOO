# importamos la las librerias que necesitaremos
import pandas as pd
import numpy as np
from itertools import product

#ejercicio 4.4.1

# meses
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
# Provincias/ciudades
provincias = ['Ciudad Autónoma de Melilla',
 'Comunitat Valenciana',
 'Aragón',
 'Galicia',
 'Cantabria',
 'País Vasco',
 'La Rioja',
 'Comunidad Foral de Navarra',
 'Comunidad de Madrid',
 'Andalucía',
 'Canarias',
 'Ciudad Autónoma de Ceuta',
 'Illes Balears',
 'Castilla y León',
 'Región de Murcia',
 'Principado de Asturias',
 'Extremadura',
 'Cataluña']

mix = ['Petrel',
'Sabadell',
'Cartagena',
'Cantabria',
'País Vasco',
'La Rioja',
'Comunidad Foral de Navarra',
'Comunidad de Madrid',
'Andalucía',
'Canarias',
'Ciudad Autónoma de Ceuta',
'Illes Balears',
'Andalusia',
'Canary Islands',
'Navarre' ,
'Valencia',
]

years = np.arange(1990, 2022, dtype=int)


# creamos el primer y el segundo dataframe

df1 = pd.DataFrame(list(product(provincias, years, meses)), columns=['Zona', 'years', 'meses'])
df1["temp"] = np.round(np.random.rand(len(provincias)*len(years)*len(meses))*100,2)
df2 = pd.DataFrame(list(product(mix, years, meses)), columns=['Zona', 'years', 'meses'])
df2["temp"] = np.round(np.random.rand(len(mix)*len(years)*len(meses))*100,2)

# para concatenarlos vectircalmente usamos

df1_y_df2 = pd.concat([df1, df2])
solucion441=df1_y_df2
print("La solucion del 4.4.1 es:")
print(solucion441)

# habra que reindexar


#ejercicio 4.4.2

# solo agregaremos las que tengas informacion de comun de ciudades
solucion442=df1.merge(df2,how='inner',on=['Zona','years','meses'])
print("La solucion del 4.4.2 es:")
print(solucion442)

#ejercicio 4.4.3

desarrollador = ['a','b','c','d','e','f','g','h','i'] # otros desarrolladores
version = ['ver1','ver2','ver3','ver4','ver5','ver6'] # versiones
desarrollador2 = ['a','b','d','k','t','f','g','h','i','p','o','x.v'] # desarrolladores
version2 = ['ver1','ver10','ver3','ver98','ver5','ver6'] # otras versiones

equipo1 = pd.DataFrame(list(product(version,desarrollador)), columns=[ 'version', 'desarrolador'])
equipo1["aportaciones"] = np.random.randint(8,size=len(desarrollador)*len(version))

equipo2 = pd.DataFrame(list(product(version2,desarrollador2)), columns=[ 'version', 'desarrolador'])
equipo2["aportaciones"] = np.random.randint(13,size=len(desarrollador2)*len(version2))

# unimos
equipo1_y_equipo2 = pd.concat([equipo1, equipo2])
solucion443=equipo1_y_equipo2.shape
print("La solucion del 4.4.3 es:")
print(solucion443)

#ejercicio 4.4.4

solucion444=equipo1.merge(equipo2,on=['version', 'desarrolador'],how='outer').shape
print("La solucion del 4.4.4 es:")
print(solucion444)

#ejercicio 4.4.5

solucion445=equipo1.merge(equipo2,on=['version', 'desarrolador'],how='inner').shape
print("La solucion del 4.4.5 es:")
print(solucion445)

#ejercicio 4.4.6

# importamos los datos
# pd.read_csv('auto-mpg.data',delim_whitespace=True,header =None)
autos = pd.read_csv('auto-mpg.data',delim_whitespace=True,header = None)
nombres = ["mpg","cylinders","displacement","horsepower",
"weight","acceleration","model year","origin","car name"]

# reasinamos los nombres
autos.columns = nombres

# la convertimos a numerica con

autos['horsepower'] = pd.to_numeric(autos['horsepower'], errors='coerce')

print("Mostramos dataset:")
print(autos.head())

# agrupamos por año y sacamos la media

autos_years = autos.groupby('model year').mean()
solucion446=autos_years
print("La solucion del 4.4.6 es:")
print(solucion446)

#ejercicio 4.4.7

#improtamos matplotlib
import matplotlib.pyplot as plt
autos_years.plot(subplots=True,figsize=(12,60))
plt.xticks(np.arange(min(autos_years.index), max(autos_years.index)+1, 1.0))
plt.tight_layout()
solucion447=(plt.show())
print(solucion447)

#ejericio 4.4.8

autos_years['weight'].plot(figsize=(12,12))
plt.xticks(np.arange(min(autos_years.index), max(autos_years.index)+1, 1.0))
solucion448=(plt.show())
print(solucion448)






