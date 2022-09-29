from avistamientos import *

def main():
    DATOS = lee_avistamientos('./data/ovnis.csv')
    print(DATOS[0])

if __name__ == '__main__':
    main()