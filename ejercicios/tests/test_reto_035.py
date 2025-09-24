"""Tests para RETO #035: LOS NÚMEROS PERDIDOS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                              # pylint: disable=wrong-import-position
from reto_035 import find_missing_numbers  # pylint: disable=import-error,wrong-import-position # type: ignore


# Tests para casos válidos
@pytest.mark.parametrize("input_array,expected_result", [
    # Casos básicos con números perdidos
    ([1, 2, 4, 6], [3, 5]),
    ([1, 3, 5, 7, 9], [2, 4, 6, 8]),
    ([2, 4, 7, 8, 10], [3, 5, 6, 9]),
    ([1, 5], [2, 3, 4]),
    ([10, 11, 12, 15, 16, 18, 19], [13, 14, 17]),

    # Casos sin números perdidos
    ([1, 2, 3, 4, 5], []),
    ([100], []),

    # Casos especiales
    ([-5, -3, -1], [-4, -2]),                  # Números negativos
    ([1000, 1002, 1005], [1001, 1003, 1004]),  # Números grandes
])
def test_valid_cases(input_array, expected_result):
    """Test para casos válidos de números perdidos"""
    result = find_missing_numbers(input_array)
    assert result == expected_result


# Tests para casos inválidos que deben lanzar excepciones
@pytest.mark.parametrize("input_array,expected_exception,expected_message", [
    ([], ValueError, "El array no puede estar vacío"),
    ([1, 3, 2, 4], ValueError, "debe estar ordenado"),
    ([1, 2, 2, 4], ValueError, "no puede contener números repetidos"),
    ([1, 2.5, 4], TypeError, "debe contener solo números enteros"),
])
def test_invalid_cases(input_array, expected_exception, expected_message):
    """Test para casos inválidos que deben lanzar excepciones"""
    with pytest.raises(expected_exception, match=expected_message):
        find_missing_numbers(input_array)


# Para ejecutar directamente este archivo de tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
