"""
    RETO #014: FACTORIAL RECURSIVO

    Escribe una función que calcule y retorne el factorial de un número dado
    de forma recursiva.
"""


def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Error: El factorial de números negativos no está definido")

    if num < 2:
        return 1

    return num * factorial(num - 1)


# Función principal
if __name__ == "__main__":
    numbers = (
        list(range(-1, 10)) + list(range(10, 100, 10)) + list(range(100, 1000, 100))
    )

    for number in numbers:
        try:
            result = f"{number:>3}! = {factorial(number)}"
        except ValueError as e:
            result = f"{number:>3}! = {e}"

        print(result)
