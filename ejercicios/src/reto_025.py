"""
    RETO #025: ITERATION MASTER

    Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
    ¿De cuántas maneras eres capaz de hacerlo?
    Crea el código para cada una de ellas.
"""


# Contar y mostrar números en un rango: Modo 01
def count_01(number_from: int = 1, number_to: int = 100) -> list[int]:
    """Contar usando for con range"""
    return list(range(number_from, number_to + 1))


# Contar y mostrar números en un rango: Modo 02
def count_02(number_from: int = 1, number_to: int = 100) -> list[int]:
    """Contar usando while"""
    result = []
    number = number_from

    while number <= number_to:
        result.append(number)
        number += 1

    return result
# Contar y mostrar números en un rango: Modo 03
def count_03(number_from: int = 1, number_to: int = 100) -> list[int]:
    """Contar usando list comprehension"""
    return [number for number in range(number_from, number_to + 1)]


# Contar y mostrar números en un rango: Modo 04
def count_04(number_from: int = 1, number_to: int = 100) -> list[int]:
    """Contar usando list() con range"""
    return list(range(number_from, number_to + 1))


# Contar y mostrar números en un rango: Modo 05
def count_05(number_from: int = 1, number_to: int = 100) -> list[int]:
    """Contar usando recursión"""
    if number_from > number_to:
        return []
    return [number_from] + count_05(number_from + 1, number_to)


# Función principal
if __name__ == "__main__":
    print("CONTAR NÚMEROS")
    print("==============")

    # Conjunto de funciones
    count_functs = [count_01, count_02, count_03, count_04, count_05]

    for idx, funct in enumerate(count_functs):
        print(f"\n<< MODO {idx + 1:02} >>")
        numbers = funct()
        print(" ".join(map(str, numbers)))
