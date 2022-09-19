from audiencias import lee_datos


if __name__=='__main__':
    DATOS = lee_datos('./data/GH.csv')
    print(DATOS[0])
    print(len(DATOS))