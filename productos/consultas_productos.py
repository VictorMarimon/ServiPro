import sys

sys.path.append("..")

from datosGenerales.datos import *

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/productos/productos.json"

def referencia_productos():
    datos = cargar_datos(RUTA_JSON)

    referencias = []

    for i in datos["productos"][0]["telefonos"]:
        referencias.append(str(i["referencia"]))
    
    return referencias
