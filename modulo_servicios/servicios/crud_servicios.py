import sys

sys.path.append("..")

from datosGenerales.datos import *

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_servicios/servicios/servicios.json"

def crear_servicios():
    datos = cargar_datos(RUTA_JSON)
    nuevos_servicio = {}
    print(" ")
    print(" AGREGAR SERVICIOS ")
    print(" ")

    cantidad_servicios = int(len(datos["servicios"][0]["internet"]))
    estado = False

    

    for i in range(0, cantidad_servicios):
        cantidad_servicios += 1

    nuevos_servicio["id"] = int(cantidad_servicios)

    try:
        nuevos_servicio["referencia"] = input("Ingrese la referencia: ")
    except Exception:
        referencia_base = "RF0"
        print("Referencia con mala ortografia (se asignara una referencia generica)")
        nuevos_servicio["referencia"]= referencia_base
    
    try:
        nombre = input("Ingrese el nombre: ")
        if not nombre:
            print("El nombre no puede estar vacío (se asignara un nombre generico)")
            nuevos_servicio["nombre"] = "xxxxxxx"
        else:
            nuevos_servicio["nombre"] = nombre
    except Exception:
        nombre_base = "xxxxxxx"
        print("Nombre con mala ortografia (se asignara un nombre generico)")
        nuevos_servicio["nombre"]= nombre_base

    try:
        precio = int(input("Ingrese el precio: "))
        if precio < 0:
            print("El precio no puede ser negativo (se le asignará un precio base)")
            nuevos_servicio["precio"] = 0
        else:
            nuevos_servicio["precio"] = precio
    except ValueError:
        precio_base = 0
        print("El precio ingresado no es válido (se le asignará un precio base)")
        nuevos_servicio["precio"] = precio_base

    try:
        print("Ingrese la fecha de creación (ej. 01/10/2020):")
        fecha_creacion = input()
        if len(fecha_creacion) != 10 or fecha_creacion[2] != '/' or fecha_creacion[5] != '/':
            print("La fecha de creación no cumple el formato (se asignará una fecha genérica.)")
            nuevos_servicio["fecha_creacion"] = "01/01/2024"
        else:
            nuevos_servicio["fecha_creacion"] = fecha_creacion
    except ValueError:
        fecha_creacion_base = "01/01/2024"
        print("Fecha de nacimiento incorrecta (se le asignara una fecha generica)")
        nuevos_servicio["fecha_creacion"] =  fecha_creacion_base
    
    nuevos_servicio["eliminado"] = estado

    
    datos["servicios"][0]["internet"].append(nuevos_servicio)
    guardar_datos(datos, RUTA_JSON)
    print("")
    print("Servicio Registrado")

def actualizar_servicios():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["servicios"][0]["telefonia"]))
    referencia = input("Ingrese la referencia: ")
    print("")
    for i in datos["servicios"][0]["telefonia"]:
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
        print("El servicio no existe")

def leer_servicios():
    datos_json = cargar_datos(RUTA_JSON)
    contador_servicios = 0
    for i in datos_json["servicios"][0]["telefonia"]:
        if(i["eliminado"] == False):
            contador_servicios += 1
            print("")
            print(f"Servicio No. {contador_servicios}")
            print("")
            for llave, valor in i.items():
                if(llave != "id" and llave != "eliminado"):
                    print(llave.capitalize(), "=", valor)
    if(contador_servicios == 0):
        print("No se han registrado servicios")

def eliminar_servicios():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["servicios"][0]["telefonia"]))
    referencia = input("Ingrese la referencia: ")
    print("")
    for i in datos["servicios"][0]["telefonia"]:
        if(i["referencia"] == referencia):
            estado = input("Ingrese 1 para eliminar y 2 de lo contrario: ")
            print("")
            if(estado == "1"):
                i["eliminado"] = True
                print("Servicio Eliminado")
                print("")
            elif(estado == "2"):
                i["eliminado"] = False
                print("Servicio No Eliminado")
                print("")
            else:
                print("Seleccione un estado correcto (ej. 1)")
                print("")
            return guardar_datos(datos, RUTA_JSON)
        else:
            contador -= 1
    if(contador == 0):
        print("El servicio no existe")
