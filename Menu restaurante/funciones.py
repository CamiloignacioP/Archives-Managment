


def diccionario_menu (a:list, b:list) -> dict:
    menu =  []
    count = 0
    for i in a:
        menu.append({i:b[count]})
        count += 1
    return menu

