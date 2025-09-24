"""Tests para RETO #004: ¿ES UN NÚMERO PRIMO?"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                  # pylint: disable=wrong-import-position
from reto_004 import es_primo  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("numero", [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
])
def test_numeros_primos(numero):
    """Test parametrizado para números que SÍ son primos"""
    assert es_primo(numero), f"{numero} debería ser primo"


@pytest.mark.parametrize("numero", [
    4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36
])
def test_numeros_no_primos(numero):
    """Test parametrizado para números que NO son primos"""
    assert not es_primo(numero), f"{numero} no debería ser primo"


@pytest.mark.parametrize("numero", [-5, -1, 0, 1])
def test_casos_especiales(numero):
    """Test parametrizado para casos especiales (números <= 1)"""
    assert not es_primo(numero), f"{numero} no debería ser primo"


@pytest.mark.parametrize("numero", [4, 9, 16, 25, 36, 49, 64, 81, 100])
def test_cuadrados_perfectos(numero):
    """Test parametrizado para cuadrados perfectos (no son primos excepto casos especiales)"""
    assert not es_primo(numero), f"{numero} es un cuadrado perfecto y no debería ser primo"


@pytest.mark.parametrize("numero,es_primo_esperado", [
    (2, True),   # Único número primo par
    (4, False),  # Primer número par no primo
])
def test_numero_2_es_primo(numero, es_primo_esperado):
    """Test específico para el 2 (único número primo par) y verificación con 4"""
    assert es_primo(numero) == es_primo_esperado


@pytest.mark.parametrize("rango_inicio,rango_fin,primos_esperados", [
    (1, 101, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
])
def test_primos_entre_1_y_100(rango_inicio, rango_fin, primos_esperados):
    """Test para verificar que hay exactamente 25 primos entre 1 y 100"""
    primos_encontrados = []
    for numero in range(rango_inicio, rango_fin):
        if es_primo(numero):
            primos_encontrados.append(numero)

    assert primos_encontrados == primos_esperados
    assert len(primos_encontrados) == 25
