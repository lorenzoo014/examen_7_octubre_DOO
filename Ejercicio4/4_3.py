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
print(solucion431)

# ejercicio 4.3.2
# filtramos el year
frecuencias = autos[autos['model year'] == 76]

# luego contamos los elementos de cada colindroo y tomamos el maximo
frecuencias['cylinders'].value_counts()

