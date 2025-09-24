"""
    RETO #032: AÑOS BISIESTOS

    Crea una función que imprima los N próximos años bisiestos
    siguientes a uno dado.
    - Utiliza el menor número de líneas para resolver el ejercicio
"""


# Obtener lista de años bisiestos a partir de uno dado
def get_leap_years(init_year: int, max_years: int = 30) -> list[int]:
    # Control de errores: Validar que el año sea un número entero
    if not isinstance(init_year, int):
        raise TypeError("El año debe ser un número entero.")

    # Control de errores: Validar que `max_years` sea positivo
    if max_years <= 0:
        return []

    # Cálculo: Generar años bisiestos usando reglas del calendario gregoriano
    return [y for y in range(init_year + 1, init_year + max_years * 8)
            if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0][:max_years]
