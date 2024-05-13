import sys

sys.path.append("..")


from datosGenerales.datos import *
from modulo_administrativo.usuarios.consultas_usuarios import fecha_afiliacion
from modulo_ventas.servicios_productos import compras_usuarios

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_administrativo/usuarios/usuarios.json"

def nuevos_usuarios():
    año_actual = 2024
    print("")
    documento = int(input("Ingrese el documento: "))
    print("")

    fecha = fecha_afiliacion(documento)
    if(fecha):
        if((año_actual - int(fecha[6:10])) <= 2):
            print(f"El cliente es nuevo, se afilio el {fecha}")
            print("")
        else:
            print(f"El cliente NO es nuevo se afilio el {fecha}")
            print("")
    else:
        print("El usuario no existe o està eliminado")
        print("")
    
def usuarios_regulares_leales():
    datos = cargar_datos(RUTA_JSON)
    clientes_categorizados = []
    for i in datos["usuarios"]:
        fecha = i["fecha_afiliacion"]
        if((2024 - int(fecha[6:10])) > 5 and i["servicios"] >= 4):
            clientes = {}
            clientes["documento"] = i["documento"]
            clientes["nombre"] = i["nombre"]
            clientes["categoria"] = "LEAL"
            clientes_categorizados.append(clientes)
        elif((2024 - int(fecha[6:10])) <= 5 and i["servicios"] >= 4):
            clientes = {}
            clientes["documento"] = i["documento"]
            clientes["nombre"] = i["nombre"]
            clientes["categoria"] = "REGULAR"
            clientes_categorizados.append(clientes)
    for k in clientes_categorizados:
        if(k["categoria"] == "LEAL"):
            print(f"El usuario {k["nombre"]} identificado con {k["documento"]} es cliente LEAL")
        elif(k["categoria"] == "REGULAR"):
            print(f"El usuario {k["nombre"]} identificado con {k["documento"]} es cliente REGULAR")
            
    
    



