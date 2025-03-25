# Clase Estrella
class Estrella:
    def __init__(self, nombre, x=0, y=0, z=0):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.nombre} ({self.x}, {self.y}, {self.z})"