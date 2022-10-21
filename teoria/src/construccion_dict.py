listado = [1, 2, 3, 3, 3, 4, 5, 6, 7, 1]


def construye_diccionario(lista):
    result = dict()

    for dato in lista:
        clave = dato
        if clave in result:
            valor_actualizado = result[dato]+1
            result[clave] = valor_actualizado
        else:
            valor_inicial = 1
            result[clave] = valor_inicial

    return result


print(construye_diccionario(listado))
#{1: 2, 2: 1, 3: 3, 4: 1, 5: 1, 6: 1, 7: 1}
