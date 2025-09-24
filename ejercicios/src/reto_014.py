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
