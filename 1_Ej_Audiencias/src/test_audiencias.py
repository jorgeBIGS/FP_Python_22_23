from audiencias import *

def test_lista_medias_shares():
    # Test de la función lista_medias_shares
    shares_eds = lista_medias_shares(AUDIENCIAS_GH)
    for s, e in shares_eds:
    print("{:3d} -> {:6.3f}".format(e, s))

def test_calcula_estadisticos(audiencias):
    # Test de la función calcula_estadisticos
    media, mediana, maximo, minimo = calcula_estadisticos(audiencias)
    print('Media: ', media)
    print('Mediana:', mediana)
    print('Máximo:', maximo)
    print('Mínimo:', minimo)

def muestra_diccionario(diccionario):
    for k in diccionario:
        print(k, diccionario[k])


def main():
    DATOS = lee_audiencias('./data/GH.csv')
    #muestra_diccionario(medias_por_ediciones(DATOS))
    #muestra_evolucion_audiencias(DATOS)
    muestra_medias_por_ediciones(DATOS)
    #print(transforma_a_medias(medias_por_ediciones(DATOS)))

if __name__ == '__main__':
    main()
