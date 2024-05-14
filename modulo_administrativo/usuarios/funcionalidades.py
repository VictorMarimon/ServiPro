import sys

sys.path.append("..")


from datosGenerales.datos import *
from modulo_administrativo.usuarios.consultas_usuarios import fecha_afiliacion
from modulo_ventas.servicios_productos import compras_usuarios

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_administrativo/usuarios/usuarios.json"
RUTA_JSON_VENTAS = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_ventas/ventas.json"
RUTA_JSON_PRODUCTOS = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_servicios/productos/productos.json"
RUTA_JSON_SERVICIOS = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_servicios/servicios/servicios.json"

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
            
def ofertas_productos(categoria):
    datos_clientes = cargar_datos(RUTA_JSON)
    datos_ventas = cargar_datos(RUTA_JSON_VENTAS)
    datos_productos = cargar_datos(RUTA_JSON_PRODUCTOS)

    contador_productos = 0
    contador_usuarios = 0
    contador_promo = 0

    precio = 0
    cantidad = 0
    total = 0

    monto_cliente = 0
    monto_minimo = 2000000
    for i in datos_clientes["usuarios"]:
        for j in datos_ventas["ventas"]:
            if(i["documento"] == j["documento_usuario"]):
                contador_usuarios += 1
                for k in datos_productos["productos"][0][categoria]:
                    if(j["referencia_articulo"] == k["referencia"]):
                        contador_productos += 1
                        precio = k["precio"]
                        cantidad = j["cantidad"]
                        total = (precio * cantidad) 
                        monto_cliente += total
                        if(monto_cliente > monto_minimo):
                            contador_promo += 1
                            print("")
                            print(f"CUPON {str(categoria).upper()}")
                            print("")
                            print(f"El usuario {i["nombre"]} tiene un descuento del 15% en cualquier producto")
                            print("Solo aplica para la tienda virtual")
                            print("")
        precio = 0
        cantidad = 0
        total = 0
        monto_cliente = 0

    if(contador_usuarios == 0):
        print("No hay usuarios compradores")
    elif(contador_productos == 0):
        print(f"No se han comprado {categoria}")
    elif(contador_promo == 0):
        print("No aplican promociones")

def ofertas_servicios(categoria):
    datos_clientes = cargar_datos(RUTA_JSON)
    datos_ventas = cargar_datos(RUTA_JSON_VENTAS)
    datos_servicios = cargar_datos(RUTA_JSON_SERVICIOS)

    contador_servicios = 0
    contador_usuarios = 0
    contador_promo = 0

    precio = 0
    cantidad = 0
    total = 0

    monto_cliente = 0
    monto_minimo = 250000
    for i in datos_clientes["usuarios"]:
        for j in datos_ventas["ventas"]:
            if(i["documento"] == j["documento_usuario"]):
                contador_usuarios += 1
                for k in datos_servicios["servicios"][0][categoria]:
                    if(j["referencia_articulo"] == k["referencia"]):
                        contador_servicios += 1
                        precio = k["precio"]
                        cantidad = j["cantidad"]
                        total = (precio * cantidad) 
                        monto_cliente += total
                        if(monto_cliente > monto_minimo):
                            contador_promo += 1
                            print("")
                            print(f"El usuario {i["nombre"]} tiene un descuento del 15% en cualquier servicio")
                            print("Solo aplica para la tienda virtual")
                            print("")
                            break
        precio = 0
        cantidad = 0
        total = 0
        monto_cliente = 0

    if(contador_usuarios == 0):
        print("No hay usuarios compradores")
    elif(contador_servicios == 0):
        print(f"No se han comprado {categoria}")
    elif(contador_promo == 0):
        print("No aplican promociones")    



