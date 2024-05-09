from datos_usu import *

RUTA_JSON = "usuarios.json"

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



eliminar_usuario()