"""
    RETO #033: EL SEGUNDO

    Dado un listado de números, encuentra el SEGUNDO más grande
"""


def get_second_largest(numbers_list: list[int]) -> int:
    """
    Encuentra el segundo número más grande en una lista de números.

    Args:
        numbers_list: Lista de números enteros

    Returns:
        El segundo número más grande de la lista

    Raises:
        ValueError: Si la lista contiene menos de dos números diferentes
    """
    unique_numbers = sorted(set(numbers_list))

    if len(unique_numbers) < 2:
        raise ValueError("La lista debe contener al menos dos números diferentes.")

    return unique_numbers[-2]
