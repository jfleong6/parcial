from funcion_l_w_json import *
categorias = {"1":"entrada","2":"plato fuerte","3":"bebidas"}
menu_categoria  = ["1. Entrada","2. Plato fuerte","3. Bebidas"]
formato_menu = {
    "categoria": "",
    "nombre": "",
    "precio": "",
    "cantidad": ""}

def validar_numero(descripcion,dato):
    try:
        dato = int(dato)
        if dato > 0:
            return dato
        else:
            print("Valor negativo")
            return validar_numero(descripcion, input(f"Ingrese {descripcion}: "))
    except ValueError:
        print("No es un numero")
        return validar_numero(descripcion, input(f"Ingrese {descripcion}: "))
def new_plato (categoria):
    list_productos = {str(i):j for i,j in enumerate(lista_categorias()[categoria][0])}
    opciones_platos = [f"{key}. {plato}" for key, plato in list_productos.items()]
    
    platos = []
    total = 0
    while True:
        pedido = {}
        opcion = input(f"Ingrese plato {opciones_platos}: ")
        if opcion in list_productos:
            cant = input("Ingrese la cantidad")
            cant = validar_numero("cantidad: ", cant)
            precio  = cant*lista_categorias()[categoria][1]
            pedido["categoria"] = categoria
            pedido["nombre"] = list_productos[opcion]
            pedido["precio"] = precio
            pedido["cantidad"] = cant
            platos.append(pedido)
            total += precio
            if input("1. agregar otro item\n0. Continuar") != "1":
                break                   
        else: 
            print("Opcion no valida")
            if input("1. agregar otro item\n0. Continuar") !="1":
                break 
    return platos, total
def new_categoria():
    itmes = []
    total = 0
    while True:
        opcion = input(f"Ingrese categoria {menu_categoria}: ")
        if opcion in categorias:
            categoria =categorias[opcion]
            if categoria in lista_categorias():        
                pedido, sub_total = new_plato(categoria)
                total += sub_total
                for plato  in pedido:
                    itmes.append(plato)
                if input("1. agregar otra categoria\n0. Continuar") !="1":
                    
                    break
            else:
                print("Categoria no tiene platos")
        else:
            print("Opcion no valida")
    return itmes,total
def agregar_items():
    return new_categoria()
        
        
def nuevo_dato(nombre_archivo,titulo, formato, menu = "no", editar = "no", ID = ""):
    print(titulo)

    for i in formato:
        print(i)
        if menu == "si" and i == "categoria":
            while True:
                opcion = input(f"Ingrese {i} {menu_categoria}: ")
                if opcion in categorias:
                    dato =categorias[opcion]
                    break
                else:
                    print("Opcion no valida")
        elif i == "items":
            dato, total = agregar_items()
            formato["total"] = total

        elif i == "estado":
                dato="creado"
        elif i == "total":
            continue
        elif i == "tipo de pago":
            dato = "CXP"
        else:
            dato = input(f"Ingrese {i}: ")
        if i == "cliente" or i == "nombre":
            dato = dato.title()
        elif i =="precio" or i == "total":
            dato = validar_numero(i,dato)
          
        formato[i]=dato
    
    if editar == "no":
        agregar_json(nombre_archivo, formato)
    else:
        
        datos = leer_json(nombre_archivo)
        datos.pop(int(ID))
        datos.insert(int(ID),formato)
        escribir_json("pedidos.json",datos)

    print("Registro Exitosamente")


