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


# Detecta palabras del texto y cuenta el número de apariciones
def count_words(txt: str) -> dict[str, int]:
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


# Función principal
if __name__ == "__main__":
    text = (
        "Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace "
        "hincapié en la legibilidad de su código. Se trata de un lenguaje de programación "
        "multiparadigma, ya que soporta parcialmente la orientación a objetos, programación "
        "imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, "
        "dinámico y multiplataforma.\n"
        "Administrado por Python Software Foundation, posee una licencia de código abierto, "
        "denominada Python Software Foundation License. Python se clasifica constantemente como "
        "uno de los lenguajes de programación más populares.\n"
        "Python fue creado a finales de los años ochenta por Guido van Rossum en Stichting "
        "Mathematisch Centrum (CWI), en Países Bajos, como un sucesor del lenguaje de programación "
        "ABC, capaz de manejar excepciones e interactuar con el sistema operativo Amoeba.\n"
        "El nombre del lenguaje proviene de la afición de su creador por los humoristas británicos "
        "Monty Python.\n"
        "Guido van Rossum es el principal autor de Python, y su continuo rol central en decidir la "
        "dirección de Python es reconocido, refiriéndose a él como Benevolente Dictador Vitalicio "
        "(en inglés: Benevolent Dictator for Life, BDFL); sin embargo el 12 de julio de 2018 "
        "declinó de dicha situación de honor sin dejar un sucesor o sucesora y con una declaración "
        "altisonante:"
        "Entonces, ¿qué van a hacer todos ustedes? ¿Crear una democracia? ¿Anarquía? ¿Una "
        "dictadura? ¿Una federación?\n"
        "Python es un lenguaje de programación multiparadigma. Esto significa que más que forzar a "
        "los programadores a adoptar un estilo particular de programación, permite varios estilos: "
        "programación orientada a objetos, programación imperativa y programación funcional. Otros "
        "paradigmas están soportados mediante el uso de extensiones.\n"
        "Python usa tipado dinámico y conteo de referencias para la gestión de memoria.\n"
        "Una característica importante de Python es la resolución dinámica de nombres; es decir, "
        "lo que enlaza un método y un nombre de variable durante la ejecución del programa "
        "(también llamado enlace dinámico de métodos).\n"
        "Otro objetivo del diseño del lenguaje es la facilidad de extensión. Se pueden escribir "
        "nuevos módulos fácilmente en C o C++. Python puede incluirse en aplicaciones que "
        "necesitan una interfaz programable.\n"
        "Aunque la programación en Python podría considerarse en algunas situaciones hostil a la "
        "programación funcional tradicional expuesta por Lisp, existen bastantes analogías entre "
        "Python y los lenguajes minimalistas de la familia Lisp (como Scheme)."
    )

    words = count_words(text)
    max_long: int = max(len(clave) for clave in words) + 2

    for word, times in words.items():
        print(f"Palabra: {word!r:{max_long}}. Nº Veces: {times:3d}")

    print(f"\nTOTAL PALABRAS{'.' * (max_long + 5)}: {sum(words.values()):3d}")
