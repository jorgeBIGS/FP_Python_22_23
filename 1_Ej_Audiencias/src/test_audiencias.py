from audiencias import lee_audiencias, medias_por_ediciones


def muestra_diccionario(diccionario):
    for k in diccionario:
        print(k, diccionario[k])


def main():
    DATOS = lee_audiencias('./data/GH.csv')
    muestra_diccionario(medias_por_ediciones(DATOS))


if __name__ == '__main__':
    main()
