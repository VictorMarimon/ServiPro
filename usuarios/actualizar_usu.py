from datos_usu import *

RUTA_JSON = "usuarios.json"

def actualizar_usuarios():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["usuarios"]))
    documento = int(input("Ingrese el nùmero de documento: "))
    print("")
    for i in datos["usuarios"]:
        if(i["documento"] == documento):
            try:
                i["nombre"]= input("Ingrese el nombre: ")
            except Exception:
                nombre_base = "Usuario"
                print("Nombre con mala ortografia (se asignara un nombre generico)")
                i["nombre"]= nombre_base

            try:
                print("Ingrese la direcciòn")
                i["direccion"] = input("(ej. Carrera 24 #12 - 65) ")
            except Exception:
                direccion_base = "Direcciòn desconocida"
                print("Direccion mala ortografia (se le asignara direccion generica)")
                i["direccion"] = direccion_base

            try:
                i["telefono"] = int(input("Ingrese el telefono: "))
            except Exception:
                telefono_base = 0000000000
                print("Telefono mal escrito (se le asignara un telefono generico)")
                i["telefono"] = telefono_base
            
            try:
                print("Ingrese el correo electronico")
                i["email"] = input("(ej. daniel@gmail.com) ")
            except Exception:
                email_base = "none@none.com"
                print("Email incorrecto (se le asignara un email generico)")
                i["email"] = email_base

            try:
                print("Ingrese la fecha de nacimiento")
                i["nacimiento"] = input("(ej. 01/10/97) ")
            except Exception:
                fecha_nacimiento_base = "00/00/00"
                print("Fecha de nacimiento incorrecta (se le asignara una fecha generica)")
                i["nacimiento"] =  fecha_nacimiento_base

            try:
                print("Ingrese la fecha de afiliaciòn")
                i["fecha_afiliacion"] = input("(ej. 01/10/97) ")
            except Exception:
                fecha_afiliacion_base = "00/00/00"
                print("Fecha de afiliacion incorrecta (se le asignara una fecha generica)")
                i["fecha_afiliacion"] =  fecha_afiliacion_base

            try:
                i["servicios"] = input("Ingrese la cantidad de servicios: ")
            except Exception:
                servicios_base = 0
                print("Cantidad de servicios incorrecta (se le asignara un servicio generico)")
                i["servicios"] =  servicios_base
                
            return guardar_datos(datos, RUTA_JSON)
    else:
        contador -= 1
    if(contador == 0):
        print("El usuario no existe")
    else:
        print("Usuario Actualizado")
            


    
        

print(actualizar_usuarios())