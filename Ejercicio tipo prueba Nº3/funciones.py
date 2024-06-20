


import json
# Funciones Mantenimiento 

def mostrar_productos (a:dict):
    for i in a:
        if i == "productos":
            for b in a[i]:
                nombre_precio = print(b["nombre"], "=", b["precio"], "pesos")
    return nombre_precio

def mostrar_clientes (a:dict):
    for i in a:
        if i == "clientes":
            for b in a[i]:
                nombre_credito = print(b["nombre"], "=", b["credito"], "credito")
    return nombre_credito

# Funciones Mantenimiento (Vendedores) 

def mostrar_vendedores (a:dict):
    for i in a:
        if i == "vendedores":
            for b in a[i]:
                nombre_vendedor = print(b["nombre"], "=", b["id"], "id")
    return nombre_vendedor

def add_seller (a:dict):
        add_seller = str(input("Desea agregar vendedor? "))
        while True:
            if add_seller == "si":
                id = str(input("Ingrese id: "))
                name = str(input("Ingrese nombre: "))
                for i in a:
                    if i == "vendedores":
                        a[i].append({"id":id, "nombre":name})
                add_seller = str(input("Desea agregar vendedor? "))         
            else:
                break
        return a["vendedores"]

# Funciones Tienda

def Total_payment (a:str, b:dict):
    productos =  {}
    total_pagar = 0
    for i in b:
        if i == "productos":
            for c in b[i]:
                if c["nombre"] == a:
                    total_pagar += int(c["precio"])
            p = str(input("Desea agregar producto? "))
            while True:
                if p == "si":
                    o = str(input("Que producto desea agregar? "))
                    for c in b[i]:
                        if c["nombre"] == o:
                            productos[o] = int(c["precio"])
                            total_pagar += int(c["precio"])
                    p = str(input("Desea agregar producto? "))
                if p == "no":
                    break
    return total_pagar

