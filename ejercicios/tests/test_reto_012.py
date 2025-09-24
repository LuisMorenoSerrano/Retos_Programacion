"""Tests para RETO #012: ELIMINANDO CARACTERES ÚNICOS ENTRE CADENAS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest  # pylint: disable=wrong-import-position
from reto_012 import remove_accents, find_chars_non_common  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("input_str,expected", [
    ("Murciélago", "Murcielago"),
    ("José María", "Jose Maria"),
    ("ñáéíóúü", "naeiouu"),
    ("Niño pequeño", "Nino pequeno"),
    ("café", "cafe"),
    ("", ""),  # Cadena vacía
    ("sin acentos", "sin acentos"),  # Sin acentos
])
def test_remove_accents(input_str, expected):
    """Test para eliminar acentos de una cadena"""
    assert remove_accents(input_str) == expected


@pytest.mark.parametrize("str1,str2,expected", [
    # Casos básicos
    ("Murciélago", "Mariposa", "ucelg"),
    ("Mariposa", "Murciélago", "ps"),

    # Casos con espacios
    ("Me gusta Python", "Me gusta Rust", "pyhon"),
    ("Me gusta Rust", "Me gusta Python", "r"),

    # Casos con repeticiones
    ("Colega", "Legado", "c"),
    ("Legado", "Colega", "d"),

    # Casos especiales
    ("abc", "def", "abc"),  # Sin caracteres comunes
    ("abc", "abc", ""),     # Cadenas iguales
    ("ABC", "abc", ""),     # Diferentes mayúsculas/minúsculas
    ("", "abc", ""),        # Cadena vacía como primer parámetro
    ("abc", "", "abc"),     # Cadena vacía como segundo parámetro
    ("", "", ""),           # Ambas cadenas vacías

    # Casos con acentos
    ("José", "Jose", ""),   # Acentos normalizados
    ("café", "cafe", ""),   # Acentos normalizados
])
def test_find_chars_non_common(str1, str2, expected):
    """Test para encontrar caracteres únicos entre dos cadenas"""
    assert find_chars_non_common(str1, str2) == expected


@pytest.mark.parametrize("str1,str2,expected", [
    ("ABC", "abc", ""),
    ("AbC", "aBc", ""),
    ("HELLO", "hello", ""),
])
def test_find_chars_non_common_case_insensitive(str1, str2, expected):
    """Test para verificar que la función sea insensible a mayúsculas"""
    assert find_chars_non_common(str1, str2) == expected


@pytest.mark.parametrize("str1,str2,expected", [
    # Si un carácter aparece múltiples veces en str1, debe aparecer múltiples veces en la salida
    ("aaa", "b", "aaa"),
    ("hello", "world", "he"),
])
def test_find_chars_non_common_preserves_duplicates(str1, str2, expected):
    """Test para verificar que se preservan caracteres duplicados"""
    assert find_chars_non_common(str1, str2) == expected
