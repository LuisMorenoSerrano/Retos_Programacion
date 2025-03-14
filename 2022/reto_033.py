"""
    RETO #033: EL SEGUNDO

    Dado un listado de números, encuentra el SEGUNDO más grande
"""


# Obtener el segundo número más grande de una lista
def get_second_largest(numbers_list: list[int]) -> int:
    unique_numbers = sorted(set(numbers_list))

    if len(unique_numbers) < 2:
        raise ValueError("La lista debe contener al menos dos números diferentes.")

    return unique_numbers[-2]


# Función principal
if __name__ == "__main__":
    # Lista de pruebas
    numbers_lists = [
        [3],
        [5, 5],
        [1, 2],
        [1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 7, 9, 4, 5, 8, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ]

    print("SEGUNDO MÁS GRANDE")
    print("==================")

    for numbers in numbers_lists:
        try:
            second_largest = get_second_largest(numbers)

            print(
                f"\nLista de Números: {numbers}\n"
                f"Segundo más grande: {second_largest}"
            )
        except ValueError as e:
            print(f"\n{numbers}: {e}")
