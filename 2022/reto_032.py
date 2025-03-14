"""
    RETO #032: AÑOS BISIESTOS

    Crea una función que imprima los N próximos años bisiestos
    siguientes a uno dado.
    - Utiliza el menor número de líneas para resolver el ejercicio
"""


# Obtener lista de años bisiestos a partir de uno dado
def get_leap_years(init_year: int, max_years: int = 30) -> list[int]:
    # Control de errores
    if not isinstance(init_year, int):
        raise TypeError("El año debe ser un número entero.")

    # Obtener los próximos años bisiestos
    return [
        year
        for year in range(init_year + 1, init_year + max_years * 4)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    ][:max_years]


# Función principal
if __name__ == "__main__":
    tests = [
        (2024, 30),
        (1895, 30),
        (2100, 5),
        (2032, 12),
        (2036, 5),
        (2040, 10),
    ]

    # Evaluar cada prueba
    print("AÑOS BISISIESTOS")
    print("----------------")

    for start_year, num_years in tests:
        print(
            f"\nAños bisiestos ({num_years}) a partir de {start_year}:"
            f"\n{get_leap_years(start_year, num_years)}"
        )
