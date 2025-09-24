"""
    RETO #017: EN MAYÚSCULA

    Crea una función que reciba un String de cualquier tipo y se encargue de
    poner en mayúscula la primera letra de cada palabra.
    - No se pueden utilizar operaciones del lenguaje que
      lo resuelvan directamente.
"""


# Convertir a mayúsculas la primera letra de cada palabra (capitalizar frase)
def capitalize(txt: str) -> str:
    if not txt:
        return txt

    # Normalizar espacios en blanco: convertir tabs/newlines a espacios
    # y eliminar espacios extra
    normalized = " ".join(txt.split())

    if not normalized:
        return normalized

    result = []
    capitalize_next = True  # Capitalizar el primer carácter

    for char in normalized:
        if char.isalpha():
            if capitalize_next:
                result.append(char.upper())
                capitalize_next = False
            else:
                result.append(char.lower())
        else:
            result.append(char)
            capitalize_next = True  # Próximo carácter alfabético será capitalizado

    return "".join(result)
