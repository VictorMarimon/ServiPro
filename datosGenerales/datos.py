import json

def cargar_datos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos
        
        

def guardar_datos(datos, archivo):
    datos = dict(datos)
    
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()
    
def leer_txt(archivo):
    with open(archivo, "r") as file:
        datos = file.read()
    return datos

def escribir_txt(datos, archivo):
    with open(archivo, "a") as file:
        file.write(datos + "\n")
    
