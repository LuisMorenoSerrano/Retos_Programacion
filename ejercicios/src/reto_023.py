"""
    RETO #023: CONJUNTOS

    Crea una función que reciba dos array, un booleano y retorne un array.
    - Si el booleano es verdadero buscará y retornará los elementos comunes
      de los dos array.
    - Si el booleano es falso buscará y retornará los elementos no comunes
      de los dos array.
    - No se pueden utilizar operaciones del lenguaje que
      lo resuelvan directamente.
"""


# Comparar listas para obtener elementos comunes o no comunes (sin repetición)
def compare_lists(list1: list, list2: list, find_common: bool) -> list:
    result: list = []

    # Encontrar elementos comunes en las dos listas
    if find_common:
        for element in list1:
            if element in list2 and element not in result:
                result.append(element)
    # Encontrar elementos no comunes en las dos listas
    else:
        for element in list1:
            if element not in list2 and element not in result:
                result.append(element)

        for element in list2:
            if element not in list1 and element not in result:
                result.append(element)

    return result


# Función principal
if __name__ == "__main__":
    lists = [
        ([1, 3, 5, 7, 9], [1, 2, 3, 5, 8, 13]),
        ([1, 2, 2, 3, 4, 5], [2, 3, 3, 5, 6, 7]),
        (["sopa", 23, "avión", "j", 13.25], ["avión", "colega", 0, 13.15, 23, 12]),
    ]

    for list_tuple in lists:
        common   = compare_lists(list_tuple[0], list_tuple[1], True)
        distinct = compare_lists(list_tuple[0], list_tuple[1], False)

        print("COMPARACIÓN DE LISTAS")
        print("=====================")
        print(f"Lista 1..: {list_tuple[0]}")
        print(f"Lista 2..: {list_tuple[1]}")
        print(f"Comunes..: {common}")
        print(f"Distintos: {distinct}\n")
