"""
    RETO #008: CONTANDO PALABRAS

    Crea un programa que cuente cuantas veces se repite cada palabra
    y que muestre el recuento final de todas ellas.
    - Los signos de puntuación no forman parte de la palabra.
    - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
    - No se pueden utilizar funciones propias del lenguaje que
      lo resuelvan automáticamente.
"""

import re


def count_words(txt: str) -> dict[str, int]:
    """
    Detecta palabras del texto y cuenta el número de apariciones.

    Args:
        txt: Texto a analizar

    Returns:
        Diccionario con las palabras como clave y su frecuencia como valor,
        ordenado por frecuencia (mayor a menor) y alfabéticamente
    """
    # Obtener lista de palabras
    words_list = re.findall(r"\b\w+\b", txt)

    # Acumular número de apariciones de cada palabra -en minúscula-
    words_dict = {}
    key: str = ""

    for item in words_list:
        key = item.lower()

        if key in words_dict:
            words_dict[key] += 1
        else:
            words_dict[key] = 1

    # Devolver el diccionario ordenado por:
    # - Número de apariciones (de mayor a menor)
    # - Alfabético por palabra
    return dict(sorted(words_dict.items(), key=lambda item: (-item[1], item[0])))
