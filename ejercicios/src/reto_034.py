"""
    RETO #034: CICLO SEXAGENARIO CHINO

    Crea un función, que dado un año, indique el elemento
    y animal correspondiente en el ciclo sexagenario del zodíaco chino.
    - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
    - El ciclo sexagenario se corresponde con la combinación de los elementos
      madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
      conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
      (en este orden).
    - Cada elemento se repite dos años seguidos.
    - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
"""

# Listas de componentes del zodíaco chino
chinese_zodiac = {
    "elements": ["Madera", "Fuego", "Tierra", "Metal", "Agua"],
    "animals": [
        "Rata",
        "Buey",
        "Tigre",
        "Conejo",
        "Dragón",
        "Serpiente",
        "Caballo",
        "Oveja",
        "Mono",
        "Gallo",
        "Perro",
        "Cerdo",
    ],
}


def get_chinese_zodiac(year: int) -> tuple[str, str]:
    """
    Obtiene el elemento y animal del ciclo sexagenario chino para un año dado.

    Args:
        year: Año para el cual calcular el elemento y animal

    Returns:
        Tupla con el elemento y animal correspondientes al año

    Raises:
        TypeError: Si el año no es un número entero
    """
    if not isinstance(year, int):
        raise TypeError("El año debe ser un número entero.")

    # Año de inicio del ciclo sexagenario más reciente
    start_year = 1984

    # Calcular los años transcurridos desde el inicio del ciclo
    years_from_start = year - start_year

    # Obtener el animal (ciclo de 12 años)
    animal_index = years_from_start % 12
    animal = chinese_zodiac["animals"][animal_index]

    # Obtener el elemento (ciclo de 10 años, cada elemento 2 años consecutivos)
    element_cycle = years_from_start % 10
    element_index = element_cycle // 2
    element = chinese_zodiac["elements"][element_index]

    return element, animal
