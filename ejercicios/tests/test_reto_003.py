"""Tests para RETO #003: LA SUCESIÓN DE FIBONACCI"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                   # pylint: disable=wrong-import-position
from reto_003 import fibonacci  # pylint: disable=import-error,wrong-import-position # type: ignore


# Tests para casos válidos de la sucesión de Fibonacci
@pytest.mark.parametrize("numero,expected_result", [
    # Casos básicos
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 1]),
    (3, [0, 1, 1, 2]),
    (4, [0, 1, 1, 2, 3]),
    (5, [0, 1, 1, 2, 3, 5]),
    (6, [0, 1, 1, 2, 3, 5, 8]),
    (7, [0, 1, 1, 2, 3, 5, 8, 13]),

    # Casos más largos
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
    (15, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]),
])
def test_fibonacci_sequence(numero, expected_result):
    """Test para verificar la correcta generación de la secuencia de Fibonacci"""
    result = fibonacci(numero)
    assert result == expected_result


@pytest.mark.parametrize("expected_len,first_val,second_val,third_val,last_val", [
    (50, 0, 1, 1, 7778742049),  # Valor por defecto: 49 números, 50 elementos
])
def test_fibonacci_default(expected_len, first_val, second_val, third_val, last_val):
    """Test para verificar el valor por defecto (49 números, 50 elementos)"""
    result = fibonacci()
    assert len(result) == expected_len
    assert result[0] == first_val
    assert result[1] == second_val
    assert result[2] == third_val
    assert result[49] == last_val       # Fibonacci(49)


@pytest.mark.parametrize("num_elements", [
    (5), (10), (15), (20),
])
def test_fibonacci_properties(num_elements):
    """Test para verificar propiedades matemáticas de Fibonacci"""
    fib_sequence = fibonacci(num_elements)

    # Verificar que cada número (después de los dos primeros) es la suma de los dos anteriores
    for i in range(2, len(fib_sequence)):
        assert fib_sequence[i] == fib_sequence[i-1] + fib_sequence[i-2]


@pytest.mark.parametrize("num_large,expected_len,min_last_value", [
    (50, 51, 10**10),    # 50 números debe tener 51 elementos
    (100, 101, 10**20),  # 100 números debe tener 101 elementos y último muy grande
])
def test_fibonacci_large_numbers(num_large, expected_len, min_last_value):
    """Test para verificar que funciona con números grandes"""
    result = fibonacci(num_large)
    assert len(result) == expected_len
    # Verificar que el último número es muy grande (Fibonacci crece exponencialmente)
    assert result[num_large] > min_last_value
