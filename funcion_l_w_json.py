import json
def escribir_json(nombre_archivo, new_dato):
    try:
        with open(nombre_archivo, "w", encoding= "utf-8") as archivo:
            json.dump(new_dato, archivo, indent=4)
    except (KeyError , ValueError) as e:
        print(e)
    except IOError as e:
        print(e)
def leer_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Archivo no encontrado")
        return []
    except json.JSONDecodeError:
        print("Error de codificación")

    except IOError as e:
        print("Error inesperado")
def agregar_json(nombre_archivo, new_dato):
    datos = leer_json(nombre_archivo)
    datos.append(new_dato)
    escribir_json(nombre_archivo, datos)
    return leer_json(nombre_archivo)
def lista_categorias():
    datos = leer_json("menu.json")
    categorias = {}
    for menu in datos:
        if menu["categoria"] in categorias:
           categorias[menu["categoria"]][0].append(menu["nombre"])
        else:
            categorias[menu["categoria"]] = [[menu["nombre"]],menu["precio"] ]
    return categorias
