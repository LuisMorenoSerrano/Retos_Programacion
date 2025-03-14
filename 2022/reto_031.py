"""
    RETO #031: MARCO DE PALABRAS

    Crea una función que reciba un texto y muestre cada palabra en una línea,
    formando un marco rectangular de asteriscos.
    - ¿Qué te parece el reto? Se vería así:
      **********
      * ¿Qué   *
      * te     *
      * parece *
      * el     *
      * reto?  *
      **********
"""


# Imprimir línea superior e inferior del marco
def print_frame_border(length: int) -> None:
    print("*" * (length + 4))


# Partir texto en líneas y formar un marco
def stacking_words(text: str) -> None:
    # Control de errores
    if not isinstance(text, str):
        raise TypeError("El texto debe ser una cadena de caracteres.")

    # Separar el texto en palabras
    words = text.split()

    # Encontrar la palabra más larga
    max_len = max(len(word) for word in words)

    # Imprimir el marco
    print_frame_border(max_len)

    for word in words:
        print(f"* {word.ljust(max_len)} *")

    print_frame_border(max_len)


# Función principal
if __name__ == "__main__":
    # Lista de pruebas
    tests = [
        "¿Qué te parece el reto?",
        "Era una noche oscura y tormentosa...",
        "Mi carro me lo robaron de noche cuando dormía...",
        "La vida es un sueño, y los sueños, sueños son.",
        "Un, dos, tres, probando...",
        "El que mucho abarca, poco aprieta.",
        "El que no llora, no mama.",
        "El que no corre, vuela.",
        "El que no arriesga, no gana.",
    ]

    # Evaluar cada prueba
    print("MARCO DE PALABRAS")
    print("-----------------")

    for i, test in enumerate(tests, 1):
        print(f"\nPrueba {i}: {test}")
        stacking_words(test)
