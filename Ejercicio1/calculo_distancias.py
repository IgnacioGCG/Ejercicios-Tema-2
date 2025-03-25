import math


from creacion_estrellas import Estrella

class DistanciaEstrella(Estrella):
    def distancia_a(self, otra_estrella):
        """Calcula la distancia entre esta estrella y otra."""
        return math.sqrt((self.x - otra_estrella.x) ** 2 + 
                         (self.y - otra_estrella.y) ** 2 + 
                         (self.z - otra_estrella.z) ** 2)

    def es_mas_lejana_que(self, otra_estrella, origen):
        """Determina si esta estrella está más lejos del origen que otra estrella."""
        return self.distancia_a(origen) > otra_estrella.distancia_a(origen)
