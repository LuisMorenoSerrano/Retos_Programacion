"""Tests para RETO #001: EL FAMOSO "FIZZ BUZZ" """
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                   # pylint: disable=wrong-import-position
from reto_001 import fizz_buzz  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("start,end,expected", [
    # Casos básicos
    (1, 15, ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz",
             "buzz", "11", "fizz", "13", "14", "fizzbuzz"]),
    (10, 16, ["buzz", "11", "fizz", "13", "14", "fizzbuzz", "16"]),

    # Un solo número
    (1, 1, ["1"]),
    (3, 3, ["fizz"]),
    (5, 5, ["buzz"]),
    (15, 15, ["fizzbuzz"]),

    # Múltiplos específicos
    (3, 9, ["fizz", "4", "buzz", "fizz", "7", "8", "fizz"]),  # múltiplos de 3
    (5, 10, ["buzz", "fizz", "7", "8", "fizz", "buzz"]),      # múltiplos de 5
])
def test_fizz_buzz_parametrized(start, end, expected):
    """Test parametrizado para fizz_buzz con diferentes rangos"""
    resultado = fizz_buzz(start, end)
    assert resultado == expected


@pytest.mark.parametrize("expected_len,pos_3,pos_5,pos_15,pos_100", [
    (100, "fizz", "buzz", "fizzbuzz", "buzz"),  # Rango original 1-100
])
def test_fizz_buzz_rango_original(expected_len, pos_3, pos_5, pos_15, pos_100):
    """Test para verificar que el rango original (1-100) funciona"""
    resultado = fizz_buzz()                # Sin parámetros usa 1-100
    assert len(resultado) == expected_len
    assert resultado[2] == pos_3           # posición 2 = número 3
    assert resultado[4] == pos_5           # posición 4 = número 5
    assert resultado[14] == pos_15         # posición 14 = número 15
    assert resultado[99] == pos_100        # posición 99 = número 100


@pytest.mark.parametrize("numero,esperado", [
    (3, "fizz"), (6, "fizz"), (9, "fizz"), (12, "fizz"),
    (5, "buzz"), (10, "buzz"), (20, "buzz"), (25, "buzz"),
    (15, "fizzbuzz"), (30, "fizzbuzz"), (45, "fizzbuzz"),
    (1, "1"), (2, "2"), (4, "4"), (7, "7"), (8, "8"),
])
def test_fizz_buzz_casos_individuales(numero, esperado):
    """Test para casos individuales específicos"""
    resultado = fizz_buzz(numero, numero)
    assert resultado == [esperado]
