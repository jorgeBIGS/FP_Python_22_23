import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple, Counter

# Creación de una tupla con nombre para los avistamientos
Avistamiento = namedtuple('Avistamiento',
    'fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')

# Función de lectura que crea una lista de avistamientos
def lee_avistamientos(fichero):
    '''
    Lee un fichero de entrada y devuelve una lista de tuplas. 
    Para convertir la cadena con la fecha y la hora al tipo datetime, usar
        datetime.strptime(fecha_hora,'%m/%d/%Y %H:%M')    
    
    ENTRADA:
       - fichero: ruta del fichero csv que contiene los datos en codificación utf-8 
            -> str
    SALIDA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, str, int, str, float, float)]   
    '''
    result = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud in lector:
            fechahora = datetime.strptime(fechahora,'%m/%d/%Y %H:%M')
            duracion = int(duracion)
            latitud = float(latitud)
            longitud = float(longitud)
            result.append(Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)) 
    return result

# Función auxiliar para el cálculo de la distancia entre dos coordenadas
def distancia(coordenadas1, coordenadas2):
    '''
    Devuelve la distancia entre dos coordenadas.
    
    ENTRADA:
       - coordenadas1: tupla con latitud y longitud -> (float, float)
       - coordenadas2: tupla con latitud y longitud -> (float, float)     
    SALIDA:
       - distancia entre las dos coordenadas -> float
    '''
    return sqrt((coordenadas2[0] - coordenadas1[0])**2
                     + (coordenadas2[1] - coordenadas1[1])**2)

def avistamientos_cercanos_ubicacion(avistamientos, ubicacion, r):
    ''' 
    Devuelve el conjunto de avistamientos cercanos a una ubicación.
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
       - ubicacion: coordenadas de la ubicación para la cual queremos encontrar
         avistamientos cercanos -> (float, float)
       - r: radio de distancia -> float
    SALIDA:
       - Conjunto de avistamientos que se encuentran a una distancia
         inferior al valor "r" de la ubicación dada por el parámetro "ubicacion" 
            -> {Avistamiento(datetime, str, str, str, int, str, float, float)}
    '''
    pass

def numero_avistamientos_fecha(avistamientos, fecha):
    ''' Avistamientos que se han producido en una fecha
    
    ENTRADA: 
       - avistamientos: lista de avistamientos
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
       - fecha: fecha del avistamiento -> datetime.date
    SALIDA: 
       - Número de avistamientos producidos en la fecha -> int
    
    Toma como entrada una lista de avistamientos y una fecha.
    Devuelve el número de avistamientos que se han producido en esa fecha.
    '''
    pass

def formas_estados(avistamientos, estados):
    ''' 
    Devuelve el número de formas distintas observadas en avistamientos 
    producidos en alguno de los estados especificados.
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
       - estados: conjunto de estados para los que se quiere hacer el cálculo -> {str}
    SALIDA:
       - Número de formas distintas observadas en los avistamientos producidos
         en alguno de los estados indicados por el parámetro "estados" -> int
    '''
    pass

def duracion_total(avistamientos, estado):
    ''' 
    Devuelve la duración total de los avistamientos de un estado. 
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
       - estado: estado para el que se quiere hacer el cálculo -> str
    SALIDA:
       - duración total en segundos de todos los avistamientos del estado -> int
    '''
    pass

