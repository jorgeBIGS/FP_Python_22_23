from audiencias import lee_datos

def main():
    DATOS = lee_datos('./data/GH.csv')
    print(DATOS[0])
    print(len(DATOS))

if __name__=='__main__':
    main()