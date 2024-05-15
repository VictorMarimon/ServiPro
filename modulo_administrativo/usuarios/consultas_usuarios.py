import sys
import os

sys.path.append("..")

from datosGenerales.datos import *

#RUTAS
ruta_base = os.path.dirname(os.path.abspath(__file__))
RUTA_JSON = os.path.join(ruta_base,  "usuarios.json")

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
    
def documentos_usuarios():
    datos = cargar_datos(RUTA_JSON)

    referencias = []

    for i in datos["usuarios"]:
        referencias.append(int(i["documento"]))
    
    return referencias

def nombres_documentos_usuarios():
    datos = cargar_datos(RUTA_JSON)

    datos_usuarios = []

    for i in datos["usuarios"]:
        info ={}
        info["documento"] = int(i["documento"])
        info["nombre"] = i["nombre"]
        datos_usuarios.append(info)
    
    return datos_usuarios   
