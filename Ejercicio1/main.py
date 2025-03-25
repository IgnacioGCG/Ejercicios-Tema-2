from lanzador import Galaxia, DistanciaEstrella, estrella_mas_lejos

if __name__ == "__main__":
    # Creamos estrellas con la nueva clase
    estrella_A = DistanciaEstrella("A", 2, 3, 1)
    estrella_B = DistanciaEstrella("B", 4, 4, 4)
    estrella_C = DistanciaEstrella("C", -3, -1, 0)

    print(" Estrellas en el universo:")
    print(estrella_A)
    print(estrella_B)
    print(estrella_C)

    # Crear galaxias y agregar estrellas
    galaxia1 = Galaxia("Galaxia Andrómeda", 10, 10, 10)
    galaxia2 = Galaxia("Galaxia Vía Láctea", -10, -10, -10)

    galaxia1.agregar_estrella(estrella_A)
    galaxia1.agregar_estrella(estrella_B)
    galaxia2.agregar_estrella(estrella_C)

    print("\n Galaxias creadas:")
    print(galaxia1)
    print(" Estrellas en Andrómeda:", ", ".join(galaxia1.listar_estrellas()))
    
    print(galaxia2)
    print(" Estrellas en Vía Láctea:", ", ".join(galaxia2.listar_estrellas()))

    # Calcular distancias
    print("\n Distancias entre estrellas:")
    print(f"Distancia entre A y B: {estrella_A.distancia_a(estrella_B):.2f}")
    print(f"Distancia entre B y C: {estrella_B.distancia_a(estrella_C):.2f}")

    estrella_lejana = estrella_mas_lejos([estrella_A, estrella_B, estrella_C])
    print("\n La estrella más lejana del origen es:", estrella_lejana)
