"""
    RETO #035: LOS NÚMEROS PERDIDOS

    Dado un array de enteros ordenado y sin repetidos,
    crea una función que calcule y retorne todos los que faltan entre
    el mayor y el menor.
    - Lanza un error si el array de entrada no es correcto.
"""


def find_missing_numbers(numbers_array: list[int]) -> list[int]:
    """
    Encuentra los números perdidos entre el menor y mayor de un array.

    Args:
        numbers_array: Lista de enteros ordenados sin repetidos

    Returns:
        Lista de enteros perdidos entre el menor y mayor

    Raises:
        ValueError: Si el array está vacío, desordenado o tiene repetidos
        TypeError: Si el array contiene elementos no enteros
    """
    # Validar que el array no esté vacío
    if not numbers_array:
        raise ValueError("El array no puede estar vacío.")

    # Validar que todos los elementos sean enteros
    if not all(isinstance(num, int) for num in numbers_array):
        raise TypeError("El array debe contener solo números enteros.")

    # Validar que el array esté ordenado
    if numbers_array != sorted(numbers_array):
        raise ValueError("El array debe estar ordenado de menor a mayor.")

    # Validar que no haya números repetidos
    if len(numbers_array) != len(set(numbers_array)):
        raise ValueError("El array no puede contener números repetidos.")

    # Encontrar el menor y mayor número
    min_number = numbers_array[0]
    max_number = numbers_array[-1]

    # Crear el conjunto de números esperados entre el menor y mayor
    expected_numbers = set(range(min_number, max_number + 1))

    # Crear el conjunto de números presentes en el array
    present_numbers = set(numbers_array)

    # Encontrar los números perdidos y ordenarlos
    missing_numbers = sorted(list(expected_numbers - present_numbers))

    return missing_numbers
