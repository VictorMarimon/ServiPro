import sys

sys.path.append("..")

from datosGenerales.datos import *

RUTA_JSON = RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/servicios/servicios.json"


def referencia_servicios(categoria):
    datos = cargar_datos(RUTA_JSON)

    referencias = []

    for i in datos["servicios"][0][categoria]:
        referencias.append(str(i["referencia"]))
    
    return referencias

def tipo_servicios():
    datos = cargar_datos(RUTA_JSON)

    referencias = []

    for i in datos["servicios"][0]:

        referencias.append(str(i))
    
    return referencias
