from avistamientos import *

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
    print(DATOS[0])

if __name__ == '__main__':
    main()