from datos_usu import *

RUTA_JSON = "usuarios.json"

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

    nuevos_usu["documento"] = int(input("Ingrese el documento: "))
    
    try:
        nuevos_usu["nombre"]= input("Ingrese el nombre: ")
    except Exception:
        nombre_base = "Usuario"
        print("Nombre con mala ortografia (se asignara un nombre generico)")
        nuevos_usu["nombre"]= nombre_base

    try:
        print("Ingrese la direcciòn")
        nuevos_usu["direccion"] = input("(ej. Carrera 24 #12 - 65) ")
    except Exception:
        direccion_base = "Direcciòn desconocida"
        print("Direccion mala ortografia (se le asignara direccion generica)")
        nuevos_usu["direccion"] = direccion_base

    try:
        nuevos_usu["telefono"] = int(input("Ingrese el telefono: "))
    except Exception:
        telefono_base = 0000000000
        print("Telefono mal escrito (se le asignara un telefono generico)")
        nuevos_usu["telefono"] = telefono_base
    
    try:
        print("Ingrese el correo electronico")
        nuevos_usu["email"] = input("(ej. daniel@gmail.com) ")
    except Exception:
        email_base = "none@none.com"
        print("Email incorrecto (se le asignara un email generico)")
        nuevos_usu["email"] = email_base

    try:
        print("Ingrese la fecha de nacimiento")
        nuevos_usu["nacimiento"] = input("(ej. 01/10/97) ")
    except Exception:
        fecha_nacimiento_base = "00/00/00"
        print("Fecha de nacimiento incorrecta (se le asignara una fecha generica)")
        nuevos_usu["nacimiento"] =  fecha_nacimiento_base

    try:
        print("Ingrese la fecha de afiliaciòn")
        nuevos_usu["fecha_afiliacion"] = input("(ej. 01/10/97) ")
    except Exception:
        fecha_afiliacion_base = "00/00/00"
        print("Fecha de afiliacion incorrecta (se le asignara una fecha generica)")
        nuevos_usu["fecha_afiliacion"] =  fecha_afiliacion_base

    try:
        nuevos_usu["servicios"] = input("Ingrese la cantidad de servicios: ")
    except Exception:
        servicios_base = 0
        print("Cantidad de servicios incorrecta (se le asignara un servicio generico)")
        nuevos_usu["servicios"] =  servicios_base
    
    nuevos_usu["eliminado"] = estado

    
    datos["usuarios"].append(nuevos_usu)
    guardar_datos(datos, RUTA_JSON)
    print("")
    print("Usuario Registrado")
        

crear_usuarios()