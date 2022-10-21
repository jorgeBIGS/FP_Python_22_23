from avistamientos import *

def test_avistamientos_mayor_duracion_por_estado(avistamientos):
    # Test de la función avistamientos_mayor_duracion_por_estado
    indice = avistamientos_mayor_duracion_por_estado(avistamientos)
    print("Mostrando los 3 avistamientos de mayor duración de los estados 'in' y 'nm':")
    for estado in ['in', 'nm']:
        print("\t", estado)
        for a in indice[estado]:
            print("\t\t", a)

def test_porc_avistamientos_por_forma(avistamientos):
    # Test de la función porc_avistamientos_por_forma
    porcentajes = porc_avistamientos_por_forma(avistamientos)
    print("Porcentajes de avistamientos de las distintas formas (sólo se muestran las formas 'changing', 'chevron', 'cigar' y 'circle'):")
    for forma in ['changing', 'chevron', 'cigar', 'circle']:
        print("\t{}: {:.2f}%".format(forma, porcentajes[forma]))

def test_longitud_media_comentarios_por_estado(avistamientos):
    # Test de la función longitud_media_comentarios_por_estado
    indice = longitud_media_comentarios_por_estado(avistamientos)
    print("Mostrando la media del tamaño de los comentarios de los avistamientos de los estados 'in','nm', 'pa' y 'wa':")
    for estado in ['in', 'nm', 'pa', 'wa']:
        print("\t{}: {}".format(estado, indice[estado]))

def test_hora_mas_avistamientos(avistamientos):
    # Test de la función hora_mas_avistamientos
    print("Hora en la que se han observado más avistamientos:",
        hora_mas_avistamientos(avistamientos))


def test_coordenadas_mas_avistamientos(avistamientos):
    # Test de la función coordenadas_mas_avistamientos
    print("Coordenadas enteras de la región en la que se observaron más avistamientos:", 
        coordenadas_mas_avistamientos(avistamientos))


def test_num_avistamientos_por_mes(avistamientos):
    # Test de la función num_avistamientos_por_mes
    indice = num_avistamientos_por_mes(avistamientos)
    print("Número de avistamientos por mes (sólo se muestran enero, febrero y marzo):")
    for mes in ["Enero", "Febrero", "Marzo"]:
        print("\t{}: {}".format(mes, indice[mes])) 


def test_numero_avistamientos_por_año(avistamientos):
    # Test de la función numero_avistamientos_por_año
    indice = numero_avistamientos_por_año(avistamientos)
    print("Número de avistamientos por año:")
    for a in indice.keys():
        print("\t{}: {}".format(a, indice[a]))


def test_formas_por_mes(avistamientos):
    # Test de la función formas_por_mes
    indice = formas_por_mes(avistamientos)
    print("Índice de formas por mes (se muestran las formas para enero, julio y noviembre:")
    for mes in ["Enero", "Julio", "Noviembre"]:
        print("\t{} ({} formas distintas): {}"
            .format(mes, len(indice[mes]), ', '.join(sorted(indice[mes]))))


def test_avistamientos_por_fecha(avistamientos):
    # Test de la función avistamientos_por_fecha
    indice = avistamientos_por_fecha(avistamientos)
    print("Avistamientos por fecha (se muestran solo dos fechas):", )
    for f in [datetime(1986, 9, 18).date(), datetime(1986, 7, 20).date()]:
        print("\t{}: {}".format(f, indice[f])) 

def test_comentario_mas_largo(avistamientos):
    # Test de la función comentario_mas_largo
    print('El avistamiento con el comentario más largo de 2015 incluyendo la palabra "ufo" es:')     
    print(comentario_mas_largo(avistamientos, 2005, "ufo"))

def test_avistamientos_fechas(avistamientos):
    # Test de la función avistamientos_fechas
    avistamientos_fec = avistamientos_fechas(avistamientos,
                                            datetime(2005,5,1).date(), datetime(2005,5,1).date())
    print("Mostrando los avistamientos entre el 1 de mayo de 2005 y el 1 de mayo de 2005: ")
    for a in avistamientos_fec:
        print("\t", a)
        
    print("\tTotal: {} avistamientos.".format(len(avistamientos_fec)))
    print("Avistamientos hasta el 1 de mayo de 2005: {} avistamientos"
        .format(len(avistamientos_fechas(avistamientos,
                                        fecha_final=datetime(2005,5,1).date()))))
    print("Avistamientos desde el 1 de mayo de 2005: {} avistamientos"
        .format(len(avistamientos_fechas(avistamientos,
                                        fecha_inicial=datetime(2005,5,1).date()))))

def avistamiento_cercano_mayor_duracion(avistamientos):
    # Test de la función avistamiento_cercano_mayor_duracion
    coordenadas = (40.2, -85.4)
    radio = 0.5
    duracion, comentario = avistamiento_cercano_mayor_duracion(avistamientos, coordenadas)
    print("Duración del avistamiento más largo en un entorno de radio {} sobre las coordenadas {}: {} segundos"
        .format(radio, coordenadas, duracion))
    print("Comentario:", comentario)

def test_avistamiento_mayor_duracion(avistamientos):
    # Test de la función avistamiento_mayor_duracion
    forma = 'circle'
    print("Avistamiento de forma \'{}\' de mayor duración: {}"
        .format(forma, avistamiento_mayor_duracion(avistamientos, forma)))

def test_avistamientos_cercanos_ubicacion(avistamientos):
    print(len(avistamientos_cercanos_ubicacion(avistamientos, (40, -85), 0.5)))

def test_duracion_total(avistamientos):
    # Test de la función duracion_total
    for estado in ['in', 'nm', 'pa', 'wa']:
        print("Duración total de los avistamientos en {}: {} segundos."
            .format(estado, duracion_total(avistamientos, estado)))

def test_formas_estados(avistamientos):
    # Test de la función formas_estados
    conjunto_estados = {'in', 'nm', 'pa', 'wa'}
    print("Número de formas distintas observadas en los estados {}: {}"
      .format(', '.join(conjunto_estados), formas_estados(avistamientos, conjunto_estados)))

def test_numero_avistamientos_fecha(avistamientos):
    # Test de la función numero_avistamientos_fecha
    fecha = datetime(2005, 5, 1).date()
    numero_avistamientos = numero_avistamientos_fecha(avistamientos, fecha)
    print("El día {} se produjeron {} avistamientos"
        .format(datetime.strftime(fecha, '%d/%m/%Y'), numero_avistamientos))

def main():
    DATOS = lee_avistamientos('./data/ovnis.csv')
    #print(DATOS[0])
    #test_avistamientos_cercanos_ubicacion(DATOS)
    #test_numero_avistamientos_fecha(DATOS)
    #test_formas_estados(DATOS)
    test_duracion_total(DATOS)

if __name__ == '__main__':
    main()