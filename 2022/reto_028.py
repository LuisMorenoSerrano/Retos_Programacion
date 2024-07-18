"""
    RETO #028: VECTORES ORTOGONALES

    Crea un programa que determine si dos vectores son ortogonales.
    - Los dos array deben tener la misma longitud.
    - Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""


# Calcular el producto escalar de dos vectores de cualquier dimensión
def scalar_product(vector1: tuple, vector2: tuple) -> int:
    # Control de errores
    if not (isinstance(vector1, tuple) and isinstance(vector2, tuple)):
        raise TypeError("Ambos argumentos deben ser tuplas.")

    if len(vector1) != len(vector2):
        raise ValueError("Las tuplas deben tener la misma longitud.")

    # Calcular producto escalar
    return sum(a * b for a, b in zip(vector1, vector2))


# Comprobar si dos vectores son ortogonales
def orthogonal_vectors(vector1: tuple, vector2: tuple) -> bool:
    return scalar_product(vector1, vector2) == 0


# Función principal
if __name__ == "__main__":
    # Lista de pares de vectores a comprobar
    vectors = [
        [(1), (2)],
        [(1,), (1, 2, 3)],
        [(1, 2, 3), (1, 2)],
        [(1, 0), (0, 1)],
        [(1, -3), (2, 5)],
        [(1, 0, 0), (0, 1, 0)],
        [(1, 1, 1), (1, 2, 3)],
        [(1, 2, 2), (2, -1, 0)],
        [(1, 4, 0, -3), (2, -3, 0, -1)],
        [(1, 2, 3, 4), (2, 1, 0, -1)],
    ]

    print("VECTORES ORTOGONALES")
    print("====================")

    for vector_tuple in vectors:
        print(f"{vector_tuple[0]} y {vector_tuple[1]}: ", end="")

        try:
            print(orthogonal_vectors(*vector_tuple))
        except (TypeError, ValueError) as e:
            print(e)
