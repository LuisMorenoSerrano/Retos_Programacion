"""
    RETO #024: MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO

    Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
    que calcule el mínimo común múltiplo (mcm) de dos números enteros.
    - No se pueden utilizar operaciones del lenguaje que
      lo resuelvan directamente.
"""


# Obtener el máximo común divisor (MCD) de 2 números
def mcd(num1: int, num2: int) -> int:
    while num2:
        num1, num2 = num2, num1 % num2

    return num1


# Obtener el mínimo común múltiplo (mcm) de 2 números
def mcm(num1: int, num2: int) -> int:
    return (num1 * num2) // mcd(num1, num2)


# Función principal
if __name__ == "__main__":
    numbers = [(1, 2), (24, 36), (12, 9), (120, 525)]

    for number_tuple in numbers:
        num_mcd = mcd(number_tuple[0], number_tuple[1])
        num_mcm = mcm(number_tuple[0], number_tuple[1])

        print(f"MCD({number_tuple[0]}, {number_tuple[1]}) = {num_mcd}")
        print(f"mcm({number_tuple[0]}, {number_tuple[1]}) = {num_mcm}\n")
