


from funciones import *

with open("platos.txt", "r") as platos:
    leer = platos.read()
    lista_platos = leer.split()

with open("precios.txt", "r") as precios:
    leer = precios.read()
    lista_precios = leer.split()

print("[1] = Mostrar platos y su precio")
print("[2] = Agregar plato")


selection = int(input("numero consola: "))

if selection == 1:
    count = 1
    for i in diccionario_menu(lista_platos, lista_precios):
        for a in i:
            print(count, ".", a, "=", i[a])
            count += 1

if selection == 2:
    name = str(input("Ingrese nombre de plato: "))
    with open("platos.txt", "a") as platos:
        nueva_linea = platos.write("\n")
        nuevo_plato = platos.write(name)
    precio = str(input("Ingrese precio: "))    
    with open("precios.txt", "a") as prices:
        nuevo_precio = prices.write("\n")
        nuevo_precio = prices.write(precio)




