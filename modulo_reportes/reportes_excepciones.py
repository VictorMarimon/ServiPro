import sys
import os

sys.path.append("..")

from datosGenerales.datos import *

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RUTA_TXT = os.path.join(project_root, "modulo_reportes", "reportes.txt")


def consultar_reportes():
    datos = leer_txt(RUTA_TXT)
    print(datos)
        
def agregar_reportes(dato):
    escribir_txt(dato, RUTA_TXT)
    
    #falta utilizar funcion en excepciones
    
    

