import sys

sys.path.append("..")

from datosGenerales.datos import *
from modulo_administrativo.usuarios.consultas_usuarios import documentos_usuarios
from modulo_servicios.servicios.consultas_servicios import *
from modulo_servicios.productos.consultas_productos import *

RUTA_JSON = "C:/Users/PC/Desktop/Proyecto---Campus/modulo_ventas/ventas.json"

def crear_ventas(categoria):
    datos = cargar_datos(RUTA_JSON)
    nuevas_ventas = {}

    print(" ")
    print(" AGREGAR VENTAS ")
    print(" ")

    cantidad_ventas = int(len(datos["ventas"]))
    estado = False

    ventas_registradas = []

    for i in datos["ventas"]:
        ventas_registradas.append(i["referencia"])

    for i in range(0, cantidad_ventas):
        cantidad_ventas += 1

    nuevas_ventas["id"] = int(cantidad_ventas)

    referencia = input("Ingrese la referencia: ")

    while True:
        if(referencia in ventas_registradas):
            print(f"La referencia {referencia} ya existe")
            try:
                referencia = input("Ingrese la referencia: ")
            except Exception:
                referencia_base = f"RF0{str(cantidad_ventas)}"
                print("Referencia con mala ortografia (se asignara una referencia generica)")
                nuevas_ventas["referencia"]= referencia_base
        else:
            nuevas_ventas["referencia"] = referencia
            break

    nuevas_ventas["referencia"] = input("Ingrese la referencia: ")

    documento = 0
    while True:
        try:
            documento = int(input("Ingrese el documento: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el documento.")

    if(documento in documentos_usuarios()):

        nuevas_ventas["documento_usuario"] = documento
        
        if(categoria == "productos"):

            nuevas_ventas["categoria"] = "productos"

            tipo_producto = input("Ingrese el tipo de producto: ")

            if(tipo_producto.lower() in tipo_productos()):

                nuevas_ventas["tipo"] = tipo_producto

                referencia = input("Ingrese la referencia del producto: ")

                if(referencia in referencia_productos(tipo_producto)):
                    while True:
                        try:
                            referencia = input("Por favor ingresa la referencia del artículo: ")
                            break
                        except Exception:
                            print("Por favor, ingrese una referencia válida")

                    nuevas_ventas["referencia_articulo"] = referencia

                    while True:
                        try:
                            cantidad = int(input("Ingrese la cantidad: "))
                            if(cantidad > 0):
                                break  
                        except ValueError:
                            print("Error: Debe ingresar un número entero.")

                    nuevas_ventas["cantidad"] = cantidad

                    while True:
                        try:
                            print("Ingrese la fecha de compra (ej. 01/10/1997): ")
                            fecha_compra = input()
                            if len(fecha_compra) != 10 or fecha_compra[2] != '/' or fecha_compra[5] != '/':
                                print("Formato de fecha incorrecto. Se asignará una fecha genérica")
                                nuevas_ventas["fecha_compra"] = "01/01/2024"
                            else: 
                                nuevas_ventas["fecha_compra"] = fecha_compra
                            break  
                        except ValueError:
                            fecha_compra_base = "01/01/2024"
                            print("Formato de fecha incorrecto. Se asignará una fecha genérica (01/01/2024).")
                            nuevas_ventas["fecha_compra"] = fecha_compra_base
                            break 
                    
                    nuevas_ventas["eliminado"] = estado
                    
                    datos["ventas"].append(nuevas_ventas)
                    guardar_datos(datos, RUTA_JSON)
                    print("")
                    print("Venta Registrada")
                else:
                    print(f"El producto {referencia} no existe")
            else:
                print(f"El tipo de producto {tipo_producto} NO existe")
        elif(categoria == "servicios"):
            nuevas_ventas["categoria"] = "servicios"

            tipo_servicio = input("Ingrese el tipo de servicio: ")

            if(tipo_servicio.lower() in tipo_servicios()):

                nuevas_ventas["tipo"] = tipo_servicio

                referencia = input("Ingrese la referencia del servicio: ")

                if(referencia in referencia_servicios(tipo_servicio)):
                    while True:
                        try:
                            referencia = input("Por favor ingresa la referencia del artículo: ")
                            break
                        except Exception:
                            print("Por favor, ingrese una referencia válida")

                    nuevas_ventas["referencia_articulo"] = referencia

                    while True:
                        try:
                            cantidad = int(input("Ingrese la cantidad: "))
                            if(cantidad > 0):
                                break  
                        except ValueError:
                            print("Error: Debe ingresar un número entero.")

                    nuevas_ventas["cantidad"] = cantidad

                    while True:
                        try:
                            print("Ingrese la fecha de compra (ej. 01/10/1997): ")
                            fecha_compra = input()
                            if len(fecha_compra) != 10 or fecha_compra[2] != '/' or fecha_compra[5] != '/':
                                print("Formato de fecha incorrecto. Se asignará una fecha genérica")
                                nuevas_ventas["fecha_compra"] = "01/01/2024"
                            else:
                                nuevas_ventas["fecha_compra"] = fecha_compra
                            break  
                        except ValueError:
                            fecha_compra_base = "01/01/2024"
                            print("Formato de fecha incorrecto. Se asignará una fecha genérica (01/01/2024).")
                            nuevas_ventas["fecha_compra"] = fecha_compra_base
                            break 
                    
                    nuevas_ventas["eliminado"] = estado
                    
                    datos["ventas"].append(nuevas_ventas)
                    guardar_datos(datos, RUTA_JSON)
                    print("")
                    print("Venta Registrada")
                else:
                    print(f"El servicio {referencia} no existe")
            else:
                print(f"El tipo de servicio {tipo_servicio} NO existe")
        else:
            print(f"La categoria {categoria} NO existe")
    else:
        print("El usuario no existe")

def actualizar_ventas(categoria):
    datos = cargar_datos(RUTA_JSON)

    ventas_registradas = []

    for i in datos["ventas"]:
        ventas_registradas.append(i["referencia"])

    contador = int(len(datos["ventas"]))
    referencia = input("Ingrese la referencia: ")
    
    print("")
    for i in datos["ventas"]:
        if(i["referencia"] == referencia and i["eliminado"] == False):

            documento = 0
            while True:
                try:
                    documento = int(input("Ingrese el documento: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido para el documento.")

            if(documento in documentos_usuarios()):

                i["documento_usuario"] = documento
                
                if(categoria == "productos"):

                    i["categoria"] = "productos"

                    tipo_producto = input("Ingrese el tipo de producto: ")

                    if(tipo_producto.lower() in tipo_productos()):

                        i["tipo"] = tipo_producto

                        referencia = input("Ingrese la referencia del producto: ")

                        if(referencia in referencia_productos(tipo_producto)):
                            while True:
                                try:
                                    referencia = input("Por favor ingresa la referencia del artículo: ")
                                    break
                                except Exception:
                                    print("Por favor, ingrese una referencia válida")

                            i["referencia_articulo"] = referencia

                            while True:
                                try:
                                    cantidad = int(input("Ingrese la cantidad: "))
                                    if(cantidad > 0):
                                        break  
                                except ValueError:
                                    print("Error: Debe ingresar un número entero.")

                            i["cantidad"] = cantidad

                            while True:
                                try:
                                    print("Ingrese la fecha de compra (ej. 01/10/1997): ")
                                    fecha_compra = input()
                                    if len(fecha_compra) != 10 or fecha_compra[2] != '/' or fecha_compra[5] != '/':
                                        print("Formato de fecha incorrecto. Se asignará una fecha genérica")
                                        i["fecha_compra"] = "01/01/2024"
                                    else:
                                        i["fecha_compra"] = fecha_compra
                                    break  
                                except ValueError:
                                    fecha_compra_base = "01/01/2024"
                                    print("Formato de fecha incorrecto. Se asignará una fecha genérica (01/01/2024).")
                                    i["fecha_compra"] = fecha_compra_base
                                    break 
                            
                            guardar_datos(datos, RUTA_JSON)
                            print("")
                            print("Venta Registrada")
                        else:
                            print(f"El producto {referencia} no existe")
                    else:
                        print(f"El tipo de producto {tipo_producto} NO existe")
                elif(categoria == "servicios"):
                    i["categoria"] = "servicios"

                    tipo_servicio = input("Ingrese el tipo de servicio: ")

                    if(tipo_servicio.lower() in tipo_servicios()):

                        i["tipo"] = tipo_servicio

                        referencia = input("Ingrese la referencia del servicio: ")

                        if(referencia in referencia_servicios(tipo_servicio)):
                            while True:
                                try:
                                    referencia = input("Por favor ingresa la referencia del artículo: ")
                                    break
                                except Exception:
                                    print("Por favor, ingrese una referencia válida")

                            i["referencia_articulo"] = referencia

                            while True:
                                try:
                                    cantidad = int(input("Ingrese la cantidad: "))
                                    if(cantidad > 0):
                                        break  
                                except ValueError:
                                    print("Error: Debe ingresar un número entero.")

                            i["cantidad"] = cantidad

                            while True:
                                try:
                                    print("Ingrese la fecha de compra (ej. 01/10/1997): ")
                                    fecha_compra = input()
                                    if len(fecha_compra) != 10 or fecha_compra[2] != '/' or fecha_compra[5] != '/':
                                        print("Formato de fecha incorrecto. Vuelva a ingresarlo")
                                        i["fecha_compra"] = "01/01/2024"
                                    else:
                                        i["fecha_compra"] = fecha_compra
                                    break  
                                except ValueError:
                                    fecha_compra_base = "01/01/2024"
                                    print("Formato de fecha incorrecto. Se asignará una fecha genérica (01/01/2024).")
                                    i["fecha_compra"] = fecha_compra_base
                                    break 
                            
                            guardar_datos(datos, RUTA_JSON)
                            print("")
                            print("Venta Registrada")
                        else:
                            print(f"El servicio {referencia} no existe")
                    else:
                        print(f"El tipo de servicio {tipo_servicio} NO existe")
                else:
                    print(f"La categoria {categoria} NO existe")
            else:
                print("El usuario no existe")
        else:
            contador -= 1
    if(contador == 0):
        print("La venta no existe")

def leer_ventas():
    datos_json = cargar_datos(RUTA_JSON)
    contador_ventas = 0
    for i in datos_json["ventas"]:
        if(i["eliminado"] == False):
            contador_ventas += 1
            print("")
            print(f"Venta No. {contador_ventas}")
            print("")
            for llave, valor in i.items():
                if(llave != "id" and llave != "eliminado"):
                    print(llave.capitalize(), "=", valor)

    if(contador_ventas == 0):
        print("No se han realizado ventas")
    
def eliminar_ventas():
    datos = cargar_datos(RUTA_JSON)

    contador = int(len(datos["ventas"]))
    referencia = input("Ingrese la referencia: ")
    print("")
    for i in datos["ventas"]:
        if(i["referencia"] == referencia):
            estado = input("Ingrese 1 para eliminar y 2 de lo contrario: ")
            print("")
            if(estado == "1"):
                i["eliminado"] = True
                print("Venta Eliminada")
                print("")
            elif(estado == "2"):
                i["eliminado"] = False
                print("Venta No Eliminada")
                print("")
            else:
                print("Seleccione un estado correcto (ej. 1)")
                print("")
            return guardar_datos(datos, RUTA_JSON)
        else:
            contador -= 1
    if(contador == 0):
        print("La venta no existe")
