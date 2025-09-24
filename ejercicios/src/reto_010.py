"""
    RETO #010: CÓDIGO MORSE

    Crea un programa que sea capaz de transformar texto natural a código
    morse y viceversa.
    - Debe detectar automáticamente de qué tipo se trata y realizar
      la conversión.
    - En morse se soporta raya '-', punto '.', un espacio ' ' entre letras
      o símbolos y dos espacios entre palabras '  '.
    - El alfabeto morse soportado será el mostrado en
      https://es.wikipedia.org/wiki/Código_morse.
"""

import re
from unidecode import unidecode

# Diccionarios de equivalencias entre caracteres <-> código Morse
text_to_morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    '"': ".-..-.",
    "/": "-..-.",
}
morse_to_text_dict = {v: k for k, v in text_to_morse_dict.items()}


def is_morse(txt: str) -> bool:
    """
    Detectar si un texto es código Morse.

    Args:
        txt: Texto a verificar

    Returns:
        True si el texto contiene solo caracteres de código Morse, False en caso contrario
    """
    return not bool(re.search(r"[^.\- /]", txt))


def text_to_morse(text: str) -> str:
    """
    Convertir texto a código Morse.

    Args:
        text: Texto a convertir

    Returns:
        Código Morse equivalente
    """
    return " ".join(
        text_to_morse_dict.get(char, "") for char in unidecode(text.upper())
    )


def morse_to_text(morse: str) -> str:
    """
    Convertir código Morse a texto.

    Args:
        morse: Código Morse a convertir

    Returns:
        Texto equivalente
    """
    # Dividir código Morse en palabras y luego en caracteres
    words = morse.split("  ")
    text = []

    for word in words:
        chars = word.split()
        text.append("".join(morse_to_text_dict.get(char, "") for char in chars))

    return " ".join(text)
