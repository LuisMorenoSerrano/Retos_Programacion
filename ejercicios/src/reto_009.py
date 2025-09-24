"""
    RETO #009: DECIMAL A BINARIO

    Crea un programa se encargue de transformar un número
    decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

# Convertir número decimal (base 10) a binario (base 2)
def decimal_to_binary(num_dec: int) -> str:
    num_bin: list = []
    dividend: int = num_dec
    quotient: int = 0

    # Calcular y almacenar restos de la división entera por 2
    while True:
        num_bin.append(dividend % 2)
        quotient = dividend // 2

        # Añadir último cociente si la división no puede continuar
        if quotient < 2:
            if quotient == 1:
                num_bin.append(quotient)

            break

        dividend = quotient

    # Tomar elementos de la lista en orden inverso y concatenar
    return ''.join(map(str, num_bin[::-1]))
