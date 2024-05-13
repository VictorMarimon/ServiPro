import sys

sys.path.append("..")

from modulo_administrativo.usuarios.crud_usuarios import *
from modulo_administrativo.usuarios.funcionalidades import *
from modulo_administrativo.usuarios.consultas_usuarios import *
from modulo_ventas.catalogo_ventas import *
from modulo_ventas.crud_ventas import *
from modulo_ventas.servicios_productos import *
from modulo_servicios.servicios.crud_servicios import *
from modulo_servicios.productos.crud_productos import *

def menu_principal():
    print("Bienvenid@ a ServiPro")
    print("")
    while True:
        print("1- Modulo Administrativo")
        print("2- Modulo de Servicios")
        print("3- Modulo de Reportes")
        print("4- Modulo de Ventas")
        print("5- Cerrar Programa")
        print("")

        opcion = input("Selecciona una opcion: ")

        if(opcion == "1"):
            menu_administrativo()
        elif(opcion == "2"):
            menu_servicios()
        elif(opcion == "3"):
            menu_reportes()
        elif(opcion == "4"):
            menu_ventas()
        elif(opcion == "5"):
            print("")
            print("Programa Finalizado")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

#MENU ADMINISTRATIVO (falta)

def menu_administrativo():
    print("")
    print("MENU ADMINISTRATIVO")
    print("")
    while True:
        print("1- Gestión Usuarios")
        print("2- Gategorias Usuarios")
        print("3- Historial de Usuarios")
        print("4- Personalización de Servicios")
        print("5- Gestión de las ventas")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")

        if(opcion == "1"):
            print("")
            gestion_usuarios()
            print("")
        elif(opcion == "2"):
            print("")
            categoria_usuarios()
            print("")
        elif(opcion == "3"):
            print("")
            historial_usuarios()
            print("")
        elif(opcion == "4"):
            print("")
            personalizacion_servicios()
            print("")
        elif(opcion == "5"):
            print("")
            gestion_ventas()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_principal()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")
#completo 
def gestion_usuarios():
    while True:
        print("1- Agregar Usuarios")
        print("2- Modificar Usuarios")
        print("3- Listar Usuarios")
        print("4- Eliminar Usuarios")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            crear_usuarios()
            print("")
        elif(opcion == "2"):
            print("")
            actualizar_usuarios()
            print("")
        elif(opcion == "3"):
            print("")
            leer_usuarios()
            print("")
        elif(opcion == "4"):
            print("")
            eliminar_usuario()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_administrativo()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")
#completo
def categoria_usuarios():
    while True:
        print("1- Nuevos Usuarios")
        print("2- Usuarios Regulares/Leales")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            nuevos_usuarios()
            print("")
        elif(opcion == "2"):
            print("")
            usuarios_regulares_leales()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_administrativo()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")
#incompleto
def historial_usuarios():
    while True:
        print("1- Servicios Utilizados por Usuarios")
        print("2- Consultas")
        print("3- Reclamaciones")
        print("4- Sugerencias")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            compras_usuarios()
            print("")
        elif(opcion == "2"):
            print("")
            #FALTA 
            print("")
        elif(opcion == "3"):
            print("")
            #FALTA 
            print("")
        elif(opcion == "4"):
            print("")
            #FALTA 
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_administrativo()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")
#completo
def personalizacion_servicios():
    while True:
        print("1- Ofertas Servicios")
        print("2- Ofertas Productos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            servicios_ofertas()
            print("")
        elif(opcion == "2"):
            print("")
            productos_ofertas()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_administrativo()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def servicios_ofertas():
    while True:
        print("1- Ofertas Telefonia")
        print("2- Ofertas Internet")
        print("3- Ofertas Televisión")
        print("4- Ofertas Datos")
        print("5- Ofertas Minutos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            ofertas_servicios("telefonia")
            print("")
        elif(opcion == "2"):
            print("")
            ofertas_servicios("internet")
            print("")
        elif(opcion == "3"):
            print("")
            ofertas_servicios("television")
            print("")
        elif(opcion == "4"):
            print("")
            ofertas_servicios("datos")
            print("")
        elif(opcion == "5"):
            print("")
            ofertas_servicios("minutos")
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            personalizacion_servicios()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def productos_ofertas():
    while True:
        print("1- Ofertas Telefonos")
        print("2- Ofertas Computadores")
        print("3- Ofertas Accesorios")
        print("4- Ofertas Tablets")
        print("5- Ofertas Electrodomesticos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            ofertas_productos("telefonos")
            print("")
        elif(opcion == "2"):
            print("")
            ofertas_productos("computadores")
            print("")
        elif(opcion == "3"):
            print("")
            ofertas_productos("accesorios")
            print("")
        elif(opcion == "4"):
            print("")
            ofertas_productos("tablets")
            print("")
        elif(opcion == "5"):
            print("")
            ofertas_productos("electrodomesticos")
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            personalizacion_servicios()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

#completo   
def gestion_ventas():
    while True:
        print("1- Productos Vendidos")
        print("2- Registro Ventas")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            catalogo_ventas()
            print("")
        elif(opcion == "2"):
            print("")
            leer_ventas()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_administrativo()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

#MENU DE SERVICIOS (terminado)

def menu_servicios():
    while True:
        print("MENU DE SERVICIOS")
        print("")
        print("1- Gestión Servicios")
        print("2- Gestión Productos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            menu_gestion_servicios()
            print("")
        elif(opcion == "2"):
            print("")
            menu_gestion_productos()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_principal()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def menu_gestion_servicios():
    while True:
        print("")
        print("1- Agregar Servicio")
        print("2- Modificar Servicio")
        print("3- Listar Servicio")
        print("4- Eliminar Servicio")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            crear_servicios()
            print("")
        elif(opcion == "2"):
            print("")
            actualizar_servicios()
            print("")
        elif(opcion == "3"):
            print("")
            leer_servicios()
            print("")
        elif(opcion == "4"):
            print("")
            eliminar_servicios()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_servicios()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def menu_gestion_productos():
    while True:
        print("")
        print("1- Agregar Productos")
        print("2- Modificar Productos")
        print("3- Listar Productos")
        print("4- Eliminar Productos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            crear_productos()
            print("")
        elif(opcion == "2"):
            print("")
            actualizar_productos()
            print("")
        elif(opcion == "3"):
            print("")
            leer_productos()
            print("")
        elif(opcion == "4"):
            print("")
            eliminar_productos()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_servicios()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

#MENU DE REPORTES (falta)

def menu_reportes():
    while True:
        print("MENU DE REPORTES")
        print("")
        print("1- Informes")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            menu_informes()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_principal()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")
#incompleto
def menu_informes():
    while True:
        print("1- Informe Productos/Servicios")
        print("2- Servicios Populares")
        print("3- Informe Usuarios")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            #falta
            print("")
        elif(opcion == "2"):
            print("")
            #falta
            print("")
        elif(opcion == "3"):
            print("")
            #falta
            print("")    
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_reportes()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

#MENU DE VENTAS (terminado)

def menu_ventas():
    while True:
        print("MENU DE VENTAS")
        print("")
        print("1- Registros")
        print("2- Gestion Ventas Productos")
        print("3- Gestion Ventas Servicios")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            menu_registros()
            print("")
        elif(opcion == "2"):
            print("")
            gestion_ventas_productos()
            print("")    
        elif(opcion == "3"):
            print("")
            gestion_ventas_servicios()
            print("")   
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_principal()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def gestion_ventas_servicios():
    while True:
        print("1- Agregar Venta")
        print("2- Modificar Venta")
        print("3- Listar Venta")
        print("4- Eliminar Venta")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            crear_ventas("servicios")
            print("")
        elif(opcion == "2"):
            print("")
            actualizar_ventas("servicios")
            print("")
        elif(opcion == "3"):
            print("")
            leer_ventas()
            print("")
        elif(opcion == "4"):
            print("")
            eliminar_ventas()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_ventas()
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def gestion_ventas_productos():
    while True:
        print("1- Agregar Venta")
        print("2- Modificar Venta")
        print("3- Listar Venta")
        print("4- Eliminar Venta")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            crear_ventas("productos")
            print("")
        elif(opcion == "2"):
            print("")
            actualizar_ventas("productos")
            print("")
        elif(opcion == "3"):
            print("")
            leer_ventas()
            print("")
        elif(opcion == "4"):
            print("")
            eliminar_ventas()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_ventas()
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def menu_registros():
    while True:
        print("1- Productos y Servicios")
        print("2- Registro Ventas")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        if(opcion == "1"):
            print("")
            leer_registos()
            print("")
        elif(opcion == "2"):
            print("")
            ventas()
            print("")
        elif(opcion == "0"):
            print("")
            print("Regresando...")
            print("")
            menu_ventas()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")