"""
    RETO #002: ¿ES UN ANAGRAMA?

    Escribe una función que reciba dos palabras (String) y retorne
    verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS
      las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
"""

from collections import Counter
import unicodedata


def normalizar_palabra(palabra: str) -> str:
    """
    Normalizar las palabras eliminando caracteres especiales y convirtiendo a minúsculas.

    Args:
        palabra: La palabra a normalizar

    Returns:
        Palabra normalizada sin acentos y en minúsculas
    """
    return "".join(
        c
        for c in unicodedata.normalize("NFD", palabra)
        if unicodedata.category(c) != "Mn"
    ).lower()


def es_anagrama(palabra1: str, palabra2: str) -> bool:
    """
    Comprobar si las 2 palabras son anagramas.

    Args:
        palabra1: Primera palabra
        palabra2: Segunda palabra

    Returns:
        True si son anagramas, False en caso contrario
    """
    if palabra1.lower() == palabra2.lower():
        return False

    return Counter(normalizar_palabra(palabra1)) == Counter(
        normalizar_palabra(palabra2)
    )
