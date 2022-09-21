def lee_datos(nombre_fichero):
    result = []
    with open(nombre_fichero, encoding='utf-8') as f:
        for linea in f:
            result.append(linea)
    return result