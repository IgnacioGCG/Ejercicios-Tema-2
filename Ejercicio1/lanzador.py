import math

from creacion_estrellas import Estrella

from creacion_galaxias import Galaxia

from calculo_distancias import DistanciaEstrella



# Función para encontrar la estrella más lejana del origen
def estrella_mas_lejos(estrellas):
    origen = DistanciaEstrella("Origen", 0, 0, 0)
    return max(estrellas, key=lambda estrella: estrella.distancia_a(origen))
