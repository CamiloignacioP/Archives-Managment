


# Importar funciones y os

import os
from funciones import *

# Importar archivo Json y transformar a diccionario python

import json
with open("compras.json", "r") as compras:
    leer = compras.read()
diccionario_json_compras = json.loads(leer)

# Imprimir consola principal
print("[1] Mantenedor de servicios")
print("[2] Tienda")
print("[3] Reportes")
print("[4] Salir")
while True:
    selection = str(input("Ingrese opcion consola: "))
    if selection == "1":
        # Imprimir consola Mantenedores
        print("[1] Mantenedor de productos")
        print("[2] Mantenedor de clientes")
        print("[3] Manteneddor de vendedores")
        print("[4] Mantenedor de boletas")
        print("[5] Exportar informacion")
        print("[6] Importar informacion")
        print("[7] salir")
        selection_mantenedor = str(input("Ingrese opcion mantenedor: "))
        while True:
            if selection_mantenedor == "1":
                mostrar_productos(diccionario_json_compras)
                selection_mantenedor = str(input("Ingrese opcion mantenedor: "))
            
            if selection_mantenedor == "2":
                mostrar_clientes(diccionario_json_compras)
                selection_mantenedor = str(input("Ingrese opcion mantenedor: "))
            
            if selection_mantenedor == "3":
                mostrar_vendedores(diccionario_json_compras)
                print(add_seller(diccionario_json_compras))
                selection_mantenedor = str(input("Ingrese opcion mantenedor: "))
                
            if selection_mantenedor == "7":
                os.system("cls")
                break
            break
        
    if selection == "2":
        seller = str(input("Ingrese id de vendedor: "))
        buyer = str(input("Ingrese id de cliente: "))
        print("Lista de productos y precios")
        mostrar_productos(diccionario_json_compras)
        product = str(input("Que producto desea comprar? "))
        print("Total a pagar", Total_payment(product, diccionario_json_compras), "pesos")


    if selection == "4":
        break

