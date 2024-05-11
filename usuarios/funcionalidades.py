import sys

sys.path.append("..")


from datosGenerales.datos import *
from usuarios.consultas_usuarios import fecha_afiliacion

RUTA_JSON = "usuarios.json"

def nuevos_usuarios():
    año_actual = 2024
    documento = int(input("Ingrese el documento: "))
    print("")

    fecha = fecha_afiliacion(documento)
    if(fecha):
        if((año_actual - int(fecha[6:10])) <= 2):
            return f"El cliente es nuevo, se afilio el {fecha}"
        else:
            return "El cliente NO es nuevo"
    else:
        return("El usuario no existe o està eliminado")
    
    



