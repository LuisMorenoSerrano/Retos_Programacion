"""
    RETO #003: LA SUCESIÓN DE FIBONACCI

    Escribe un programa que imprima los 50 primeros números de la sucesión
    de Fibonacci empezando en 0.
    - La serie Fibonacci se compone por una sucesión de números en
      la que el siguiente siempre es la suma de los dos anteriores.
      0, 1, 1, 2, 3, 5, 8, 13...
"""

import sys
import os

sys.set_int_max_str_digits(1000000)


# Generar secuencia de Fibonacci
def fibonacci(numero: int = 49) -> list[int]:
    sucesion_fib: list[int] = []

    for posicion in range(0, numero + 1):
        if posicion in (0, 1):
            sucesion_fib.append(posicion)
        else:
            sucesion_fib.append(sucesion_fib[-1] + sucesion_fib[-2])

    return sucesion_fib


# Imprimir lista
def print_lista(lista: list[int]):
    print(", ".join(str(num) for num in lista))


# Función principal
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_lista(fibonacci())
    elif len(sys.argv) == 2:
        try:
            num = int(sys.argv[1])

            if num >= 0:
                print_lista(fibonacci(num))
            else:
                print("Error: El argumento debe ser un número >= 0")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print(f"Sintaxis de llamada: {os.path.basename(sys.argv[0])} [número]")
