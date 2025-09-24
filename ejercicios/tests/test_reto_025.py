"""Tests para RETO #025: ITERATION MASTER"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                                                          # pylint: disable=wrong-import-position
from reto_025 import count_01, count_02, count_03, count_04, count_05  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("start,end,expected", [
    (1, 5, [1, 2, 3, 4, 5]),
    (10, 15, [10, 11, 12, 13, 14, 15]),
    (1, 1, [1]),
    (50, 53, [50, 51, 52, 53]),
])
def test_count_functions_different_ranges(start, end, expected):
    """Test para todas las funciones de conteo con diferentes rangos"""
    # Verificar que todas las funciones producen el mismo resultado
    assert count_01(start, end) == expected
    assert count_02(start, end) == expected
    assert count_03(start, end) == expected
    assert count_04(start, end) == expected
    assert count_05(start, end) == expected


@pytest.mark.parametrize("count_function", [count_01, count_02, count_03, count_04, count_05])
def test_count_functions_rango_original(count_function):
    """Test parametrizado para verificar que todas las funciones manejan el rango original 1-100"""
    resultado = count_function()  # Sin parámetros
    expected = list(range(1, 101))
    assert resultado == expected
    assert len(resultado) == 100


@pytest.mark.parametrize("count_function", [count_01, count_02, count_03, count_04, count_05])
def test_count_functions_casos_especiales(count_function):
    """Test parametrizado para casos especiales"""
    # Números grandes
    resultado_grandes = count_function(95, 100)
    expected_grandes = [95, 96, 97, 98, 99, 100]
    assert resultado_grandes == expected_grandes

    # Un solo número
    resultado_solo = count_function(42, 42)
    expected_solo = [42]
    assert resultado_solo == expected_solo


@pytest.mark.parametrize("start,end", [
    (1, 10), (20, 25), (1, 100), (50, 60)
])
def test_consistency_between_methods(start, end):
    """Test para verificar que todos los métodos producen el mismo resultado"""
    # Obtener resultado de la primera función como referencia
    expected = count_01(start, end)

    # Verificar que todas las demás funciones produzcan el mismo resultado
    assert count_02(start, end) == expected, f"count_02 falló para rango ({start}, {end})"
    assert count_03(start, end) == expected, f"count_03 falló para rango ({start}, {end})"
    assert count_04(start, end) == expected, f"count_04 falló para rango ({start}, {end})"
    assert count_05(start, end) == expected, f"count_05 falló para rango ({start}, {end})"
