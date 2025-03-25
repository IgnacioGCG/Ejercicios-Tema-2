from creacion_estrellas import Estrella

# Clase Galaxia
class Galaxia(Estrella):
    def __init__(self, x=0, y=0, z=0, nombre="Galaxia Desconocida"):
        super().__init__(x, y, z)  # Llamamos al constructor de Estrella
        self.nombre = nombre
        self.estrellas = []  # Lista para almacenar estrellas

    def agregar_estrella(self, estrella):
        """Añade una estrella a la galaxia."""
        self.estrellas.append(estrella)

    def listar_estrellas(self):
        """Devuelve una lista de todas las estrellas en la galaxia."""
        return [str(estrella) for estrella in self.estrellas]

    def __str__(self):
        return f"{self.nombre} en posición {super().__str__()} con {len(self.estrellas)} estrellas"