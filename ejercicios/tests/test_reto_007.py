"""Tests para RETO #007: INVIRTIENDO CADENAS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                       # pylint: disable=wrong-import-position
from reto_007 import invert_string  # pylint: disable=import-error,wrong-import-position # type: ignore


# Tests para inversión de cadenas
@pytest.mark.parametrize("input_string,expected_result", [
    # Casos básicos
    ("Hola mundo", "odnum aloH"),
    ("Esto es una prueba de inversión de cadenas", "sanedac ed nóisrevni ed abeurp anu se otsE"),

    # Casos especiales
    ("", ""),              # Cadena vacía
    ("a", "a"),            # Un solo carácter
    ("Python", "nohtyP"),
    ("12345", "54321"),

    # Casos con caracteres especiales
    ("¡Hola!", "!aloH¡"),
    ("Niño", "oñiN"),
    ("Año 2024", "4202 oñA"),

    # Casos con espacios
    ("   ", "   "),        # Solo espacios
    (" Hola ", " aloH "),  # Espacios al inicio y final

    # Palíndromos
    ("oso", "oso"),
    ("radar", "radar"),
])
def test_invert_string(input_string, expected_result):
    """Test para inversión de cadenas de texto"""
    result = invert_string(input_string)
    assert result == expected_result


@pytest.mark.parametrize("original", [
    ("Esta es una prueba"),
    ("Hola mundo"),
    ("12345"),
    ("Python"),
    ("a"),
    (""),
])
def test_double_inversion(original):
    """Test para verificar que invertir dos veces devuelve la cadena original"""
    inverted_once = invert_string(original)
    inverted_twice = invert_string(inverted_once)
    assert inverted_twice == original


@pytest.mark.parametrize("text", [
    ("Hola mundo"),
    ("Python es genial"),
    ("12345"),
    ("a"),
])
def test_inversion_properties(text):
    """Test para verificar propiedades de la inversión"""
    inverted = invert_string(text)

    # La longitud debe ser la misma
    assert len(inverted) == len(text)

    # El primer carácter original debe ser el último en la inversión
    if text:
        assert text[0] == inverted[-1]
        assert text[-1] == inverted[0]
