"""Tests para RETO #030: ORDENA LA LISTA"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                       # pylint: disable=wrong-import-position
from reto_030 import order_numbers  # pylint: disable=import-error,wrong-import-position # type: ignore


# Tests para casos válidos
@pytest.mark.parametrize("input_list,order,expected_result", [
    # Casos básicos de ordenación
    ([2, 4, 6, 8, 9], "Asc", [2, 4, 6, 8, 9]),
    ([2, 4, 6, 8, 9], "Desc", [9, 8, 6, 4, 2]),

    # Listas desordenadas
    ([2, 4, 6, 8, 9, 1, 3, 5, 7], "Asc", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([2, 4, 6, 8, 9, 1, 3, 5, 7], "Desc", [9, 8, 7, 6, 5, 4, 3, 2, 1]),

    # Listas en orden inverso
    ([9, 8, 6, 4, 2], "Asc", [2, 4, 6, 8, 9]),
    ([9, 8, 6, 4, 2], "Desc", [9, 8, 6, 4, 2]),

    # Casos complejos
    ([7, 5, 3, 1, 9, 8, 6, 4, 2], "Asc", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([7, 5, 3, 1, 9, 8, 6, 4, 2], "Desc", [9, 8, 7, 6, 5, 4, 3, 2, 1]),

    # Listas ya ordenadas
    ([1, 2, 3, 4, 5], "Asc", [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], "Desc", [5, 4, 3, 2, 1]),

    # Casos especiales
    ([], "Asc", []),      # Lista vacía
    ([42], "Asc", [42]),  # Un solo elemento
])
def test_valid_cases(input_list, order, expected_result):
    """Test para casos válidos de ordenación"""
    result = order_numbers(input_list, order)
    assert result == expected_result


# Tests para casos inválidos que deben lanzar excepciones
@pytest.mark.parametrize("input_list,order,expected_exception,expected_message", [
    ([2, 4.0, 6, 8.1, 9], "Asc", TypeError, "debe contener solo números enteros"),
    ([2, 4, 6, 8, 9], "Random order", ValueError, 'El orden debe ser "Asc" o "Desc"'),
])
def test_invalid_cases(input_list, order, expected_exception, expected_message):
    """Test para casos inválidos que deben lanzar excepciones"""
    with pytest.raises(expected_exception, match=expected_message):
        order_numbers(input_list, order)


@pytest.mark.parametrize("original_list,order", [
    ([7, 5, 3, 1, 9, 8, 6, 4, 2], "Asc"),
])
def test_original_list_not_modified(original_list, order):
    """Verificar que la lista original no se modifica"""
    original_copy = original_list[:]
    order_numbers(original_list, order)
    assert original_list == original_copy
