"""
    RETO #011: EXPRESIONES EQUILIBRADAS

    Crea un programa que comprueba si los paréntesis, llaves y corchetes
    de una expresión están equilibrados.
    - Equilibrado significa que estos delimitadores se abren y cieran
      en orden y de forma correcta.
    - Paréntesis, llaves y corchetes son igual de prioritarios.
      No hay uno más importante que otro.
    - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
    - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""


# Comprobar si una expresión está balanceada
def is_balanced(expr: str) -> bool:
    stack = []
    opening = "({["
    closing = ")}]"
    matches = {")": "(", "}": "{", "]": "["}

    for char in expr:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()

    return not stack


# Función principal
if __name__ == "__main__":
    expressions = [
        "{ [ a * ( c + d ) ] - 5 }",
        "{ a * ( c + d ) ] - 5 }",
        "{a + b [c] * (2x2)}}}}",
        "{a^4 + (((ax4)}",
        "{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }",
        "{{{{{{(}}}}}}",
        "(a"
    ]

    for expression in expressions:
        result: str = "SÍ" if is_balanced(expression) else "NO"
        print(f"La expresión {result} está balanceada: '{expression}'")
