"""
    RETO #030: ORDENA LA LISTA

    Crea una función que ordene y retorne una matriz de números.
    - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
      adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
      o de mayor a menor.
    - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
      automáticamente.
"""


def order_numbers(nums: list[int], order: str) -> list[int]:
    """
    Ordena una lista de números usando el algoritmo bubble sort.

    Args:
        nums: Lista de números enteros a ordenar
        order: Orden de clasificación ("Asc" para ascendente, "Desc" para descendente)

    Returns:
        Lista de enteros ordenada según el parámetro order

    Raises:
        TypeError: Si la lista contiene elementos no enteros
        ValueError: Si el parámetro order no es "Asc" o "Desc"
    """
    # Control de errores
    if not all(isinstance(num, int) for num in nums):
        raise TypeError("La lista debe contener solo números enteros.")

    if order not in ("Asc", "Desc"):
        raise ValueError('El orden debe ser "Asc" o "Desc".')

    # Crear una copia de la lista para no modificar la original
    sorted_nums = nums[:]
    num_elems = len(sorted_nums)

    # Ordenar la lista usando bubble sort
    for i in range(num_elems):
        swapped = False

        for j in range(0, num_elems - i - 1):
            if (order == "Asc" and sorted_nums[j] > sorted_nums[j + 1]) or (
                order == "Desc" and sorted_nums[j] < sorted_nums[j + 1]
            ):
                sorted_nums[j], sorted_nums[j + 1] = sorted_nums[j + 1], sorted_nums[j]
                swapped = True

        if not swapped:
            break

    return sorted_nums
