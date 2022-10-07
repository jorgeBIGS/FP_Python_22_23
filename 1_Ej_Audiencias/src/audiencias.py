import csv
import statistics
from matplotlib import pyplot as plt

def lee_audiencias(nombre_fichero):
    result = []
    with open(nombre_fichero, encoding='utf-8') as f:
        # Se crea un objeto lector (un iterator) que separará los valores por comas 
        lector = csv.reader(f)
        for edicion, share in lector:
            result.append((int(edicion), float(share)))
    return result

def filtra_por_ediciones(audiencias, ediciones):
    result = []
    for a in audiencias:
        if a[0] in ediciones:
            result.append(a)
    return result

def calcula_ediciones(audiencias):
    result = []
    for audiencia in audiencias:
        result.append(audiencia[0])
    return result

def calcula_shares_de_edicion(audiencias, edicion):
    result = []
    for a in audiencias:
        if a[0] == edicion:
            result.append(a[1])
    return result

def medias_por_ediciones(audiencias):
    medias = dict()
    ediciones = calcula_ediciones(audiencias)
    for edicion in ediciones:
        # Calculamos la lista de shares de cada edición
        shares = calcula_shares_de_edicion(audiencias, edicion)
        # Usamos la lista de shares para calcular la media
        medias[edicion] = sum(shares)/len(shares)
    return medias

def transforma_a_audiencias(audiencias):
    result = []
    for a in audiencias:
        result.append(a[1])
    return result


def muestra_evolucion_audiencias(audiencias):
    ''' Genera una curva con la evolución de las audiencias
    
    ENTRADA: 
       - audiencias: lista de audiencias -> [(int, float)]
    SALIDA EN PANTALLA:
       - gráfica con la evolución de los shares a lo largo del tiempo

    Toma como entrada una lista de tuplas (edición, share) y muestra una
    curva con la evolución de los shares a lo largo del tiempo.
    
    Para generar la gráfica usaremos elementos del paquete matplotlib. Estas
    son las instrucciones que permiten trazar una curva a partir de la lista de
    shares:
        plt.plot(shares, label='audiencia')
        plt.legend()
        plt.show()
    '''
    # Calculamos la lista de shares
    shares = transforma_a_audiencias(audiencias)
    # Componemos y visualizamos la gráfica
    plt.plot(shares, label='audiencia')
    plt.legend()
    plt.show()

def transforma_a_medias(dicc_medias_por_edicion):
    result = []
    for _, valor in dicc_medias_por_edicion.items():
        result.append(valor)
    return result

def muestra_medias_por_ediciones(audiencias):
    ''' Genera un diagrama de barras 
    con la media de audiencia de cada edición
    
    ENTRADA: 
       - audiencias: lista de audiencias -> [(int, float)]
    SALIDA EN PANTALLA:
       - gráfica con las medias por cada edición

    Toma como entrada una lista de tuplas (edición, share) y muestra un diagrama
    de barras. Habrá una barra por cada edición presente en la lista de audiencias.
    Se mostrará la media de shares de cada edición.
    
    Estas son las instrucciones 'matplotlib' para trazar el diagrama de barras
    a partir de una lista de ediciones y otra lista (con el mismo orden) de
    medias de shares:
        plt.bar(ediciones, lista_medias)
        plt.xticks(ediciones, ediciones, fontsize=8)
        plt.show()
    '''
    # Calculamos la lista de ediciones
    ediciones = sorted(set(calcula_ediciones(audiencias)))

    # Calculamos las medias por cada edición
    dicc_medias = medias_por_ediciones(audiencias)
    # Generamos una lista de medias con el mismo orden que las ediciones
    lista_medias = transforma_a_medias(dicc_medias)
    # Componemos y visualizamos la gráfica
    plt.bar(ediciones, lista_medias)
    plt.xticks(ediciones, ediciones, fontsize=8)
    plt.show()

def mediana(lista):
    ''' Calcula la mediana de una serie
    
    ENTRADA: 
       - lista: serie de valores numéricos -> [float]
    SALIDA:
       - mediana de los valores de entrada -> float
    '''
    pass


def calcula_estadisticos(audiencias):
    ''' Calcula la media, mediana, máximo y mínimo de una lista de audiencias
    
    ENTRADA: 
       - audiencias: lista de audiencias -> [(int, float)]
    SALIDA:
       - media, mediana, máximo y mínimo -> (float, float, float, float)
    '''
    pass

def lista_medias_shares(audiencias):
    ''' Calcula una lista ordenada de ediciones según su media de shares
    
    ENTRADA: 
       - audiencias: lista de audiencias -> [(int, float)]
    SALIDA:
       - pares (medias de audiencia, edición) ordenados de mayor a menor media -> [(float, int)]
    '''
    pass