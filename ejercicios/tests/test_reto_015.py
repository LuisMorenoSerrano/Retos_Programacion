"""Tests para RETO #015: NÚMEROS DE ARMSTRONG (NARCISISTAS)"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest  # pylint: disable=wrong-import-position
from reto_015 import is_armstrong_number  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("num,expected", [
    # Números de Armstrong de 1 dígito (todos son Armstrong)
    (0, True),
    (1, True),
    (2, True),
    (3, True),
    (4, True),
    (5, True),
    (6, True),
    (7, True),
    (8, True),
    (9, True),

    # Números de Armstrong de 3 dígitos
    (153, True),  # 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    (370, True),  # 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370
    (371, True),  # 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371
    (407, True),  # 4^3 + 0^3 + 7^3 = 64 + 0 + 343 = 407

    # Números de Armstrong de 4 dígitos
    (8208, True),  # 8^4 + 2^4 + 0^4 + 8^4 = 4096 + 16 + 0 + 4096 = 8208
    (9474, True),  # 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474

    # Números que NO son Armstrong
    (36, False),
    (78, False),
    (112, False),
    (245, False),
    (389, False),
    (598, False),
    (2345, False),
    (100, False),
    (200, False),
    (999, False),

    # Números de 2 dígitos (ninguno es Armstrong excepto casos especiales)
    (10, False),
    (11, False),
    (22, False),
    (99, False),
])
def test_is_armstrong_number(num, expected):
    """Test para verificar si un número es de Armstrong"""
    assert is_armstrong_number(num) == expected


@pytest.mark.parametrize("num,expected", [
    (0, True),
    (-1, False),  # "-1" tiene 2 caracteres, no cumple
    (54748, True),   # 5^5 + 4^5 + 7^5 + 4^5 + 8^5
    (92727, True),   # 9^5 + 2^5 + 7^5 + 2^5 + 7^5
    (93084, True),   # 9^5 + 3^5 + 0^5 + 8^5 + 4^5
])
def test_is_armstrong_number_edge_cases(num, expected):
    """Test para casos especiales"""
    assert is_armstrong_number(num) == expected


@pytest.mark.parametrize("num,manual_calc", [
    (153, 1**3 + 5**3 + 3**3),  # 1 + 125 + 27 = 153
    (371, 3**3 + 7**3 + 1**3),  # 27 + 343 + 1 = 371
    (8208, 8**4 + 2**4 + 0**4 + 8**4),  # 4096 + 16 + 0 + 4096 = 8208
])
def test_armstrong_mathematical_property(num, manual_calc):
    """Test para verificar la propiedad matemática de los números Armstrong"""
    # Verificar que el cálculo manual coincide con el número
    assert manual_calc == num
    assert is_armstrong_number(num)


@pytest.mark.parametrize("digit", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_all_single_digit_armstrong(digit):
    """Test para verificar que todos los números de un dígito son Armstrong"""
    assert is_armstrong_number(digit)
