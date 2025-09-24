"""Tests para RETO #024: MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                  # pylint: disable=wrong-import-position
from reto_024 import mcd, mcm  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("num1,num2,expected_mcd", [
    (24, 36, 12),
    (12, 9, 3),
    (120, 525, 15),
    (1, 2, 1),
    (5, 5, 5),
    (100, 100, 100),
    (1, 1, 1),
    (0, 5, 5),
    (10, 0, 10),
    (7, 11, 1),    # coprimos
    (15, 16, 1),   # coprimos
    (25, 49, 1),   # coprimos
    (12, 48, 12),  # uno divide al otro
    (7, 21, 7),    # uno divide al otro
    (5, 35, 5),    # uno divide al otro
])
def test_mcd_parametrized(num1, num2, expected_mcd):
    """Test parametrizado para la función mcd"""
    resultado = mcd(num1, num2)
    assert resultado == expected_mcd


@pytest.mark.parametrize("num1,num2,expected_mcm", [
    (24, 36, 72),
    (12, 9, 36),
    (120, 525, 4200),
    (1, 2, 2),
    (5, 5, 5),
    (100, 100, 100),
    (1, 1, 1),
    (7, 11, 77),   # coprimos
    (3, 5, 15),    # coprimos
    (4, 9, 36),    # coprimos
    (12, 48, 48),  # uno divide al otro
    (7, 21, 21),   # uno divide al otro
    (5, 35, 35),   # uno divide al otro
    (2, 3, 6),     # números pequeños
    (4, 6, 12),    # números pequeños
    (6, 8, 24),    # números pequeños
])
def test_mcm_parametrized(num1, num2, expected_mcm):
    """Test parametrizado para la función mcm"""
    resultado = mcm(num1, num2)
    assert resultado == expected_mcm


@pytest.mark.parametrize("a,b", [
    (24, 36), (12, 9), (120, 525), (7, 11), (15, 25),
    (8, 16), (13, 17), (15, 30), (6, 8), (10, 15)
])
def test_relacion_mcd_mcm(a, b):
    """Test parametrizado para verificar que MCD(a,b) * MCM(a,b) = a * b"""
    resultado_mcd = mcd(a, b)
    resultado_mcm = mcm(a, b)
    assert resultado_mcd * resultado_mcm == a * b
