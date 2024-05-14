import sys

sys.path.append("..")

from datosGenerales.datos import *

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_servicios/productos/productos.json"

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

    try:
        nuevos_productos["referencia"] = input("Ingrese la referencia: ")
    except Exception:
        referencia_base = "RF0"
        print("Referencia con mala ortografia (se asignara una referencia generica)")
        nuevos_productos["referencia"]= referencia_base
    
    try:
        nombre = input("Ingrese el nombre: ")
        if not nombre:
            print("El nombre no puede estar vacío (se asignara un nombre generico)")
            nuevos_productos["nombre"] = "xxxxxxx"
        else:
            nuevos_productos["nombre"] = nombre
    except Exception:
        nombre_base = "xxxxxxx"
        print("Nombre con mala ortografia (se asignara un nombre generico)")
        nuevos_productos["nombre"]= nombre_base

    try:
        precio = int(input("Ingrese el precio: "))
        if precio < 0:
            print("El precio no puede ser negativo (se le asignará un precio base)")
            nuevos_productos["precio"] = 0
        else:
            nuevos_productos["precio"] = precio
    except ValueError:
        precio_base = 0
        print("El precio ingresado no es válido (se le asignará un precio base)")
        nuevos_productos["precio"] = precio_base

    try:
        print("Ingrese la fecha de creación (ej. 01/10/2020):")
        fecha_creacion = input()
        if len(fecha_creacion) != 10 or fecha_creacion[2] != '/' or fecha_creacion[5] != '/':
            print("La fecha de creación no cumple el formato (se asignará una fecha genérica.)")
            nuevos_productos["fecha_creacion"] = "01/01/2024"
        else:
            nuevos_productos["fecha_creacion"] = fecha_creacion
    except ValueError:
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
                i["referencia"] = input("Ingrese la referencia: ")
            except Exception:
                referencia_base = "RF0"
                print("Referencia con mala ortografia (se asignara una referencia generica)")
                i["referencia"]= referencia_base

            try:
                nombre = input("Ingrese el nombre: ")
                if not nombre:
                    print("El nombre no puede estar vacío (se asignara un nombre generico)")
                    i["nombre"] = "xxxxxxx"
                else:
                    i["nombre"] = nombre
            except Exception:
                nombre_base = "xxxxxxx"
                print("Nombre con mala ortografia (se asignara un nombre generico)")
                i["nombre"]= nombre_base

            try:
                precio = int(input("Ingrese el precio: "))
                if precio < 0:
                    print("El precio no puede ser negativo (se le asignará un precio base)")
                    i["precio"] = 0
                else:
                    i["precio"] = precio
            except ValueError:
                precio_base = 0
                print("El precio ingresado no es válido (se le asignará un precio base)")
                i["precio"] = precio_base

            try:
                print("Ingrese la fecha de creación (ej. 01/10/2020):")
                fecha_creacion = input()
                if len(fecha_creacion) != 10 or fecha_creacion[2] != '/' or fecha_creacion[5] != '/':
                    print("La fecha de creación no cumple el formato (se asignará una fecha genérica.)")
                    i["fecha_creacion"] = "01/01/2024"
                else:
                    i["fecha_creacion"] = fecha_creacion
            except ValueError:
                fecha_creacion_base = "01/01/2024"
                print("Fecha de nacimiento incorrecta (se le asignara una fecha generica)")
                i["fecha_creacion"] =  fecha_creacion_base
            return guardar_datos(datos, RUTA_JSON)
        else:
            contador -= 1
    if(contador == 0):
        print("El producto no existe")

def leer_productos():
    datos_json = cargar_datos(RUTA_JSON)
    contador_productos = 0
    for i in datos_json["productos"][0]["telefonos"]:
        if(i["eliminado"] == False):
            contador_productos += 1
            print("")
            print(f"Producto No. {contador_productos}")
            print("")
            for llave, valor in i.items():
                if(llave != "id" and llave != "eliminado"):
                    print(llave.capitalize(), "=", valor)

    if(contador_productos == 0):
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

