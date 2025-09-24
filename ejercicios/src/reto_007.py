"""
    RETO #007: INVIRTIENDO CADENAS

    Crea un programa que invierta el orden de una cadena de texto
    sin usar funciones propias del lenguaje que lo hagan de forma automática.
    - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invert_string(txt_origin: str) -> str:
    """
    Invierte una cadena de texto sin usar funciones built-in de inversión.

    Args:
        txt_origin: Cadena de texto a invertir

    Returns:
        Cadena invertida
    """
    txt_stack: list = list(txt_origin)
    txt_reversed: str = ""

    while txt_stack:
        txt_reversed += txt_stack.pop()

    return txt_reversed
