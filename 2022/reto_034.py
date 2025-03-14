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


# Obtener el elemento y animal del ciclo sexagenario chino
def get_chinese_zodiac(year: int) -> tuple[str, str]:
    # Año de inicio del ciclo sexagenario más reciente
    start_year = 1984

    # Calcular la posición del año en el ciclo sexagenario
    position = abs(year - start_year) % 60

    # Obtener el elemento y animal correspondiente
    element = chinese_zodiac["elements"][position // 10]
    animal = chinese_zodiac["animals"][position % 12]

    return element, animal


# Función principal
if __name__ == "__main__":
    # Años de prueba
    years = [
        0,
        1000,
        1924,
        1925,
        1926,
        1927,
        1969,
        1984,
        1992,
        2000,
        2005,
        2010,
        2024,
        2025,
    ]

    print("CICLO SEXAGENARIO CHINO")
    print("=======================")

    for current_year in years:
        zodiac_element, zodiac_animal = get_chinese_zodiac(current_year)

        print(
            f"Año: {current_year} -> "
            f"Elemento: {zodiac_element}, "
            f"Animal: {zodiac_animal}"
        )
