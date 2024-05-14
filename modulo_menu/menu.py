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
from modulo_reportes.manejo_reportes import *

def menu_principal():
    print("Bienvenid@ a ServiPro")
    print("")
    while True:
        print("")
        print("1- Modulo Administrativo")
        print("2- Modulo de Servicios")
        print("3- Modulo de Reportes")
        print("4- Modulo de Ventas")
        print("5- Cerrar Programa")
        print("")

        opcion = input("Selecciona una opcion: ")
        print("")

        if opcion == "1":
            menu_administrativo()
        elif opcion == "2":
            menu_servicios()
        elif opcion == "3":
            menu_reportes()
        elif opcion == "4":
            menu_ventas()
        elif opcion == "5":
            print("")
            print("Programa Finalizado")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

# MENU ADMINISTRATIVO
def menu_administrativo():
    print("")
    print("MENU ADMINISTRATIVO")
    print("")
    while True:
        print("")
        print("1- Gestión Usuarios")
        print("2- Categorías Usuarios")
        print("3- Historial de Usuarios")
        print("4- Personalización de Servicios")
        print("5- Gestión de las ventas")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")

        if opcion == "1":
            gestion_usuarios()
        elif opcion == "2":
            categoria_usuarios()
        elif opcion == "3":
            historial_usuarios()
        elif opcion == "4":
            personalizacion_servicios()
        elif opcion == "5":
            gestion_ventas()
        elif opcion == "0":
            print("")
            print("Regresando...")
            menu_principal()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def gestion_usuarios():
    while True:
        print("")
        print("1- Agregar Usuarios")
        print("2- Modificar Usuarios")
        print("3- Listar Usuarios")
        print("4- Eliminar Usuarios")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            crear_usuarios()
        elif opcion == "2":
            actualizar_usuarios()
        elif opcion == "3":
            leer_usuarios()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def categoria_usuarios():
    while True:
        print("")
        print("1- Nuevos Usuarios")
        print("2- Usuarios Regulares/Leales")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            nuevos_usuarios()
        elif opcion == "2":
            usuarios_regulares_leales()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def historial_usuarios():
    while True:
        print("")
        print("1- Servicios Utilizados por Usuarios")
        print("2- Agregar PQRS")
        print("3- Listar PQRS")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            compras_usuarios()
        elif opcion == "2":
            pass  # Falta implementar
        elif opcion == "3":
            pass  # Falta implementar
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def personalizacion_servicios():
    while True:
        print("")
        print("1- Ofertas Servicios")
        print("2- Ofertas Productos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            servicios_ofertas()
        elif opcion == "2":
            productos_ofertas()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def servicios_ofertas():
    while True:
        print("")
        print("1- Ofertas Telefonia")
        print("2- Ofertas Internet")
        print("3- Ofertas Televisión")
        print("4- Ofertas Datos")
        print("5- Ofertas Minutos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            ofertas_servicios("telefonia")
        elif opcion == "2":
            ofertas_servicios("internet")
        elif opcion == "3":
            ofertas_servicios("television")
        elif opcion == "4":
            ofertas_servicios("datos")
        elif opcion == "5":
            ofertas_servicios("minutos")
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def productos_ofertas():
    while True:
        print("")
        print("1- Ofertas Telefonos")
        print("2- Ofertas Computadores")
        print("3- Ofertas Accesorios")
        print("4- Ofertas Tablets")
        print("5- Ofertas Electrodomesticos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            ofertas_productos("telefonos")
        elif opcion == "2":
            ofertas_productos("computadores")
        elif opcion == "3":
            ofertas_productos("accesorios")
        elif opcion == "4":
            ofertas_productos("tablets")
        elif opcion == "5":
            ofertas_productos("electrodomesticos")
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def gestion_ventas():
    while True:
        print("")
        print("1- Productos Vendidos")
        print("2- Registro Ventas")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            catalogo_ventas()
        elif opcion == "2":
            leer_ventas()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

# MENU DE SERVICIOS
def menu_servicios():
    while True:
        print("")
        print("MENU DE SERVICIOS")
        print("")
        print("1- Gestión Servicios")
        print("2- Gestión Productos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            categoria_servicios()
        elif opcion == "2":
            categoria_productos()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def categoria_servicios():
    while True:
        print("")
        print("1- Servicio Telefonia")
        print("2- Servicio Internet")
        print("3- Servicio Televisión")
        print("4- Servicio Datos")
        print("5- Servicio Minutos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            menu_gestion_servicios("telefonia")
        elif opcion == "2":
            menu_gestion_servicios("internet")
        elif opcion == "3":
           menu_gestion_servicios("television")
        elif opcion == "3":
            menu_gestion_servicios("datos")
        elif opcion == "4":
            menu_gestion_servicios("minutos")
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def categoria_productos():
    while True:
        print("")
        print("1- Productos Telefonos")
        print("2- Productos Computadores")
        print("3- Productos Accesorios")
        print("4- Productos Tablets")
        print("5- Productos Electrodomesticos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            menu_gestion_productos("telefonos")
        elif opcion == "2":
            menu_gestion_productos("computadores")
        elif opcion == "3":
            menu_gestion_productos("accesorios")
        elif opcion == "3":
            menu_gestion_productos("tablets")
        elif opcion == "4":
            menu_gestion_productos("electrodomesticos")
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def menu_gestion_servicios(categoria):
    while True:
        print("")
        print("1- Agregar Servicio")
        print("2- Modificar Servicio")
        print("3- Listar Servicio")
        print("4- Eliminar Servicio")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            crear_servicios(categoria)
        elif opcion == "2":
            actualizar_servicios(categoria)
        elif opcion == "3":
            leer_servicios()
        elif opcion == "4":
            eliminar_servicios()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def menu_gestion_productos(categoria):
    while True:
        print("")
        print("1- Agregar Productos")
        print("2- Modificar Productos")
        print("3- Listar Productos")
        print("4- Eliminar Productos")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            crear_productos(categoria)
        elif opcion == "2":
            actualizar_productos(categoria)
        elif opcion == "3":
            leer_productos()
        elif opcion == "4":
            eliminar_productos()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

# MENU DE REPORTES
def menu_reportes():
    while True:
        print("")
        print("MENU DE REPORTES")
        print("")
        print("1- Informes")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            menu_informes()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def menu_informes():
    while True:
        print("")
        print("1- Informe Productos/Servicios")
        print("2- Servicios Populares")
        print("3- Informe Usuarios")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            total_productos()
            total_servicios()
        elif opcion == "2":
            servicios_populares()
        elif opcion == "3":
            ventas()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

# MENU DE VENTAS
def menu_ventas():
    while True:
        print("")
        print("MENU DE VENTAS")
        print("")
        print("1- Registros")
        print("2- Gestion Ventas Productos")
        print("3- Gestion Ventas Servicios")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            menu_registros()
        elif opcion == "2":
            gestion_ventas_productos()
        elif opcion == "3":
            gestion_ventas_servicios()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def gestion_ventas_servicios():
    while True:
        print("")
        print("1- Agregar Venta")
        print("2- Modificar Venta")
        print("3- Listar Venta")
        print("4- Eliminar Venta")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            crear_ventas("servicios")
        elif opcion == "2":
            actualizar_ventas("servicios")
        elif opcion == "3":
            leer_ventas()
        elif opcion == "4":
            eliminar_ventas()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def gestion_ventas_productos():
    while True:
        print("")
        print("1- Agregar Venta")
        print("2- Modificar Venta")
        print("3- Listar Venta")
        print("4- Eliminar Venta")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            crear_ventas("productos")
        elif opcion == "2":
            actualizar_ventas("productos")
        elif opcion == "3":
            leer_ventas()
        elif opcion == "4":
            eliminar_ventas()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def menu_registros():
    while True:
        print("")
        print("1- Productos y Servicios")
        print("2- Registro Ventas")
        print("0- Regresar")
        print("")
        opcion = input("Seleccione una opción: ")
        print("")
        if opcion == "1":
            leer_registos()
        elif opcion == "2":
            ventas()
        elif opcion == "0":
            print("")
            print("Regresando...")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")
