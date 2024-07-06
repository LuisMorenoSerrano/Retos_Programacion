"""
    RETO #017: EN MAYÚSCULA

    Crea una función que reciba un String de cualquier tipo y se encargue de
    poner en mayúscula la primera letra de cada palabra.
    - No se pueden utilizar operaciones del lenguaje que
      lo resuelvan directamente.
"""


# Convertir a mayúsculas la primera letra de cada palabra (capitalizar frase)
def capitalize(txt: str) -> str:
    return " ".join([word.capitalize() for word in txt.split()])


# Función principal
if __name__ == "__main__":
    strings = [
        "hola",
        "adiós",
        "mi carro me lo robaron",
        "Es una prueba de Fuego",
        "era una noche de luna y sin embargo llovía.",
    ]

    # Longitud máxima de texto
    max_long: int = max(len(txt) for txt in strings)

    for string in strings:
        print(f"'{string:{max_long}}' => '{capitalize(string)}'")
