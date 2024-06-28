"""
    RETO #002: ¿ES UN ANAGRAMA?

    Escribe una función que reciba dos palabras (String) y retorne
    verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS
      las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
"""

# Lista de palabras a comprobar
pares_palabras = [
    ("NoEsAnagrama", "NoEsAnagrama"),
    ("Legado", "Colega"),
    ("Pace", "Cepa"),
    ("Retama", "Madera"),
    ("Daba", "Abad"),
    ("Zorra", "Arroz"),
    ("Arroz", "Rozar"),
    ("Monja", "Jamón"),
    ("Monja", "Jamon"),
    ("Alegan", "Ángela"),
    ("Conservadora", "Conversadora"),
    ("SetecAstronomy", "MontereysCoast"),
    ("SetecAstronomy", "MySocratesNote"),
    ("SetecAstronomy", "TooManySecrets"),
]

# Longitud máxima de palabra, incluyendo el delimitador (comilla)
max_long: int = max(len(palabra) for par in pares_palabras for palabra in par) + 2


# Comprobar si las 2 palabras son anagramas
def es_anagrama(palabra1, palabra2: str) -> bool:
    if palabra1.lower() == palabra2.lower():
        return False

    return sorted(palabra1.lower()) == sorted(palabra2.lower())


# Función principal
if __name__ == "__main__":
    for par in pares_palabras:
        resultado: str = "SÍ" if es_anagrama(par[0], par[1]) else "NO"
        print(
            f"¿Son {par[0]!r:{max_long}} y {par[1]!r:{max_long}} anagramas? {resultado}"
        )
