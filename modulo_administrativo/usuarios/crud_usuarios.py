import sys
import os

sys.path.append("..")

from datosGenerales.datos import *
from modulo_ventas.servicios_productos import compras_usuarios

#RUTAS
ruta_base = os.path.dirname(os.path.abspath(__file__))
RUTA_JSON = os.path.join(ruta_base,  "usuarios.json")

def crear_usuarios():
    datos = cargar_datos(RUTA_JSON)
    nuevos_usu = {}
    print(" ")
    print(" AGREGAR USUARIOS ")
    print(" ")

    cantidad_usuarios = int(len(datos["usuarios"]))
    estado = False

    for i in range(0, cantidad_usuarios):
        cantidad_usuarios += 1

    nuevos_usu["id"] = int(cantidad_usuarios)

    documentos_registrados = []

    for i in datos["usuarios"]:
        documentos_registrados.append(i["documento"])
    
    
    while True:
        try:
            documento = int(input("Ingrese el documento: "))
            break  
        except ValueError:
            print("Por favor, ingrese un número válido para el documento.")    

    while True:
        if(documento in documentos_registrados):
            print(f"El documento {documento} ya está registrado.")
            try:
                documento = int(input("Ingrese el documento: "))
            except ValueError:
                print("Por favor, ingrese un número válido para el documento.") 
        else:     
            nuevos_usu["documento"] = documento
            break

    try:
        nombre = input("Ingrese el nombre: ")
        if not nombre:
            print("El nombre no puede estar vacío")
            nuevos_usu["nombre"] = "Usuario"
        else:
            nuevos_usu["nombre"] = nombre
    except Exception:
        nombre_base = "Usuario"
        print("Error. Se asignará un nombre genérico.")
        nuevos_usu["nombre"] = nombre_base

    try:
        print("Ingrese la dirección:")
        direccion = input("(ej. Carrera 24 #12 - 65) ")

        if not direccion.replace(' ', '').replace('-', '').replace('#', '').replace('.', '').isalnum():
            print("La dirección contiene caracteres no válidos (Se asignará una dirección genérica).")
            nuevos_usu["direccion"] = "Dirección desconocida"
        else:
            nuevos_usu["direccion"] = direccion
    except ValueError:
        direccion_base = "Dirección desconocida"
        print("Error. Se asignará una dirección genérica:", direccion_base)
        nuevos_usu["direccion"] = direccion_base

    try:
        telefono = int(input("Ingrese el telefono: "))
        i["telefono"] = telefono
    except ValueError:
        telefono_base = 0000000000
        print("Telefono mal escrito (se le asignara un telefono generico)")
        nuevos_usu["telefono"] = telefono_base

    try:
        print("Por favor, ingrese su correo electrónico:")
        email = input("(por ejemplo, daniel@gmail.com): ")
        if "@" not in email or "." not in email:
            print("El correo electrónico debe contener un '@' y un '.' (Se le asignará un correo electrónico genérico)")
            nuevos_usu["email"] = "none@none.com"
        else:
            nuevos_usu["email"] = email
    except ValueError :
        print(f"Error. Se le asignará un correo electrónico genérico.")
        nuevos_usu["email"] = "none@none.com"

    try:
        print("Por favor ingrese su fecha de nacimiento (ej. 01/10/1997): ")
        fecha_nacimiento = input()
        if len(fecha_nacimiento) != 10 or fecha_nacimiento[2] != '/' or fecha_nacimiento[5] != '/':
            print("La fecha de nacimiento no cumple el formato (se asignará una fecha genérica.)")
            nuevos_usu["nacimiento"] = "01/01/2001"
        else:
            nuevos_usu["nacimiento"] = fecha_nacimiento
    except ValueError:
        fecha_nacimiento_base = "01/01/2001"
        print("La fecha de nacimiento ingresada no es válida (se asignará una fecha genérica.)")
        nuevos_usu["nacimiento"] = fecha_nacimiento_base

    try:
        print("Ingrese la fecha de afiliación (ej. 01/10/2020):")
        fecha_afiliacion = input()
        if len(fecha_afiliacion) != 10 or fecha_afiliacion[2] != '/' or fecha_afiliacion[5] != '/':
            print("La fecha de afiliación no cumple el formato (se asignará una fecha genérica.)")
            nuevos_usu["fecha_afiliacion"] = "01/01/2024"
        else:
            nuevos_usu["fecha_afiliacion"] = fecha_afiliacion
    except ValueError:
        fecha_afiliacion_base = "01/01/2024"
        print("Fecha de afiliacion ingresada no es válida, se asignará una fecha genérica.")
        nuevos_usu["fecha_afiliacion"] =  fecha_afiliacion_base

    nuevos_usu["servicios"] = 0

    nuevos_usu["eliminado"] = estado


    datos["usuarios"].append(nuevos_usu)
    guardar_datos(datos, RUTA_JSON)
    print("")
    print("Usuario Registrado")

def actualizar_usuarios():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["usuarios"]))
    documento = int(input("Ingrese el nùmero de documento: "))
    print("")
    for i in datos["usuarios"]:
        if(i["documento"] == documento and i["eliminado"] == False):
            try:
                nombre = input("Ingrese el nombre: ")
                if not nombre:
                    print("El nombre no puede estar vacío (Se asignará un nombre genérico.)")
                    i["nombre"] = "Usuario"
                else:
                    i["nombre"] = nombre
            except Exception:
                nombre_base = "Usuario"
                print("Error. Se asignará un nombre genérico.")
                i["nombre"] = nombre_base

            try:
                print("Ingrese la dirección:")
                direccion = input("(ej. Carrera 24 #12 - 65) ")

                if not direccion.replace(' ', '').replace('-', '').replace('#', '').replace('.', '').isalnum():
                    print("La dirección contiene caracteres no válidos o está vacia (Se asignará una dirección genérica).")
                    i["direccion"] = "Dirección desconocida"
                else:
                    i["direccion"] = direccion
            except ValueError:
                direccion_base = "Dirección desconocida"
                print("Error. Se asignará una dirección genérica:", direccion_base)
                i["direccion"] = direccion_base

            try:
                telefono = int(input("Ingrese el telefono: "))
                i["telefono"] = telefono
            except ValueError:
                telefono_base = 0000000000
                print("Telefono mal escrito (se le asignara un telefono generico)")
                i["telefono"] = telefono_base
            
            try:
                print("Por favor, ingrese su correo electrónico:")
                email = input("(por ejemplo, daniel@gmail.com): ")
                if "@" not in email or "." not in email:
                    print("El correo electrónico debe contener un '@' y un '.' (Se le asignará un correo electrónico genérico)")
                    i["email"] = "none@none.com"
                else:
                    i["email"] = email
            except ValueError :
                print(f"Error. Se le asignará un correo electrónico genérico.")
                i["email"] = "none@none.com"

            try:
                print("Por favor ingrese su fecha de nacimiento (ej. 01/10/1997): ")
                fecha_nacimiento = input()
                if len(fecha_nacimiento) != 10 or fecha_nacimiento[2] != '/' or fecha_nacimiento[5] != '/':
                    print("La fecha de nacimiento no cumple el formato (se asignará una fecha genérica.)")
                    i["nacimiento"] = "01/01/2001"
                else:
                    i["nacimiento"] = fecha_nacimiento
            except ValueError:
                fecha_nacimiento_base = "01/01/2001"
                print("La fecha de nacimiento ingresada no es válida (se asignará una fecha genérica.)")
                i["nacimiento"] = fecha_nacimiento_base

            try:
                print("Ingrese la fecha de afiliación (ej. 01/10/2020):")
                fecha_afiliacion = input()
                if len(fecha_afiliacion) != 10 or fecha_afiliacion[2] != '/' or fecha_afiliacion[5] != '/':
                    print("La fecha de afiliación no cumple el formato (se asignará una fecha genérica.)")
                    i["fecha_afiliacion"] = "01/01/2024"
                else:
                    i["fecha_afiliacion"] = fecha_afiliacion
            except ValueError:
                fecha_afiliacion_base = "01/01/2024"
                print("Fecha de afiliacion ingresada no es válida, se asignará una fecha genérica.")
                i["fecha_afiliacion"] =  fecha_afiliacion_base

            datos_compras = compras_usuarios()
            contador_datos_compras = 0
            for k in datos_compras:
                if(k["documento_usuario"] == documento):
                    contador_datos_compras += 1
                    i["servicios"] = k["cantidad_servicios"]
            
            if(contador_datos_compras == 0):
                servicios_base = 0
                i["servicios"] =  servicios_base
            print("")
            print("Usuario Actualizado")    
            return guardar_datos(datos, RUTA_JSON)
        else:
            contador -= 1
    if(contador == 0):
        print("El usuario no existe")

def leer_usuarios():
    datos_json = cargar_datos(RUTA_JSON)
    contador_usuario = 0
    for i in datos_json["usuarios"]:
        if(i["eliminado"] == False):
            contador_usuario += 1
            print("")
            print(f"Usuario No. {contador_usuario}")
            print("")
            for llave, valor in i.items():
                if(llave != "id" and llave != "eliminado"):
                    print(llave.capitalize(), "=", valor)
    
    if(contador_usuario == 0):
        print("No se han registrado usuarios")

def eliminar_usuario():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["usuarios"]))
    documento = int(input("Ingrese el documento del usuario: "))
    print("")
    for i in datos["usuarios"]:
        if(i["documento"] == documento):
            estado = input("Ingrese 1 para eliminar y 2 de lo contrario: ")
            print("")
            if(estado == "1"):
                i["eliminado"] = True
                print("Usuario Eliminado")
                print("")
            elif(estado == "2"):
                i["eliminado"] = False
                print("Usuario No Eliminado")
                print("")
            else:
                print("Seleccione un estado correcto (ej. 1)")
                print("")
            
            return guardar_datos(datos, RUTA_JSON)
        else:
            contador -= 1
    if(contador == 0):
        print("El usuario no existe")
