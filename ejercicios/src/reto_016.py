"""
    RETO #016: ¿CUÁNTOS DÍAS?

    Crea una función que calcule y retorne cuántos días hay entre dos cadenas
    de texto que representen fechas.
    - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
    - La función recibirá dos String y retornará un Int.
    - La diferencia en días será absoluta (no importa el orden de las fechas).
    - Si una de las dos cadenas de texto no representa una fecha correcta se
      lanzará una excepción.
"""

from datetime import datetime


# Calcular la diferencia absoluta en días entre 2 fechas
def datediff_days(date1_str: str, date2_str: str) -> int:
    try:
        date1 = datetime.strptime(date1_str, "%d/%m/%Y")
        date2 = datetime.strptime(date2_str, "%d/%m/%Y")

        return abs((date2 - date1).days)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

        return -1
