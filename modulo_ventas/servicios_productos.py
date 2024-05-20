import sys
import os

sys.path.append("..")

from modulo_servicios.productos.consultas_productos import productos_catalogo
from modulo_servicios.servicios.consultas_servicios import servicios_catalogo
from modulo_administrativo.usuarios.consultas_usuarios import nombres_documentos_usuarios
from datosGenerales.datos import *

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RUTA_JSON = os.path.join(project_root, "modulo_ventas", "registro.json")
RUTA_JSON_VENTAS = os.path.join(project_root, "modulo_ventas", "ventas.json")

def actualizar_registro():
    datos = cargar_datos(RUTA_JSON)
    for i in datos:
            datos["productos"] = productos_catalogo()
            datos["servicios"] = servicios_catalogo()
            guardar_datos(datos, RUTA_JSON)

def leer_registos():
    datos = cargar_datos(RUTA_JSON)
    cantidad_productos = 0
    cantidad_servicios = 0
    for llave,valor in datos.items():
        if(llave == "servicios"):
            print("CATALOGO SERVICIOS")
            for j in valor:
                cantidad_servicios += 1
                print("")
                print(f"Servicio No. {cantidad_servicios}")
                print("")
                print(f"Tipo: {j['articulo']}")
                print(f"Referencia: {j['referencia']}")
                print(f"Nombre: {j['nombre']}")
                print(f"Precio: {j['precio']}")
                print("")
        elif(llave == "productos"):
            print("CATALOGO PRODUCTOS")
            for j in valor:
                cantidad_productos += 1
                print("")
                print(f"Producto No. {cantidad_productos}")
                print("")
                print(f"Tipo: {j['articulo']}")
                print(f"Referencia: {j['referencia']}")
                print(f"Nombre: {j['nombre']}")
                print(f"Precio: {j['precio']}")
                print("")

def compras_usuarios():
    datos = cargar_datos(RUTA_JSON_VENTAS)
    compras_totales = []
    for i in datos["ventas"]:
        if(i["categoria"] == "servicios"):
            compras = {}
            compras["documento_usuario"] = i["documento_usuario"]
            compras["cantidad_servicios"] = i["cantidad"]
            encontrado = False
            for servicio in compras_totales:
                if servicio["documento_usuario"] == compras["documento_usuario"]:
                    servicio["cantidad_servicios"] += i["cantidad"]
                    encontrado = True
                    break

            if not encontrado:
                compras_totales.append(compras)
    return compras_totales

def ventas():
    datos_clientes = nombres_documentos_usuarios()
    datos = cargar_datos(RUTA_JSON_VENTAS)
    contador_ventas = 0
    for i in datos_clientes:
        for j in datos["ventas"]:
            if(i["documento"]== j["documento_usuario"]):
                contador_ventas += 1
                print("")
                print(f"Venta No. {contador_ventas}") 
                print("")
                print("Fecha= ", j["fecha_compra"])
                print("Tipo= ", j["tipo"])
                print("Referencia articulo= ", j["referencia_articulo"])
                print("Cantidad= ", j["cantidad"])
                print("Cliente= ", i["nombre"])
                print("Estado= Completada")
                print("")
    if(contador_ventas == 0):
        print("No hay registro de ventas")

        


