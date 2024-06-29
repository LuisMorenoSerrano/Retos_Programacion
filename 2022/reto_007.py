"""
    RETO #007: INVIRTIENDO CADENAS

    Crea un programa que invierta el orden de una cadena de texto
    sin usar funciones propias del lenguaje que lo hagan de forma automática.
    - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invert_string(txt_origin: str) -> str:
    txt_stack: list = list(txt_origin)
    txt_reversed: str = ""

    while txt_stack:
        txt_reversed += txt_stack.pop()

    return txt_reversed


# Función principal
if __name__ == "__main__":
    strings = [
        "Hola mundo",
        "Esto es una prueba de inversión de cadenas"
    ]

    for string in strings:
        print(
            f"Cadena Original.: {string}\n"
            f"Cadena Invertida: {invert_string(string)}\n"
        )
