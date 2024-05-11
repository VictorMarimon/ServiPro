import sys

sys.path.append("..")

from datosGenerales.datos import *

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/productos/productos.json"

def referencia_productos(categoria):
    datos = cargar_datos(RUTA_JSON)

    referencias = []

    for i in datos["productos"][0][categoria]:
        referencias.append(str(i["referencia"]))
    
    return referencias

def tipo_productos():
    datos = cargar_datos(RUTA_JSON)

    referencias = []

    for i in datos["productos"][0]:

        referencias.append(str(i))
    
    return referencias
