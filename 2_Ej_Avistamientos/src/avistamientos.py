import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple, Counter

# Creación de una tupla con nombre para los avistamientos
Avistamiento = namedtuple('Avistamiento','fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')

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
         -> {Avistamiento(datetime, str, str, str, int, str, float, float)}'''
   result = set()
   for a in avistamientos:
      if distancia(ubicacion, (a.latitud, a.longitud))<r:
         result.add(a)
   return result

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
   result = []
   for a in avistamientos:
      aux = a.fechahora.date()
      if aux == fecha:
         result.append(a)
   return len(result)

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
   result = []
   for a in avistamientos:
      if a.estado in estados:
         result.append(a.forma)
   return len(set(result))

def duracion_total(avistamientos, estado):
   ''' 
   Devuelve la duración total de los avistamientos de un estado. 
   
   ENTRADA:
      - avistamientos: lista de tuplas con la información de los 
      avistamientos 
         -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
      - estado: estado para el que se quiere hacer el cálculo -> str
   SALIDA:
      - duración total en segundos de todos los avistamientos del estado -> int
   '''
   result = []
   for a in avistamientos:
      if a.estado == estado:
         result.append(a.duracion)
   return sum(result)

def filtra_avistamientos_con_forma(avistamientos2, forma2):
   result = []
   for a in avistamientos2:
      if a.forma == forma2:
         result.append(a)
   return result

def avistamiento_mas_reciente_con_forma(avistamientos, forma):
   result = filtra_avistamientos_con_forma(avistamientos, forma)
   return max(result)

def avistamiento_mas_antiguo_con_forma(avistamientos, forma):
   result = filtra_avistamientos_con_forma(avistamientos, forma)
   return min(result)

def avistamiento_mas_reciente_con_forma2(avistamientos, forma):
   result = filtra_avistamientos_con_forma(avistamientos, forma)
   return sorted(result)[-1]

def avistamientos_fechas(avistamientos, fecha_inicial=None, fecha_final=None):
    '''
    Devuelve una lista con los avistamientos que han tenido lugar
    entre fecha_inicial y fecha_final (ambas inclusive). La lista devuelta
    estará ordenada de los avistamientos más recientes a los más antiguos.
    
    Si fecha_inicial es None se devolverán todos los avistamientos
    hasta fecha_final.
    Si fecha_final es None se devolverán todos los avistamientos desde
    fecha_inicial.
    Si ambas fechas son None se devolverá la lista de 
    avistamientos completa. 
    
    Usar el método date() para obtener la fecha de un objeto datetime.
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
       - fecha_inicial: fecha a partir de la cual se devuelven los avistamientos
            -> datetime.date
       - fecha_final: fecha hasta la cual se devuelven los avistamientos
            -> datetime.date
    SALIDA:
       - lista de tuplas con la información de los avistamientos en el rango de fechas
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
    '''
    pass

def avistamiento_mayor_duracion_con_forma(avistamientos, forma):
   '''
   Devuelve el avistamiento de mayor duración de entre todos los
   avistamientos de una forma dada.
   
   ENTRADA:
      - avistamientos: lista de tuplas con la información de los avistamientos 
         -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
      - forma: forma del avistamiento -> str
   SALIDA:
      - avistamiento más largo de la forma dada
         -> Avistamiento(datetime, str, str, str, int, str, float, float)
   '''
   filtrado = filtra_avistamientos_con_forma(avistamientos, forma)
   return max(filtrado, key = lambda a:a.duracion)

def avistamiento_cercano_mayor_duracion(avistamientos, coordenadas, radio=0.5):
    '''
    Devuelve la duración y los comentarios del avistamiento que más 
    tiempo ha durado de aquellos situados en el entorno de las
    coordenadas que se pasan como parámetro de entrada.
    El resultado debe ser una tupla de la forma (duración, comentarios)
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
       - coordenadas: tupla con latitud y longitud -> (float, float)
       - radio: radio de búsqueda -> float
    SALIDA:
       - duración del avistamiento más largo en el entorno de las coordenadas
            -> int
       - comentarios del avistamiento más largo en el entorno de las coordenadas
            -> str
    '''
    pass

def comentario_mas_largo(avistamientos, anyo, palabra):
    ''' 
    Devuelve el avistamiento cuyo comentario es más largo, de entre
    los avistamientos observados en el año dado por el parámetro "anyo"
    y cuyo comentario incluya la palabra recibida en el parámetro "palabra".
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
       - anyo: año para el que se hará la búsqueda -> int
       - palabra: palabra que debe incluir el comentario del avistamiento buscado -> str
    SALIDA:
       - longitud del comentario más largo -> int
       - avistamiento con el comentario más largo
            -> Avistamiento(datetime, str, str, str, int, str, float, float)
    '''    
    pass

def avistamientos_por_fecha(avistamientos):
   ''' 
   Devuelve un diccionario que indexa los avistamientos por fechas
   
   ENTRADA:
      - avistamientos: lista de tuplas con la información de los avistamientos 
         -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
   SALIDA:
      - diccionario en el que las claves son las fechas de los avistamientos 
      y los valores son conjuntos con los avistamientos observados en cada fecha
         -> {datetime.date: {Avistamiento(...)}}
   '''
   result = dict()
   for a in avistamientos:
      clave = a.fechahora.date()
      if not clave in result:
         result[clave] = [a]
      else:
         result[clave] += [a]

   return result

   return result

def formas_por_mes(avistamientos):
    ''' 
    Devuelve un diccionario que indexa las distintas formas de avistamientos
    por los nombres de los meses en que se observan.
    Por ejemplo, para el mes "Enero" se asociará un conjunto con todas las
    formas distintas observadas en dicho mes.
    
    Usar como claves los nombres de los doce meses con la inicial en mayúsculas:
    meses = ["Enero", "Febrero", "Marzo", 
             "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", 
             "Octubre", "Noviembre", "Diciembre"]
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
    SALIDA:
       - diccionario en el que las claves son los nombres de los meses 
         y los valores son conjuntos con las formas observadas en cada mes
            -> {str: {str}}
    '''
    pass


def numero_avistamientos_por_año(avistamientos):
    '''
    Devuelve el número de avistamientos observados en cada año.
             
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
    SALIDA:
       - diccionario en el que las claves son los años
         y los valores son el número de avistamientos observados en ese año
            -> {int: int}
    '''
    pass

def num_avistamientos_por_mes(avistamientos):
    '''
    Devuelve el número de avistamientos observados en cada mes del año.
    
    Usar la expresión .date().month para obtener el número del mes de un objeto datetime.
    
    Usar como claves los nombres de los doce meses con la inicial en mayúsculas:
    meses = ["Enero", "Febrero", "Marzo", 
             "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", 
             "Octubre", "Noviembre", "Diciembre"]
             
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
    SALIDA:
       - diccionario en el que las claves son los nombres de los meses y 
         los valores son el número de avistamientos observados en ese mes
            -> {str: int}
    '''
    pass

def coordenadas_mas_avistamientos(avistamientos): 
    '''
    Devuelve las coordenadas enteras que se corresponden con 
    la zona donde más avistamientos se han observado.
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
    SALIDA:
       - latitud y longitud enteras que acumulan más avistamientos -> (int, int)
       
    En primer lugar construiremos un diccionario cuyas claves sean las coordenadas 
    enteras obtenidas a partir de las coordenadas de los avistamientos, y
    cuyos valores sean el número de avistamientos observados en esas coordenadas.
    Después obtendremos el máximo de los elementos del diccionario según el valor
    del elemento.
    '''   
    pass

def hora_mas_avistamientos(avistamientos):
    ''' 
    Devuelve la hora del día (de 0 a 23) con mayor número de avistamientos
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
    SALIDA:
       - hora del día en la que se producen más avistamientos -> int
       
    En primer lugar construiremos un diccionario cuyas claves sean las horas del
    día en las que se han observado avistamientos, y cuyos valores sean el número
    de avistamientos observados en esa hora.
    Después obtendremos el máximo de los elementos del diccionario según el valor
    del elemento.
    '''
    pass

def longitud_media_comentarios_por_estado(avistamientos):
    '''
    Devuelve un diccionario en el que las claves son los estados donde se
    producen los avistamientos y los valores son la longitud media de los
    comentarios de los avistamientos en cada estado.
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
    SALIDA:
       - diccionario que almacena la longitud media de los comentarios (valores)
         por estado (claves)
            -> {str: float}
            
    En primer lugar construiremos un diccionario cuyas claves sean los estados
    y cuyos valores sean el número de avistamientos de ese estado.
    Después crearemos otro diccionario cuyas claves sean los estados
    y cuyos valores sean la suma de las longitudes de los comentarios de los
    avistamientos de ese estado.
    A partir de estos dos diccionarios crearemos un tercer diccionario cuyas claves
    sean los estados y cuyos valores sean los que nos piden, y que se obtienen
    a partir de los valores de los dos diccionarios auxiliares creados.
    '''
    pass  

def porc_avistamientos_por_forma(avistamientos):  
    '''
    Devuelve un diccionario en el que las claves son las formas de los
    avistamientos, y los valores los porcentajes de avistamientos con cada forma.
    
    ENTRADA:
       - avistamientos: lista de tuplas con la información de los avistamientos 
            -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
    SALIDA:
       - diccionario que almacena los porcentajes de avistamientos (valores)
         por forma (claves)
            -> {str: float}
            
    En primer lugar crearemos un diccionario cuyas claves sean las formas
    y cuyos valores sean el número de avistamientos de esa forma.
    Después crearemos un segundo diccionario con las mismas claves y cuyos valores
    resulten de dividir los valores del diccionario anterior por el número
    total de avistamientos, para obtener los porcentajes.
    '''  
    pass

def avistamientos_mayor_duracion_por_estado(avistamientos, limite=3):
   '''
   Devuelve un diccionario que almacena los avistamientos de mayor duración 
   en cada estado, ordenados de mayor a menor duración.
   
   ENTRADA:
      - avistamientos: lista de tuplas con la información de los avistamientos 
         -> [Avistamiento(datetime, str, str, str, int, str, float, float)]
      - limite: número de avistamientos a almacenar por cada estado -> int
   SALIDA:
      - diccionario en el que las claves son los estados y los valores son listas 
      con los "limite" avistamientos de mayor duración de cada estado,
      ordenados de mayor a menor duración
         -> {str: [Avistamiento(...)]}
         
   En primer lugar crearemos un diccionario cuyas claves sean los estados
   y cuyos valores sean listas con los avistamientos observados en ese estado.
   Después crearemos un segundo diccionario cuyas claves sean los estados
   y cuyos valores sean las mismas listas, pero en orden de mayor a menor
   duración y recortadas a "limite" elementos.
   '''
   pass