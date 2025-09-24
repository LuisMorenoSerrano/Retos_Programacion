"""Tests para RETO #017: CAPITALIZAR PRIMERA LETRA DE CADA PALABRA"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest  # pylint: disable=wrong-import-position
from reto_017 import capitalize  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("input_text,expected", [
    # Casos básicos
    ("hola", "Hola"),
    ("adiós", "Adiós"),
    ("hello world", "Hello World"),

    # Casos con múltiples palabras
    ("mi carro me lo robaron", "Mi Carro Me Lo Robaron"),
    ("Es una prueba de Fuego", "Es Una Prueba De Fuego"),
    ("era una noche de luna y sin embargo llovía.", "Era Una Noche De Luna Y Sin Embargo Llovía."),

    # Casos especiales
    ("", ""),  # Cadena vacía
    ("   ", ""),  # Solo espacios
    ("a", "A"),  # Una sola letra
    ("A", "A"),  # Ya está en mayúscula

    # Casos con espacios múltiples
    ("hello  world", "Hello World"),  # Espacios dobles
    ("  hello   world  ", "Hello World"),  # Espacios al inicio y final

    # Casos con caracteres especiales
    ("hello-world", "Hello-World"),  # Con guión (no se separa)
    ("hello_world", "Hello_World"),  # Con guión bajo (no se separa)
    ("hello.world", "Hello.World"),  # Con punto (no se separa)

    # Casos con números
    ("word1 word2", "Word1 Word2"),
    ("test123 abc456", "Test123 Abc456"),

    # Casos con acentos y caracteres especiales
    ("josé maría", "José María"),
    ("niño pequeño", "Niño Pequeño"),
    ("café con leche", "Café Con Leche"),

    # Casos con mayúsculas y minúsculas mezcladas
    ("hOlA mUnDo", "Hola Mundo"),
    ("tEST cASE", "Test Case"),
    ("PyThOn PrOgRaMmInG", "Python Programming"),
])
def test_capitalize(input_text, expected):
    """Test para capitalizar primera letra de cada palabra"""
    assert capitalize(input_text) == expected


@pytest.mark.parametrize("input_text,expected", [
    # Los caracteres no alfabéticos al inicio de palabra deberían permanecer
    ("123abc def456", "123Abc Def456"),
    ("!hello @world", "!Hello @World"),
    ("#hashtag $money", "#Hashtag $Money"),
])
def test_capitalize_preserves_non_alphabetic(input_text, expected):
    """Test para verificar que se preservan caracteres no alfabéticos"""
    assert capitalize(input_text) == expected


@pytest.mark.parametrize("input_text,expected", [
    # Palabras de una sola letra
    ("a b c d", "A B C D"),
    # Mezcla de mayúsculas y minúsculas
    ("HELLO world", "Hello World"),
    ("hello WORLD", "Hello World"),
    # Solo consonantes/vocales
    ("bcdfg aeiou", "Bcdfg Aeiou"),
])
def test_capitalize_edge_cases(input_text, expected):
    """Test para casos límite"""
    assert capitalize(input_text) == expected


@pytest.mark.parametrize("input_text,expected", [
    # Múltiples espacios deben colapsar a uno
    ("word1    word2", "Word1 Word2"),
    ("   word1   word2   ", "Word1 Word2"),
    # Tabulaciones y otros espacios en blanco
    ("word1\tword2", "Word1 Word2"),
    ("word1\nword2", "Word1 Word2"),
])
def test_capitalize_whitespace_normalization(input_text, expected):
    """Test para verificar normalización de espacios en blanco"""
    assert capitalize(input_text) == expected
