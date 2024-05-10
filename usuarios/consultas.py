import sys

sys.path.append("..")

from datosGenerales.datos import *

RUTA_JSON = "usuarios.json"

def fecha_afiliacion(documento):
    datos_json = cargar_datos(RUTA_JSON)
    contador = int(len(datos_json["usuarios"]))
    for i in datos_json["usuarios"]:
        if(int(documento) == i["documento"] and i["eliminado"] == False):
            return i["fecha_afiliacion"]
        else:
            contador -= 1
    
    if(contador == 0):
        return(False)
    
