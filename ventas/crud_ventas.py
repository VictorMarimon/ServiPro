import sys

sys.path.append("..")

from datosGenerales.datos import *
from usuarios.consultas_usuarios import documentos_usuarios
from servicios.consultas_servicios import *
from productos.consultas_productos import *

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/ventas/ventas.json"

def crear_ventas(categoria):
    datos = cargar_datos(RUTA_JSON)
    nuevas_ventas = {}

    producto = "productos"

    print(" ")
    print(" AGREGAR VENTAS ")
    print(" ")

    cantidad_ventas = int(len(datos["ventas"]))
    estado = False

    for i in range(0, cantidad_ventas):
        cantidad_ventas += 1

    nuevas_ventas["id"] = int(cantidad_ventas)

    nuevas_ventas["referencia"] = input("Ingrese la referencia: ")

    documento = int(input("Ingrese el documento del cliente: "))

    if(documento in documentos_usuarios()):

        try:
            nuevas_ventas["documento_usuario"] = documento
        except ValueError:
            documento_base = 00000
            print("Documento mal escrito (se le asignara un documento base)")
            nuevas_ventas["documento_usuario"] = documento_base
        
        if(categoria == "productos"):

            nuevas_ventas["categoria"] = "productos"

            tipo_producto = input("Ingrese el tipo de producto: ")

            if(tipo_producto.lower() in tipo_productos()):

                nuevas_ventas["tipo"] = tipo_producto

                referencia = input("Ingrese la referencia del producto: ")

                if(referencia in referencia_productos(tipo_producto)):
                    try:
                        nuevas_ventas["referencia_articulo"] = referencia
                    except Exception:
                        referencia_base = "xxxxxxx"
                        print("Referencia con mala ortografia (se asignara una referencia generica)")
                        nuevas_ventas["referencia_articulo"]= referencia_base

                    try:
                        nuevas_ventas["cantidad"] = int(input("Ingrese la cantidad: "))
                    except Exception:
                        cantidad_base = 0
                        print("Cantidad mal escrita (se le asignara una cantidad base)")
                        nuevas_ventas["cantidad"] = cantidad_base

                    try:
                        print("Ingrese la fecha de compra")
                        nuevas_ventas["fecha_compra"] = input("(ej. 01/10/1997) ")
                    except Exception:
                        fecha_compra_base = "01/01/2024"
                        print("Fecha de compra incorrecta (se le asignara una fecha generica)")
                        nuevas_ventas["fecha_compra"] =  fecha_compra_base
                    
                    nuevas_ventas["eliminado"] = estado
                    
                    datos["ventas"].append(nuevas_ventas)
                    guardar_datos(datos, RUTA_JSON)
                    print("")
                    print("Venta Registrada")
                else:
                    print(f"El producto {referencia} no existe")
            else:
                print(f"El tipo de producto {tipo_producto} NO existe")

        elif(categoria == "servicios"):
            nuevas_ventas["categoria"] = "servicios"

            tipo_servicio = input("Ingrese el tipo de servicio: ")

            if(tipo_servicio.lower() in tipo_servicios()):

                nuevas_ventas["tipo"] = tipo_servicio

                referencia = input("Ingrese la referencia del servicio: ")

                if(referencia in referencia_servicios(tipo_servicio)):
                    try:
                        nuevas_ventas["referencia_articulo"] = referencia
                    except Exception:
                        referencia_base = "xxxxxxx"
                        print("Referencia con mala ortografia (se asignara una referencia generica)")
                        nuevas_ventas["referencia_articulo"]= referencia_base

                    try:
                        nuevas_ventas["cantidad"] = int(input("Ingrese la cantidad: "))
                    except Exception:
                        cantidad_base = 0
                        print("Cantidad mal escrita (se le asignara una cantidad base)")
                        nuevas_ventas["cantidad"] = cantidad_base

                    try:
                        print("Ingrese la fecha de compra")
                        nuevas_ventas["fecha_compra"] = input("(ej. 01/10/1997) ")
                    except Exception:
                        fecha_compra_base = "01/01/2024"
                        print("Fecha de compra incorrecta (se le asignara una fecha generica)")
                        nuevas_ventas["fecha_compra"] =  fecha_compra_base
                    
                    nuevas_ventas["eliminado"] = estado
                    
                    datos["ventas"].append(nuevas_ventas)
                    guardar_datos(datos, RUTA_JSON)
                    print("")
                    print("Venta Registrada")
                else:
                    print(f"El servicio {referencia} no existe")
            else:
                print(f"El tipo de servicio {tipo_servicio} NO existe")
        else:
            print(f"La categoria {categoria} NO existe")
    else:
        print("El usuario no existe")

def actualizar_ventas():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["ventas"]))
    referencia = input("Ingrese la referencia: ")
    print("")
    for i in datos["ventas"]:
        if(i["referencia"] == referencia):

            documento = int(input("Ingrese el documento del cliente: "))

            if(documento in documentos_usuarios()):

                try:
                    i["documento_usuario"] = documento
                except ValueError:
                    documento_base = 00000
                    print("Documento mal escrito (se le asignara un documento base)")
                    i["documento_usuario"] = documento_base
                
                referencia = input("Ingrese la referencia del producto: ")

                if(referencia in referencia_productos()):
                    try:
                        i["referencia_producto"]= referencia
                    except Exception:
                        referencia_base = "xxxxxxx"
                        print("Referencia con mala ortografia (se asignara una referencia generica)")
                        i["referencia_producto"]= referencia_base

                    try:
                        i["cantidad"] = int(input("Ingrese la cantidad: "))
                    except Exception:
                        cantidad_base = 0
                        print("Cantidad mal escrita (se le asignara una cantidad base)")
                        i["cantidad"] = cantidad_base

                    try:
                        print("Ingrese la fecha de compra")
                        i["fecha_compra"] = input("(ej. 01/10/1997) ")
                    except Exception:
                        fecha_compra_base = "01/01/2024"
                        print("Fecha de compra incorrecta (se le asignara una fecha generica)")
                        i["fecha_compra"] =  fecha_compra_base
                    
                    guardar_datos(datos, RUTA_JSON)
                    print("")
                    print("Venta Actualizada")
                else:
                    print("El producto no existe")
            else:
                print("El usuario no existe")
        else:
            contador -= 1
    if(contador == 0):
        print("La venta no existe")

def leer_ventas():
    datos_json = cargar_datos(RUTA_JSON)
    contador_ventas = 0
    for i in datos_json["ventas"]:
        if(i["eliminado"] == False):
            contador_ventas += 1
            print("")
            print(f"Venta No. {contador_ventas}")
            print("")
            for llave, valor in i.items():
                if(llave != "id" and llave != "eliminado"):
                    print(llave.capitalize(), "=", valor)

def eliminar_ventas():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["ventas"]))
    referencia = input("Ingrese la referencia: ")
    print("")
    for i in datos["ventas"]:
        if(i["referencia"] == referencia):
            estado = input("Ingrese 1 para eliminar y 2 de lo contrario: ")
            print("")
            if(estado == "1"):
                i["eliminado"] = True
                print("Venta Eliminada")
                print("")
            elif(estado == "2"):
                i["eliminado"] = False
                print("Venta No Eliminada")
                print("")
            else:
                print("Seleccione un estado correcto (ej. 1)")
                print("")
            return guardar_datos(datos, RUTA_JSON)
        else:
            contador -= 1
    if(contador == 0):
        print("La venta no existe")
