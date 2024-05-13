import sys

sys.path.append("..")

from datosGenerales.datos import *

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_ventas/ventas.json"
RUTA_JSON_CATALOGO = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_ventas/catalogo_ventas.json"

def actualizar_catalogo_ventas():
    datos = cargar_datos(RUTA_JSON_CATALOGO)
    for i in datos:
        datos["catalogo_ventas"] = catalogo_ventas()
        guardar_datos(datos, RUTA_JSON_CATALOGO)

def catalogo_ventas():
    datos = cargar_datos(RUTA_JSON)
    catalogo = []

    for i in datos["ventas"]:
        if i["categoria"] == "productos":
            producto_catalogo = {}

            producto_catalogo["categoria"]= i["categoria"]
            producto_catalogo["tipo"]= i["tipo"]
            producto_catalogo["referencia"]= i["referencia_articulo"]
            producto_catalogo["cantidad"]= i["cantidad"]

            encontrado = False
            for producto in catalogo:
                if producto["referencia"] == producto_catalogo["referencia"]:
                    producto["cantidad"] += i["cantidad"]
                    encontrado = True
                    break

            if not encontrado:
                catalogo.append(producto_catalogo)
        elif i["categoria"] == "servicios":
            servicios_catalogo = {}

            servicios_catalogo["categoria"]= i["categoria"]
            servicios_catalogo["tipo"]= i["tipo"]
            servicios_catalogo["referencia"]= i["referencia_articulo"]
            servicios_catalogo["cantidad"]= i["cantidad"]

            encontrado = False
            for producto in catalogo:
                if producto["referencia"] == servicios_catalogo["referencia"]:
                    producto["cantidad"] += i["cantidad"]
                    encontrado = True
                    break

            if not encontrado:
                catalogo.append(servicios_catalogo)
    print(catalogo)
    return catalogo
