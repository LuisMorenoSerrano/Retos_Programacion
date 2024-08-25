"""
    Crea una función que ordene y retorne una matriz de números.
    - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
      adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
      o de mayor a menor.
    - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
      automáticamente.
"""

from typing import List


# Ordenar listas de números
def order_numbers(nums: List[int], order: str) -> List[int]:
    # Control de errores
    if not all(isinstance(num, int) for num in nums):
        raise TypeError("La lista debe contener solo números enteros.")

    if order not in ("Asc", "Desc"):
        raise ValueError('El orden debe ser "Asc" o "Desc".')

    # Crear una copia de la lista para no modificar la original
    sorted_nums = nums[:]
    num_elems = len(sorted_nums)

    # Ordenar la lista
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


# Función principal
if __name__ == "__main__":
    # Lista de pruebas
    tests = [
        ([2, 4.0, 6, 8.1, 9], "Asc"),
        ([2, 4, 6, 8, 9], "Random order"),
        ([2, 4, 6, 8, 9], "Asc"),
        ([2, 4, 6, 8, 9], "Desc"),
        ([2, 4, 6, 8, 9, 1, 3, 5, 7], "Asc"),
        ([2, 4, 6, 8, 9, 1, 3, 5, 7], "Desc"),
        ([9, 8, 6, 4, 2], "Asc"),
        ([9, 8, 6, 4, 2], "Desc"),
        ([7, 5, 3, 1, 9, 8, 6, 4, 2], "Asc"),
        ([7, 5, 3, 1, 9, 8, 6, 4, 2], "Desc"),
        ([1, 2, 3, 4, 5], "Asc"),
        ([1, 2, 3, 4, 5], "Desc"),
    ]

    # Evaluar cada prueba
    print("ORDENAR LISTAS DE NÚMEROS")
    print("-------------------------")

    for numbers_list, order_mode in tests:
        try:
            result = order_numbers(numbers_list, order_mode)
            print(f"order_numbers({numbers_list}, {order_mode}) = {result}")
        except (TypeError, ValueError) as e:
            print(f"order_numbers({numbers_list}, {order_mode}) = {e}")
