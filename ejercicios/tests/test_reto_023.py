"""Tests para RETO #023: CONJUNTOS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest  # pylint: disable=wrong-import-position
from reto_023 import compare_lists  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("list1,list2,find_common,expected", [
    # Elementos comunes
    ([1, 3, 5, 7, 9], [1, 2, 3, 5, 8, 13], True, [1, 3, 5]),
    ([1, 2, 2, 3, 4, 5], [2, 3, 3, 5, 6, 7], True, [2, 3, 5]),
    (["sopa", 23, "avión", "j", 13.25], ["avión", "colega", 0, 13.15, 23, 12], True, [23, "avión"]),

    # Elementos no comunes
    ([1, 3, 5, 7, 9], [1, 2, 3, 5, 8, 13], False, [7, 9, 2, 8, 13]),
    ([1, 2, 2, 3, 4, 5], [2, 3, 3, 5, 6, 7], False, [1, 4, 6, 7]),
    (["sopa", 23, "avión", "j", 13.25],
     ["avión", "colega", 0, 13.15, 23, 12],
     False,
     ["sopa", "j", 13.25, "colega", 0, 13.15, 12]),
])
def test_compare_lists_parametrized(list1, list2, find_common, expected):
    """Test parametrizado para compare_lists"""
    resultado = compare_lists(list1, list2, find_common)
    assert resultado == expected


@pytest.mark.parametrize("list1,list2", [
    ([], []),
    ([1, 2, 3], []),
    ([], [4, 5, 6]),
])
def test_listas_vacias_comunes(list1, list2):
    """Test parametrizado para listas vacías buscando comunes"""
    resultado = compare_lists(list1, list2, True)
    assert resultado == []


@pytest.mark.parametrize("list1,list2,expected", [
    ([1, 2, 3], [], [1, 2, 3]),
    ([], [4, 5, 6], [4, 5, 6]),
    ([], [], []),
])
def test_listas_vacias_no_comunes(list1, list2, expected):
    """Test parametrizado para listas vacías buscando no comunes"""
    resultado = compare_lists(list1, list2, False)
    assert resultado == expected


@pytest.mark.parametrize("lista", [
    [1, 2, 3, 4],
    ["a", "b", "c"],
    [1.5, 2.5, 3.5],
])
def test_listas_identicas(lista):
    """Test parametrizado para listas idénticas"""
    # Comunes: todos los elementos
    resultado_comunes = compare_lists(lista, lista, True)
    assert resultado_comunes == lista

    # No comunes: lista vacía
    resultado_no_comunes = compare_lists(lista, lista, False)
    assert resultado_no_comunes == []


@pytest.mark.parametrize("list1,list2", [
    ([1, 3, 5], [2, 4, 6]),
    (["a", "c"], ["b", "d"]),
    ([1.1, 2.2], [3.3, 4.4]),
])
def test_listas_sin_elementos_comunes(list1, list2):
    """Test parametrizado para listas completamente diferentes"""
    # Comunes: lista vacía
    resultado_comunes = compare_lists(list1, list2, True)
    assert resultado_comunes == []

    # No comunes: todos los elementos de ambas listas
    resultado_no_comunes = compare_lists(list1, list2, False)
    expected = list1 + list2
    assert resultado_no_comunes == expected
