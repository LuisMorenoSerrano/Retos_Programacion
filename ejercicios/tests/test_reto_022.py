"""Tests para RETO #022: CALCULADORA DE ARCHIVO TXT"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                        # pylint: disable=wrong-import-position
from reto_022 import txt_calculator  # pylint: disable=import-error,wrong-import-position # type: ignore


# Directorio de archivos de prueba
TEST_DIR = os.path.dirname(__file__)


@pytest.mark.parametrize("filename", [
    "test_reto_022_1.txt",
    "test_reto_022_2.txt",
    "test_reto_022_3.txt",
    "test_reto_022_4.txt"
])
def test_txt_calculator_valid_files(filename):
    """Test parametrizado para archivos válidos de calculadora"""
    filepath = os.path.join(TEST_DIR, filename)

    # Verificar que el archivo existe
    assert os.path.exists(filepath), f"El archivo {filename} no existe en tests/"

    # Ejecutar calculadora con path completo
    expression, result, error = txt_calculator(filepath)

    # Verificar que devuelve una tupla con los 3 elementos esperados
    assert isinstance(expression, str)
    assert isinstance(result, (int, float))
    assert isinstance(error, str)

    # Si hay error, verificar que está presente
    if error:
        print(f"✓ {filename}: Error - {error}")
        # Para archivos con errores conocidos, validar tipos específicos
        assert "Error:" in error
    else:
        # Para archivos válidos, verificar que hay expresión y resultado
        assert expression.strip() != ""
        assert result != 0 or "0" in expression  # resultado puede ser 0 legítimo
        print(f"✓ {filename}: {expression}= {result}")


@pytest.mark.parametrize("test_case", [
    ("archivo_inexistente.txt", "Error: No se pudo encontrar el archivo"),
    ("/tmp", "Error: No se pudo leer el archivo"),  # directorio en lugar de archivo
])
def test_txt_calculator_error_cases(test_case):
    """Test parametrizado para casos de error"""
    filename, expected_error = test_case
    expression, result, error = txt_calculator(filename)

    # Verificar que devuelve la tupla correcta
    assert isinstance(expression, str)
    assert isinstance(result, (int, float))
    assert isinstance(error, str)

    # Verificar que el error esperado está en el mensaje de error
    assert expected_error in error


@pytest.mark.parametrize("content,expected_expression,expected_result,expected_error_contains", [
    # Archivo válido simple
    ("10\n+\n5\n", "10 + 5 ", 15.0, ""),
    # Archivo con división por cero
    ("10\n/\n0\n", "10 / 0 ", 10.0, "Error: División por cero"),
    # Archivo vacío
    ("", "", 0, ""),
    # Archivo con número inválido
    ("abc\n+\n5\n", "abc ", 0, "Error: 'abc' no es un número válido"),
    # Archivo con operador inválido
    ("10\n%\n5\n", "10 % ", 10.0, "Error: '%' no es un operador válido"),
])
def test_txt_calculator_with_temp_files(
    content, expected_expression, expected_result, expected_error_contains
):
    """Test para archivos temporales creados dinámicamente"""
    temp_file = os.path.join(TEST_DIR, f"temp_test_{hash(content) % 10000}.txt")

    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(content)

    try:
        expression, result, error = txt_calculator(temp_file)

        # Verificar tipos de retorno
        assert isinstance(expression, str)
        assert isinstance(result, (int, float))
        assert isinstance(error, str)

        # Verificar contenidos esperados
        if expected_error_contains:
            assert expected_error_contains in error
        else:
            assert error == ""
            assert expression == expected_expression
            assert result == expected_result

    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)


@pytest.mark.parametrize("content,expected_expression,expected_result", [
    ("10.5\n+\n2.3\n", "10.5 + 2.3 ", 12.8),  # Operación decimal válida
])
def test_txt_calculator_decimal_operations(content, expected_expression, expected_result):
    """Test para operaciones con números decimales"""
    decimal_file = os.path.join(TEST_DIR, "temp_decimal.txt")
    with open(decimal_file, "w", encoding="utf-8") as f:
        f.write(content)

    try:
        expression, result, error = txt_calculator(decimal_file)

        # Verificar tipos de retorno
        assert isinstance(expression, str)
        assert isinstance(result, (int, float))
        assert isinstance(error, str)

        # Verificar que no hay error
        assert error == ""

        # Verificar expresión y resultado
        assert expression == expected_expression
        assert abs(result - expected_result) < 0.001  # Comparación de flotantes con tolerancia

    finally:
        if os.path.exists(decimal_file):
            os.remove(decimal_file)
