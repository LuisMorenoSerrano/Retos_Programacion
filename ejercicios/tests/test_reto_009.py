"""Tests para RETO #009: CONVERSIÓN DECIMAL A BINARIO"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                           # pylint: disable=wrong-import-position
from reto_009 import decimal_to_binary  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("decimal,expected_binary", [
    # Casos básicos
    (0, "0"),
    (1, "1"),
    (2, "10"),
    (3, "11"),
    (4, "100"),

    # Casos intermedios
    (9, "1001"),
    (10, "1010"),
    (11, "1011"),
    (27, "11011"),
    (45, "101101"),

    # Casos de números grandes
    (12323, "11000000100011"),
    (2342342343, "10001011100111010100111011000111"),
    (342984753987, "100111111011011011111000000001101000011"),

    # Potencias de 2
    (8, "1000"),
    (16, "10000"),
    (32, "100000"),
    (64, "1000000"),
    (128, "10000000"),
    (256, "100000000"),
    (512, "1000000000"),
    (1024, "10000000000"),
])
def test_decimal_to_binary(decimal, expected_binary):
    """Test para conversión de decimal a binario"""
    assert decimal_to_binary(decimal) == expected_binary


@pytest.mark.parametrize("test_number", [
    0, 1, 2, 3, 4, 9, 10, 11, 27, 45, 255, 1023
])
def test_decimal_to_binary_verification(test_number):
    """Test adicional verificando que la conversión sea correcta usando int() built-in"""
    result = decimal_to_binary(test_number)
    # Verificar que la conversión inversa da el número original
    assert int(result, 2) == test_number


@pytest.mark.parametrize("edge_case", [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
])
def test_decimal_to_binary_edge_cases(edge_case):
    """Test para casos especiales y números consecutivos"""
    result = decimal_to_binary(edge_case)
    # Verificar que no esté vacío y contenga solo 0s y 1s
    assert result
    assert all(c in '01' for c in result)
    # Verificar conversión inversa
    assert int(result, 2) == edge_case
