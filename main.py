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
    pedidos_t = {str(i): j for i,j in enumerate(leer_json("pedidos.json")) if j["estado"] != "anulado"}

    for i,pedidos in pedidos_t.items():
        print(f"Id de pedido: {i}")
        print(f"{'Cliente:':<20} {pedidos['cliente']}")
        print("Items")
        for items in pedidos["items"]:
            for descrispcion,item in items.items():
                print(f"\t{descrispcion:<20}: {item}")
        print(f"{'Estado':<20}: {pedidos['estado']}")
        print()
    opcion= input("1. Si desea editar un pedido\n2. Si desea Anular un pedido\n3. cambiar de estado\n0. Menu Anteror ")
    print()
    if opcion in funciones_ver_pedidos:
        try:
            ids = input("Ingrese el ID: ")
            
            if ids in pedidos_t:
                
                idse = int(ids)

                funciones_ver_pedidos[opcion](ids,pedidos_t)
            else: 
                print("pedido no registrado")
        except:
            print("valor ingresado no es un numero")
def editar_pedido(ids, pedidos= ""):
    if pedidos[ids]["estado"] == "creado":
        nuevo_dato("pedidos.json","Editar Pedido", formato_pedido,"no","si",ids)
    else:
        print("no se puede editar")
def anular_pedido(ID, pedidos =""):
    if pedidos[ID]["estado"] == "creado":
        pedidos[ID]["estado"]="anulado"
        datos = leer_json("pedidos.json")

        datos.pop(int(ID))

        datos.insert(int(ID), pedidos[ID])

        escribir_json("pedidos.json", datos)

        print("anulado")
    else:
        print("no se puede editar")
    
    
def cambiar_estado(ID,pedidos = ""):
    estad = estados[pedidos[ID]["estados"]]
    print(0)
    [print(f"{key}: {estado}") for key, estado in estados if pedidos[ID]["estados"] != estado]
    print(1)
    opcion = input("Ingrese la Opcion: ")
    print(2)

    if opcion>estad and opcion in estados_ww:
        pedidos[ID]["estado"] = estados_ww[opcion]
        datos = leer_json("pedidos.json")

        datos.pop(int(ID))

        datos.insert(int(ID), pedidos[ID])

        escribir_json("pedidos.json", datos)

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

estados = {"creado":1,"preparacion":2,"servido":3}
estados_ww = {"1":"creado","2":"preparacion","3":"servido"}
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