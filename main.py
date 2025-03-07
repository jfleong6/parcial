import os
from funciones_principales import *
from funcion_l_w_json import *
def agregar_menu():
    nuevo_dato("menu.json","Nuevo Menú", formato_menu, "si")
    input("Enter para continuar")
    
def realizar_pedido ():
    nuevo_dato("pedidos.json","Nuevo Pedido", formato_pedido)
    input("Enter para continuar")

def ver_pedidos():
    pedidos_t = {str(i): j for i,j in enumerate(leer_json("pedidos.json")) if j["estado"] != "anular"}

    for i,pedidos in pedidos_t.items():
        if pedidos['estado'] != "anular":
            print(f"Id de pedido: {i}")
            print(f"{'Cliente:':<20} {pedidos['cliente']}")
            print("Items")
            for items in pedidos["items"]:
                for descrispcion,item in items.items():
                    print(f"{descrispcion:<20}: {item}")
            print(f"{'Estado':<20}: {pedidos['estado']}")
        print()
    opcion= input("1. Si desea editar un pedido\n2. Si desea Anular un pedido\n3. cambiar de estado\n0. Menu Anteror ")
    print()
    if opcion in funciones_ver_pedidos:
        try:
            ID = input("Ingrese el ID: ")

            if ID in pedidos_t:
                funciones_ver_pedidos[opcion](int(ID),pedidos_t)
            else: 
                print("pedido no registrado")
        except:
            print("valor ingresado no es un numero")
def editar_pedido(ID, pedidos= ""):
    if pedidos[ID]["estado"] == "creado":
        nuevo_dato("pedidos.json","Nuevo Pedido", formato_pedido,"no","si",ID)
    else:
        print("no se puede editar")
def anular_pedido(ID, pedidos =""):
    if pedidos[ID]["estado"] == "creado":
        pedidos[ID]["estado"] = "anular"
        escribir_json("poblacion.json")
    else:
        print("no se puede editar")
    
    
def cambiar_estado(ID,pedidos = ""):
    [print(f"{key}: {estado}") for key, estado in estados if pedidos[ID]["estados"] != estado]
funciones_ver_pedidos = {"1": editar_pedido, "2": anular_pedido, "3":cambiar_estado}
formato_menu = {
    "categoria": "",
    "nombre": "",
    "precio": ""
}

formato_pagos = {
    "cliente": "",
    "total": "",
    "fecha_pago": ""
}
formato_pedido = {
    "cliente": "",
    "items": [],
    "estado":""
}
categorias = {"1":"entrada","2":"plato fuerte","3":"bebidas"}

estados = {"1":"creado","2":"preparacion","3":"servido"}
funcione_principales = {"1": agregar_menu, "2": realizar_pedido, "3": ver_pedidos}
menu_principal = ["1. Agregar nuevo Menu", "2. Nuevo pedido", "3. Ver Peidos", "4. Salir"]
while True:
    [print(i) for i in menu_principal]
    opcion = input("Ingrese la opcion: ")
    if opcion in funcione_principales:
        funcione_principales[opcion]()
    elif opcion == "4":
        print("Saliendo")
        break
    else:
        print("Opcion no valida")