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

def total_servicios():
    datos = cargar_datos(RUTA_JSON)
    cantidad_productos = 0

    contador_telefonia = 0
    contador_internet = 0
    contador_television = 0
    contador_datos = 0
    contador_minutos = 0
    

    for i in datos["servicios"]:
        for llave, valor in i.items():
            for j in valor:
                if(j["eliminado"] == False):
                    cantidad_productos += 1
                    if(llave == "telefonia"):
                        contador_telefonia += 1
                    elif(llave == "internet"):
                        contador_internet += 1
                    elif(llave == "television"):
                        contador_television += 1
                    elif(llave == "datos"):
                        contador_datos += 1
                    elif(llave == "minutos"):
                        contador_minutos += 1
    print(f"Total servicios ofrecidos: {cantidad_productos}")
    print(f"Telefonia: {contador_telefonia}") if contador_telefonia > 0 else contador_telefonia
    print(f"Internet: {contador_internet}") if contador_internet > 0 else contador_internet
    print(f"Televisión: {contador_television}") if contador_television > 0 else contador_television
    print(f"Datos: {contador_datos}") if contador_datos > 0 else contador_datos
    print(f"Minutos: {contador_minutos}") if contador_minutos > 0 else contador_minutos                
