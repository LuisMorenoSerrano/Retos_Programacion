"""Tests para RETO #014: FACTORIAL RECURSIVO"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                   # pylint: disable=wrong-import-position
from reto_014 import factorial  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("num,expected", [
    # Casos básicos
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (10, 3628800),

    # Casos adicionales
    (11, 39916800),
    (12, 479001600),
    (15, 1307674368000),
    (20, 2432902008176640000),
])
def test_factorial_positive_numbers(num, expected):
    """Test para factorial de números positivos"""
    assert factorial(num) == expected


@pytest.mark.parametrize("negative_num", [
    -1, -2, -5, -10, -100
])
def test_factorial_negative_numbers(negative_num):
    """Test para factorial de números negativos (debe lanzar ValueError)"""
    with pytest.raises(ValueError,
                       match="Error: El factorial de números negativos no está definido"):
        factorial(negative_num)


@pytest.mark.parametrize("base,factorial_compare", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (10, 3628800),
    (11, 39916800),
    (12, 479001600),
    (13, 6227020800),
    (14, 87178291200),
])
def test_factorial_edge_cases(base, factorial_compare):
    """Test para casos especiales comparando con versión iterativa"""
    def factorial_iterative(n):
        if n < 0:
            raise ValueError("Error: El factorial de números negativos no está definido")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    # Verificar que la implementación recursiva coincide con la iterativa
    assert factorial(base) == factorial_iterative(base)
    assert factorial(base) == factorial_compare


@pytest.mark.parametrize("n,expected_relation", [
    (2, True),
    (3, True),
    (4, True),
    (5, True),
    (6, True),
    (7, True),
    (8, True),
    (9, True),
])
def test_factorial_mathematical_properties(n, expected_relation):
    """Test para verificar propiedades matemáticas del factorial"""
    # n! = n * (n-1)! y 0! = 1! = 1
    assert (factorial(n) == n * factorial(n - 1)) == expected_relation
    assert factorial(0) == factorial(1) == 1
