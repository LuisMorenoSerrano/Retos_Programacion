"""
    RETO #003: LA SUCESIÓN DE FIBONACCI

    Escribe un programa que imprima los 50 primeros números de la sucesión
    de Fibonacci empezando en 0.
    - La serie Fibonacci se compone por una sucesión de números en
      la que el siguiente siempre es la suma de los dos anteriores.
      0, 1, 1, 2, 3, 5, 8, 13...
"""

import sys

sys.set_int_max_str_digits(1000000)


def fibonacci(numero: int = 49) -> list[int]:
    """
    Generar secuencia de Fibonacci.

    Args:
        numero: Cantidad de números de Fibonacci a generar (por defecto 49 para obtener 50 números)

    Returns:
        Lista con la secuencia de Fibonacci desde 0
    """
    sucesion_fib: list[int] = []

    for posicion in range(0, numero + 1):
        if posicion in (0, 1):
            sucesion_fib.append(posicion)
        else:
            sucesion_fib.append(sucesion_fib[-1] + sucesion_fib[-2])

    return sucesion_fib


def print_lista(lista: list[int]) -> None:
    """
    Imprimir lista de números separados por comas.

    Args:
        lista: Lista de números a imprimir
    """
    print(", ".join(str(num) for num in lista))
