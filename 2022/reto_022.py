"""
    RETO #022: CALCULADORA .TXT

    Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
    resultado e imprímelo.
    - El .txt se corresponde con las entradas de una calculadora.
    - Cada línea tendrá un número o una operación representada por un
      símbolo (alternando ambos).
    - Soporta números enteros y decimales.
    - Soporta las operaciones suma "+", resta "-", multiplicación "*"
      y división "/".
    - El resultado se muestra al finalizar la lectura de la última
      línea (si el .txt es correcto).
    - Si el formato del .txt no es correcto, se indicará que no se han
      podido resolver las operaciones.
"""

import os

DIRNAME = os.path.dirname(__file__) + "/"


# Calculadora que procesa entradas de un archivo de texto
def txt_calculator(filename: str):
    # Obtener operando y aplicar operación
    def get_operand(line, line_number) -> bool:
        nonlocal err_msg
        nonlocal result

        try:
            number = float(line)
        except ValueError:
            err_msg = f"Error: '{line}' no es un número válido"
            return False

        if line_number == 1:
            result = number
        else:
            if operator == "+":
                result += number
            elif operator == "-":
                result -= number
            elif operator == "*":
                result *= number
            elif operator == "/":
                result /= number
            else:
                err_msg = f"Error: '{operator}' no es un operador válido"
                return False

        return True

    # Obtener operador
    def get_operator(line) -> bool:
        nonlocal err_msg
        nonlocal operator

        if line not in valid_operators:
            err_msg = f"Error: '{line}' no es un operador válido"
            return False

        operator = line
        return True

    # Definiciones internas
    file_content: str = ""
    result = 0
    err_msg: str = ""

    # Lectura del archivo con las operaciones (operando y operador)
    with open(DIRNAME + filename, "r", encoding="utf-8") as txtfile:
        valid_operators = {"+", "-", "*", "/"}
        operator: str = ""

        for line_number, line in enumerate(txtfile, start=1):
            line = line.rstrip("\n")
            file_content += line + " "

            if line_number % 2 == 1:  # Operando
                if not get_operand(line, line_number):
                    break
            else:  # Operador
                if not get_operator(line):
                    break

    return file_content, result, err_msg


# Función principal
if __name__ == "__main__":
    files = ["reto_022_1.txt", "reto_022_2.txt", "reto_022_3.txt", "reto_022_4.txt"]

    for file in files:
        expression, value, msg = txt_calculator(file)
        print(f"ARCHIVO DE CÁLCULO: '{file}'")
        print("==================")
        print(f"{expression}", end="")

        if msg:
            print(f"-> {msg}\n")
        else:
            print(f"= {value}\n")
