"""Tests para RETO #013: DETECCIÓN DE PALÍNDROMOS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest  # pylint: disable=wrong-import-position
from reto_013 import remove_non_chars, is_palindrome  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("input_str,expected", [
    # Casos básicos
    ("Ana", "Ana"),
    ("A man, a plan, a canal: Panama", "AmanaplanacanalPanama"),

    # Casos con acentos
    ("Aérea", "Aerea"),
    ("¿Será lodo o dólares?", "Seralodoodolares"),

    # Casos con espacios y puntuación
    ("No 'x' in Nixon", "NoxinNixon"),
    ("¡Hola, mundo!", "Holamundo"),

    # Casos especiales
    ("", ""),  # Cadena vacía
    ("123", "123"),  # Solo números
    ("   ", ""),  # Solo espacios
])
def test_remove_non_chars(input_str, expected):
    """Test para eliminar caracteres no alfabéticos"""
    assert remove_non_chars(input_str) == expected


@pytest.mark.parametrize("text,expected", [
    # Palíndromos simples
    ("Ana", True),
    ("Aérea", True),
    ("Erigiré", True),
    ("Orejero", True),

    # Palíndromos con espacios y puntuación
    ("Ana lleva al oso la avellana", True),
    ("A man, a plan, a canal: Panama", True),
    ("No 'x' in Nixon", True),
    ("¿Será lodo o dólares?", True),
    ("Dábale arroz a la zorra el abad", True),

    # No palíndromos
    ("Amar", False),
    ("Aéreo", False),
    ("Ovejero", False),
    ("Sillones", False),
    ("Mi carro me lo robaron", False),
    ("Rey va Javier", False),

    # Casos especiales
    ("", True),     # Cadena vacía es palíndromo
    ("a", True),    # Un solo carácter es palíndromo
    ("A", True),    # Un solo carácter mayúscula
    ("aa", True),   # Dos caracteres iguales
    ("ab", False),  # Dos caracteres diferentes

    # Casos con mayúsculas/minúsculas
    ("ANA", True),
    ("AbA", True),
    ("ABC", False),
])
def test_is_palindrome(text, expected):
    """Test para verificar si un texto es palíndromo"""
    assert is_palindrome(text) == expected


@pytest.mark.parametrize("text,expected", [
    ("Ana", True),
    ("ANA", True),
    ("ana", True),
    ("aNa", True),
])
def test_is_palindrome_case_insensitive(text, expected):
    """Test para verificar que la función sea insensible a mayúsculas/minúsculas"""
    assert is_palindrome(text) == expected


@pytest.mark.parametrize("text1,text2,expected", [
    ("Aérea", "Aerea", True),
    ("¿Será lodo o dólares?", "Sera lodo o dolares", True),
])
def test_is_palindrome_ignores_accents(text1, text2, expected):
    """Test para verificar que la función ignore acentos"""
    # Ambos textos deben ser palíndromos equivalentes
    assert is_palindrome(text1) == expected
    assert is_palindrome(text2) == expected
