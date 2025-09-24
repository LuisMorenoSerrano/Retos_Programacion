"""Tests para RETO #033: EL SEGUNDO MÁS GRANDE"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                            # pylint: disable=wrong-import-position
from reto_033 import get_second_largest  # pylint: disable=import-error,wrong-import-position # type: ignore


# Tests para casos válidos
@pytest.mark.parametrize("input_list,expected_result", [
    # Casos básicos
    ([1, 2], 1),
    ([100, 50], 50),
    ([50, 100], 50),

    # Listas ordenadas
    ([1, 2, 3, 4, 5], 4),
    ([5, 4, 3, 2, 1], 4),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 9),

    # Listas desordenadas
    ([3, 7, 9, 4, 5, 8, 1], 8),

    # Listas con duplicados (pero al menos 2 números diferentes)
    ([3, 7, 9, 4, 5, 8, 1, 9, 7], 8),

    # Números negativos
    ([-5, -2, -8, -1, -10], -2),

    # Mezcla de positivos y negativos
    ([-5, 10, -2, 8, -1], 8),
])
def test_valid_cases(input_list, expected_result):
    """Test para casos válidos del segundo número más grande"""
    result = get_second_largest(input_list)
    assert result == expected_result


# Tests para casos inválidos que deben lanzar excepciones
@pytest.mark.parametrize("input_list", [
    [3],              # Un solo elemento
    [5, 5],           # Todos iguales (2 elementos)
    [1, 1, 1, 1, 1],  # Todos iguales (múltiples elementos)
    [42, 42, 42],     # Todos iguales (3 elementos)
])
def test_invalid_cases(input_list):
    """Test para casos inválidos que deben lanzar excepciones"""
    with pytest.raises(ValueError, match="debe contener al menos dos números diferentes"):
        get_second_largest(input_list)


# Para ejecutar directamente este archivo de tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
