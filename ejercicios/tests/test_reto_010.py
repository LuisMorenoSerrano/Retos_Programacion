"""Tests para RETO #010: CÓDIGO MORSE"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                                                # pylint: disable=wrong-import-position
from reto_010 import is_morse, text_to_morse, morse_to_text  # pylint: disable=import-error,wrong-import-position # type: ignore


# Tests para detección de código Morse
@pytest.mark.parametrize("text,expected", [
    # Casos que SÍ son código Morse
    ("... --- ...", True),   # SOS
    (".- -... -.-.", True),  # ABC
    (".  ..", True),         # EI con espacios
    ("", True),              # Cadena vacía
    (".", True),             # Solo un punto
    ("-", True),             # Solo una raya
    ("  ", True),            # Solo espacios

    # Casos que NO son código Morse
    ("Hola", False),   # Texto normal
    ("123", False),    # Solo números (no en código morse)
    (".-a", False),    # Mezcla
    (".-.-+", False),  # Caracteres inválidos
])
def test_is_morse(text, expected):
    """Test para detectar si un texto es código Morse"""
    assert is_morse(text) is expected


# Tests para conversión de texto a Morse
@pytest.mark.parametrize("text,expected", [
    ("SOS", "... --- ..."),
    ("ABC", ".- -... -.-."),
    ("Hola", ".... --- .-.. .-"),
    ("123", ".---- ..--- ...--"),
    ("A", ".-"),
    ("", ""),
])
def test_text_to_morse(text, expected):
    """Test para conversión de texto a código Morse"""
    result = text_to_morse(text)
    assert result == expected


# Tests para conversión de Morse a texto
@pytest.mark.parametrize("morse,expected", [
    ("... --- ...", "SOS"),
    (".- -... -.-.", "ABC"),
    (".... --- .-.. .-", "HOLA"),
    (".---- ..--- ...--", "123"),
    (".-", "A"),
    ("", ""),

    # Casos con múltiples palabras (doble espacio)
    (".... --- .-.. .-  -- ..- -. -.. ---", "HOLA MUNDO"),
])
def test_morse_to_text(morse, expected):
    """Test para conversión de código Morse a texto"""
    result = morse_to_text(morse)
    assert result == expected


# Tests bidireccionales
@pytest.mark.parametrize("original_text", [
    "HOLA",
    "MUNDO",
    "PYTHON",
    "CODIGO MORSE",
    "SOS",
    "ABC123",
])
def test_bidirectional_conversion(original_text):
    """Test para verificar que la conversión ida y vuelta mantiene el texto original"""
    morse = text_to_morse(original_text)
    converted_back = morse_to_text(morse)
    assert converted_back == original_text.upper()


@pytest.mark.parametrize("text,expected_morse_contains", [
    ("HOLA.", ".-.-.-"),  # El punto debe estar en el resultado
])
def test_special_characters(text, expected_morse_contains):
    """Test para caracteres especiales soportados"""
    morse = text_to_morse(text)
    assert expected_morse_contains in morse

    converted_back = morse_to_text(morse)
    assert converted_back == text


@pytest.mark.parametrize("text,expected_morse", [
    ("HOLA@#", ".... --- .-.. .-  "),  # Caracteres no soportados resultan en espacios
])
def test_unsupported_characters(text, expected_morse):
    """Test para caracteres no soportados (deben ser ignorados)"""
    morse = text_to_morse(text)
    # Los caracteres no soportados deben resultar en espacios vacíos
    assert morse == expected_morse


@pytest.mark.parametrize("upper_text,lower_text,mixed_text", [
    ("HOLA", "hola", "HoLa"),
    ("SOS", "sos", "SoS"),
])
def test_case_insensitive(upper_text, lower_text, mixed_text):
    """Test para verificar que la conversión es insensible a mayúsculas/minúsculas"""
    upper_morse = text_to_morse(upper_text)
    lower_morse = text_to_morse(lower_text)
    mixed_morse = text_to_morse(mixed_text)

    # Todos deben producir el mismo código Morse
    assert upper_morse == lower_morse == mixed_morse


@pytest.mark.parametrize("text_with_accents,expected_result", [
    ("NIÑO", "NINO"),
])
def test_accented_characters(text_with_accents, expected_result):
    """Test para verificar manejo de caracteres acentuados"""
    morse = text_to_morse(text_with_accents)
    converted_back = morse_to_text(morse)

    # Los acentos deben ser removidos por unidecode
    assert converted_back == expected_result
