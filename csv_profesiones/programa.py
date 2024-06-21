


import csv
import random
# Sintaxis: open('nombre_del_archivo.csv', 'modo', newline='')
# Modo común: 'r' (lectura)

"""
with open('nuevo.csv', 'w', newline='', encoding="utf8") as nuevo_csv:
    n_csv = csv.writer(nuevo_csv,)
    n_csv.writerow(["RUN", "nombre", "EDAD"])
    for i in dicci_personas:
        n_csv.writerows([i["dni"], i["nombre"], i["edad"]])
"""

# Importar archivo csv
# Pasar a array y diccionario en python

array_profesion = []
dic_profesion = []
with open("profesion.csv", "r", encoding="utf8") as profesion:
    read = csv.reader(profesion)
    for i in read:
        array_profesion.append(i)
        profesion = {
            "dni": i[0],
            "nombre" : i[1],
            "profesion" : i[2]
        }
        dic_profesion.append(profesion)

array_profesion.pop(0)
dic_profesion.pop(0)

# Contar personas y profesiones

count_desarrollador = 0
count_total_personas = 0
count_disenador = 0
for i in array_profesion:
    for a in i:
        if a == "desarrollador":
            count_desarrollador += 1
        if a == "diseñador":
            count_disenador += 1

# Menu principal de reportes

print("[1] = Reporte personas")
print("[2] = Reporte desarrolladores")
print("[3] = Reporte Diseñadores")
selection = str(input("Ingrese opcion: "))

while True:
    if selection == "1":
        print(f"Hay {len(array_profesion)} personas en total")
        selection = str(input("Ingrese opcion: "))

    if selection == "2":
        print(f"Hay {count_desarrollador} personas que son desarrolladores.")
        porcentaje_desarrollador = int(count_desarrollador * 100 / len(array_profesion))
        print(f"Corresponden al {porcentaje_desarrollador} % del total de personas ({len(array_profesion)} personas).")
        selection = str(input("Ingrese opcion: "))

    if selection == "3":
        print(f"Hay {count_disenador} personas que son diseñadores.")
        porcentaje_disenador = int(count_disenador * 100 / len(array_profesion))
        print(f"Corresponden al {porcentaje_disenador} % del total de personas ({len(array_profesion)} personas).")
        selection = str(input("Ingrese opcion: "))


