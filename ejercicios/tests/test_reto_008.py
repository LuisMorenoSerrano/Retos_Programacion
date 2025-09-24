"""Tests para RETO #008: CONTANDO PALABRAS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                     # pylint: disable=wrong-import-position
from reto_008 import count_words  # pylint: disable=import-error,wrong-import-position # type: ignore


# Tests para casos básicos
@pytest.mark.parametrize("text,expected_result", [
    # Caso simple
    ("hola mundo", {"hola": 1, "mundo": 1}),

    # Palabras repetidas
    ("hola mundo hola", {"hola": 2, "mundo": 1}),

    # Mayúsculas y minúsculas
    ("Hola HOLA hola", {"hola": 3}),

    # Con signos de puntuación
    ("hola, mundo! ¿hola?", {"hola": 2, "mundo": 1}),

    # Texto vacío
    ("", {}),

    # Solo espacios y puntuación
    ("   !!! ??? ", {}),
])
def test_count_words_basic(text, expected_result):
    """Test para casos básicos de conteo de palabras"""
    result = count_words(text)
    assert result == expected_result


@pytest.mark.parametrize("text,expected_order", [
    ("python java python c python java", ["python", "java", "c"]),
    ("a b c a b a", ["a", "b", "c"]),
])
def test_count_words_ordering(text, expected_order):
    """Test para verificar el ordenamiento correcto (frecuencia desc, alfabético asc)"""
    result = count_words(text)
    keys_list = list(result.keys())

    # Verificar el orden esperado
    assert keys_list == expected_order


@pytest.mark.parametrize("text,expected_alphabetical", [
    ("zebra apple banana", ["apple", "banana", "zebra"]),
    ("casa perro gato", ["casa", "gato", "perro"]),
])
def test_count_words_same_frequency_alphabetical(text, expected_alphabetical):
    """Test para verificar ordenamiento alfabético cuando hay misma frecuencia"""
    result = count_words(text)
    keys_list = list(result.keys())

    # Todas tienen frecuencia 1, deben aparecer alfabéticamente
    assert keys_list == expected_alphabetical


# Tests con casos complejos
@pytest.mark.parametrize("text,expected_first_word,expected_first_count", [
    ("Python es Python. Python programa", "python", 3),
    ("a b c d e a b c a b a", "a", 4),
    ("Test! test? TEST.", "test", 3),
])
def test_count_words_complex(text, expected_first_word, expected_first_count):
    """Test para casos complejos verificando la palabra más frecuente"""
    result = count_words(text)
    first_key = next(iter(result))
    first_value = result[first_key]

    assert first_key == expected_first_word
    assert first_value == expected_first_count


@pytest.mark.parametrize("text,expected_words", [
    ("word1 word-2 word_3 word4's", {"word1", "word", "2", "word_3", "word4", "s"}),
])
def test_count_words_regex_behavior(text, expected_words):
    """Test para verificar el comportamiento del regex con caracteres especiales"""
    result = count_words(text)

    # Solo deben extraerse las palabras válidas (letras y números)
    assert set(result.keys()) == expected_words


@pytest.mark.parametrize("text,expected_results", [
    ("niño niña niño", {"niño": 2, "niña": 1}),
])
def test_count_words_unicode(text, expected_results):
    """Test para verificar manejo de caracteres unicode"""
    result = count_words(text)

    for word, count in expected_results.items():
        assert result[word] == count
