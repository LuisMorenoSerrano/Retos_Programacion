"""
    RETO #012: ELIMINANDO CARACTERES

    Crea una función que reciba dos cadenas como parámetro (str1, str2)
    e imprima otras dos cadenas como salida (out1, out2).
    - out1 contendrá todos los caracteres presentes en la str1 pero NO
      estén presentes en str2.
    - out2 contendrá todos los caracteres presentes en la str2 pero NO
      estén presentes en str1.
"""

from typing import List
import unicodedata


# Eliminar acentos de una cadena
def remove_accents(string: str) -> str:
    return "".join(
        char
        for char in unicodedata.normalize("NFD", string)
        if unicodedata.category(char) != "Mn"
    )


# Encontrar caracteres de una cadena no existentes en la otra
def find_chars_non_common(str_in1: str, str_in2: str) -> str:
    str1 = remove_accents(str_in1.lower())
    str2 = remove_accents(str_in2.lower())

    return "".join([char for char in str1 if char not in str2])


# Mostrar caracteres de cada cadena que no están en la otra cadena
def print_chars_non_common(str_in: List[str]):
    print(
        f"Entrada 1: {str_in[0]}\n"
        f"Entrada 2: {str_in[1]}\n"
        f"Salida  1: {find_chars_non_common(str_in[0], str_in[1])}\n"
        f"Salida  2: {find_chars_non_common(str_in[1], str_in[0])}\n"
    )


# Función principal
if __name__ == "__main__":
    strings = [
        ("Murciélago", "Mariposa"),
        ("Colega", "Legado"),
        ("Me gusta Python", "Me gusta Rust"),
    ]

    for str_input in strings:
        print_chars_non_common(str_input)
