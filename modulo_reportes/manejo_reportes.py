import sys
import os

sys.path.append("..")

from datosGenerales.datos import *

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RUTA_JSON_VENTAS = os.path.join(project_root, "modulo_ventas", "ventas.json")

def servicios_populares():
    datos_ventas = cargar_datos(RUTA_JSON_VENTAS)

    contador = 0

    ventas_por_servicio = {}

    for venta in datos_ventas["ventas"]:
        if venta["categoria"] == "servicios":
            servicio = venta["referencia_articulo"]
            if servicio in ventas_por_servicio:
                ventas_por_servicio[servicio] += venta["cantidad"]
            else:
                ventas_por_servicio[servicio] = venta["cantidad"]

    print("TOP 5 SERVICIOS MÁS POPULARES")
    print("")
    for llave, valor in ventas_por_servicio.items():
        contador += 1
        if(contador < 6):
            print(f"Servicio: {llave}, Cantidad Vendida: {valor}")
        else:
            break
    
        


