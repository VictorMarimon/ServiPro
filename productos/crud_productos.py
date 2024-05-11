import sys

sys.path.append("..")

from datosGenerales.datos import *

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/productos/productos.json"

def crear_productos():
    datos = cargar_datos(RUTA_JSON)
    nuevos_productos = {}
    print(" ")
    print(" AGREGAR PRODUCTOS ")
    print(" ")

    cantidad_productos = int(len(datos["productos"][0]["telefonos"]))
    estado = False

    for i in range(0, cantidad_productos):
        cantidad_productos += 1

    nuevos_productos["id"] = int(cantidad_productos)

    nuevos_productos["referencia"] = input("Ingrese la referencia: ")
    
    try:
        nuevos_productos["nombre"]= input("Ingrese el nombre: ")
    except Exception:
        nombre_base = "xxxxxxx"
        print("Nombre con mala ortografia (se asignara un nombre generico)")
        nuevos_productos["nombre"]= nombre_base

    try:
        nuevos_productos["precio"] = int(input("Ingrese el precio: "))
    except Exception:
        precio_base = 0
        print("Precio mal escrito (se le asignara un precio base)")
        nuevos_productos["precio"] = precio_base

    try:
        print("Ingrese la fecha de creaciòn")
        nuevos_productos["fecha_creacion"] = input("(ej. 01/10/1997) ")
    except Exception:
        fecha_creacion_base = "01/01/2024"
        print("Fecha de nacimiento incorrecta (se le asignara una fecha generica)")
        nuevos_productos["fecha_creacion"] =  fecha_creacion_base
    
    nuevos_productos["eliminado"] = estado

    
    datos["productos"][0]["telefonos"].append(nuevos_productos)
    guardar_datos(datos, RUTA_JSON)
    print("")
    print("Producto Registrado")

def actualizar_productos():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["productos"][0]["telefonos"]))
    referencia = input("Ingrese la referencia: ")
    print("")
    for i in datos["productos"][0]["telefonos"]:
        if(i["referencia"] == referencia and i["eliminado"] == False):

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

def leer_productos():
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

    if(contador_servicios == 0):
        print("No se han registrado productos")

def eliminar_productos():
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

