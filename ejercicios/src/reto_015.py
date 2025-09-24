"""
    RETO #015: ¿ES UN NÚMERO DE ARMSTRONG?

    Escribe una función que calcule si un número dado es un número de Armstrong
    (o también llamado narcisista).
    Si no conoces qué es un número de Armstrong, debes buscar información
    al respecto.

    Un número de 'n' dígitos es un número de Armstrong si es igual a la suma de
    las n-ésimas potencias de sus dígitos. Por ejemplo, 371 y 8208 lo son por:

      371  = 3^3 + 7^3 + 1^3
      8208 = 8^4 + 2^4 + 0^4 + 8^4
"""

# Comprueba si es o no un número de Armstrong
def is_armstrong_number(num: int) -> bool:
    # Los números de Armstrong solo se definen para números no negativos
    if num < 0:
        return False

    num_string: str = str(num)
    num_digits: int = len(num_string)

    return num == sum(int(digit) ** num_digits for digit in num_string)
