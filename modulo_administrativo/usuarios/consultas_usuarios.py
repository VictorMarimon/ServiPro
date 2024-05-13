import sys

sys.path.append("..")

from datosGenerales.datos import *

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_administrativo/usuarios/usuarios.json"

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

    
