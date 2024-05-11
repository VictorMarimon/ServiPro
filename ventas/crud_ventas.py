import sys

sys.path.append("..")

from datosGenerales.datos import *
from usuarios.consultas_usuarios import documentos_usuarios
from servicios.consultas_servicios import referencia_servicios
from productos.consultas_productos import referencia_productos

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/ventas/ventas.json"

def crear_ventas():
    datos = cargar_datos(RUTA_JSON)
    nuevas_ventas = {}
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
        
        referencia = input("Ingrese la referencia del producto: ")

        if(referencia in referencia_productos()):
            try:
                nuevas_ventas["referencia_producto"]= referencia
            except Exception:
                referencia_base = "xxxxxxx"
                print("Referencia con mala ortografia (se asignara una referencia generica)")
                nuevas_ventas["referencia_producto"]= referencia_base

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
            print("El producto no existe")
    else:
        print("El usuario no existe")

def actualizar_ventas():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["productos"][0]["telefonos"]))
    referencia = input("Ingrese la referencia: ")
    print("")
    for i in datos["productos"][0]["telefonos"]:
        if(i["referencia"] == referencia):

            try:
                i["referencia"]= input("Ingrese la referencia: ")
            except Exception:
                referencia_base = "RF0"
                print("Referencia con mala ortografia (se asignara una referencia generica)")
                i["referencia"]= referencia_base

            try:
                i["nombre"]= input("Ingrese el nombre: ")
            except Exception:
                nombre_base = "Servicio"
                print("Nombre con mala ortografia (se asignara un nombre generico)")
                i["nombre"]= nombre_base

            try:
                i["precio"] = int(input("Ingrese el precio: "))
            except Exception:
                precio_base = 0
                print("Precio mal escrito (se le asignara un precio base)")
                i["precio"] = precio_base

            try:
                print("Ingrese la fecha de creaciòn")
                i["fecha_creacion"] = input("(ej. 01/10/1997) ")
            except Exception:
                fecha_creacion_base = "01/01/2024"
                print("Fecha de nacimiento incorrecta (se le asignara una fecha generica)")
                i["fecha_creacion"] =  fecha_creacion_base
            print("Producto Actualizado")
            return guardar_datos(datos, RUTA_JSON)
        else:
            contador -= 1
    if(contador == 0):
        print("El producto no existe")

def leer_ventas():
    datos_json = cargar_datos(RUTA_JSON)
    contador_servicios = 0
    for i in datos_json["productos"][0]["telefonos"]:
        if(i["eliminado"] == False):
            contador_servicios += 1
            print("")
            print(f"Producto No. {contador_servicios}")
            print("")
            for llave, valor in i.items():
                if(llave != "id" and llave != "eliminado"):
                    print(llave.capitalize(), "=", valor)

def eliminar_ventas():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["productos"][0]["telefonos"]))
    referencia = input("Ingrese la referencia: ")
    print("")
    for i in datos["productos"][0]["telefonos"]:
        if(i["referencia"] == referencia):
            estado = input("Ingrese 1 para eliminar y 2 de lo contrario: ")
            print("")
            if(estado == "1"):
                i["eliminado"] = True
                print("Producto Eliminado")
                print("")
            elif(estado == "2"):
                i["eliminado"] = False
                print("Producto No Eliminado")
                print("")
            else:
                print("Seleccione un estado correcto (ej. 1)")
                print("")
            return guardar_datos(datos, RUTA_JSON)
        else:
            contador -= 1
    if(contador == 0):
        print("El producto no existe")
