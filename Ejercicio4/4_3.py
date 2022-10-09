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