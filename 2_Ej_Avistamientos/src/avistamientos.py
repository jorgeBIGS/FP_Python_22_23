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