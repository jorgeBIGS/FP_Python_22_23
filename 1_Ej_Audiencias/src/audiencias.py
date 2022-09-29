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
