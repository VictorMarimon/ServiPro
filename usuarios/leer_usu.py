from datos_usu import *

RUTA_JSON = "usuarios.json"

def leer_usuarios():
    datos_json = cargar_datos(RUTA_JSON)
    contador_usuario = 0
    for i in datos_json["usuarios"]:
        contador_usuario += 1
        print("")
        print(f"Usuario No. {contador_usuario}")
        print("")
        for llave, valor in i.items():
            print(llave.capitalize(), "=", valor)
        

leer_usuarios()