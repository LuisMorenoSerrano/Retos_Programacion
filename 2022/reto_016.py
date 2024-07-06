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


# Función principal
if __name__ == "__main__":
    date_tuples = [
        ("01/01/1900", 31564),
        ("30/02/1900", "15/01/1900"),
        ("01/01/1900", "15/01/1900"),
        ("28/02/2101", "02/02/2101"),
        ("06/06/1969", "30/06/2024"),
        ("11/06/1969", "30/06/2024"),
        ("02/06/1995", "30/06/2024"),
        ("10/07/2001", "30/06/2024"),
    ]

    for date_tuple in date_tuples:
        print(
            f"|{date_tuple[0]} - {date_tuple[1]}| = "
            f"{datediff_days(date_tuple[0], date_tuple[1])} días"
        )
