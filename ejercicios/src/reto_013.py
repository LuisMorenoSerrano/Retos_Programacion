"""
    RETO #013: ¿ES UN PALÍNDROMO?

    Escribe una función que reciba un texto y retorne verdadero o
    falso (Boolean) según sean o no palíndromos.

    Un Palíndromo es una palabra o expresión que es igual si se lee
    de izquierda a derecha que de derecha a izquierda.

    NO se tienen en cuenta los espacios, signos de puntuación y tildes.
    Ejemplo: Ana lleva al oso la avellana.
"""

import unicodedata
import string

PUNCTUATION_AND_SPACES = string.punctuation + "¿¡ "


# Eliminar espacios, signos de puntuación y acentos de una cadena
def remove_non_chars(txt_in: str) -> str:
    # Normalizar y eliminar caracteres diacríticos
    txt_out = "".join(
        char
        for char in unicodedata.normalize("NFD", txt_in)
        if unicodedata.category(char) != "Mn"
    )

    # Eliminar signos de puntuación y espacios
    txt_out = txt_out.translate(str.maketrans("", "", PUNCTUATION_AND_SPACES))

    return txt_out


# Comprobar si el texto es o no un palíndromo
def is_palindrome(txt_in: str) -> bool:
    txt_cleaned: str = remove_non_chars(txt_in).lower()

    return txt_cleaned == txt_cleaned[::-1]
