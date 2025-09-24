"""
    RETO #001: EL FAMOSO "FIZZ BUZZ"

    Escribe un programa que muestre por consola (con un print) los
    números de 1 a 100 (ambos incluidos y con un salto de línea entre
    cada impresión), sustituyendo los siguientes:
    - Múltiplos de 3 por la palabra "fizz".
    - Múltiplos de 5 por la palabra "buzz".
    - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizz_buzz(start: int = 1, end: int = 100) -> list[str]:
    """
    Genera la secuencia FizzBuzz para un rango dado.

    Args:
        start: Número inicial (inclusive)
        end: Número final (inclusive)

    Returns:
        Lista de strings con la secuencia FizzBuzz
    """
    resultado = []

    for numero in range(start, end + 1):
        es_multiplo_3: bool = numero % 3 == 0
        es_multiplo_5: bool = numero % 5 == 0

        elemento = (
            f"{'fizz' if es_multiplo_3 else ''}"
            f"{'buzz' if es_multiplo_5 else ''}"
            or str(numero)
        )
        resultado.append(elemento)

    return resultado


if __name__ == "__main__":
    # Ejecutar la secuencia FizzBuzz original (1 a 100)
    secuencia = fizz_buzz()
    for valor in secuencia:
        print(valor)
