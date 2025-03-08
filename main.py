import os
from funciones_principales import *
from funcion_l_w_json import *
from datetime import datetime
def agregar_menu():
    nuevo_dato("menu.json","Nuevo Menú", formato_menu, "si")
    input("Enter para continuar")
    
def realizar_pedido ():
    nuevo_dato("pedidos.json","Nuevo Pedido", formato_pedido)
    input("Enter para continuar")

def ver_pedidos():
    print("="*50)
    pedidos_t = {str(i): j for i,j in enumerate(leer_json("pedidos.json")) if j["estado"] != "anulado"}
    for i,pedidos in pedidos_t.items():
        print(f"Id de pedido: {i}")
        print(f"{'Cliente:':<10} {pedidos['cliente']}")
        print("Items")
        print("-"*50)
        for items in pedidos["items"]:
            for descrispcion,item in items.items():
                print(f"\t{descrispcion:<10}: {item}")
            print("-"*50)
        print(f"{'Estado':<10}: {pedidos['estado']}")
        print(f"{'Total':<10}: {pedidos['total']}")
        print(f"{'Tipo de pago':<10}: {pedidos['tipo de pago']}")
        print("="*50)
    opcion= input("1. Si desea editar un pedido\n2. Si desea Anular un pedido\n3. cambiar de estado\n4. Pagar\n0. Menu Anteror\n")
    print()
    if opcion in funciones_ver_pedidos:
        try:
            ids = input("Ingrese el ID: ")
            
            if ids in pedidos_t:
                
                idse = int(ids)
                
                funciones_ver_pedidos[opcion](ids,pedidos_t)
            else: 
                print("pedido no registrado")
        except IOError as e:
            print(e)
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
    
    estad = estados[pedidos[ID]["estado"]]
    print("Digite")
    [print(f"{key}: {estado}") for key, estado in estados_ww.items() if pedidos[ID]["estado"] != estado]

    opcion = input("Ingrese la Opcion: ")


    if int(opcion)>estad and opcion in estados_ww:
        pedidos[ID]["estado"] = estados_ww[opcion]
        datos = leer_json("pedidos.json")
        ID = int(ID)
        datos.pop(int(ID))

        datos.insert(int(ID), pedidos[str(ID)])

        escribir_json("pedidos.json", datos)
    else:
        print("No se puede devolver al ese estado")
def pagar(ID,pedidos):
    if pedidos[ID]["tipo de pago"]=="CXP":
        [print(f"{key}: {valor}") for key, valor in tipos_depagos.items()]
        opcion = input("Ingrese metodo de pago: ")
        if opcion in tipos_depagos:
            pago = tipos_depagos[opcion]
            datos= leer_json("pedidos.json")
            datos[int(ID)]["tipo de pago"] = pago
            escribir_json("pedidos.json",datos)
            formato_pagos["cliente"] = datos[int(opcion)]["cliente"]
            formato_pagos["total"] = datos[int(opcion)]["total"]
            formato_pagos["tipo de pago"] = datos[int(opcion)]["tipo de pago"]
            formato_pagos["fecha_pago"] = datetime.now().strftime("%H:%M:%S")
            print(formato_pagos)
            agregar_json("pagos.json", formato_pagos)
            print("Se regitro el pago correctamete")
    else:
        print("Pedido ya esta Pago")
    

funciones_ver_pedidos = {"1": editar_pedido, "2": anular_pedido, "3":cambiar_estado,"4":pagar}
formato_menu = {
    "categoria": "",
    "nombre": "",
    "precio": ""
}
tipos_depagos = {"1":"Efectivo","2":"Transferencia","3":"Nequi"}
formato_pagos = {
    "cliente": "",
    "total": "",
    "tipo de pago":"",
    "fecha_pago": ""
}
formato_pedido = {
    "cliente": "",
    "items": [],
    "estado":"",
    "total":"",
    "tipo de pago":""
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