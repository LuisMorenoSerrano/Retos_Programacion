"""Tests para RETO #031: MARCO DE PALABRAS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                                            # pylint: disable=wrong-import-position
from reto_031 import print_frame_border, stacking_words  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("length,expected", [
    (5, "*********\n"),  # 5 + 4 = 9 asteriscos
])
def test_print_frame_border(length, expected, capsys):
    """Test de la función print_frame_border"""
    print_frame_border(length)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize("length,expected_stars", [
    (0, 4),    # 0 + 4 = 4 asteriscos
    (1, 5),    # 1 + 4 = 5 asteriscos
    (3, 7),    # 3 + 4 = 7 asteriscos
    (10, 14),  # 10 + 4 = 14 asteriscos
])
def test_print_frame_border_different_lengths(length, expected_stars, capsys):
    """Test de print_frame_border con diferentes longitudes"""
    print_frame_border(length)
    captured = capsys.readouterr()
    expected = "*" * expected_stars + "\n"
    assert captured.out == expected


@pytest.mark.parametrize("text,expected_lines_count", [
    ("Hola mundo", 4),  # 2 bordes + 2 palabras
])
def test_stacking_words_simple(text, expected_lines_count, capsys):
    """Test básico de stacking_words con texto simple"""
    stacking_words(text)
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    # Verificar estructura del marco
    assert len(lines) == expected_lines_count
    assert lines[0] == "*********"  # Ajustado según la palabra más larga
    assert "Hola " in lines[1]
    assert "mundo" in lines[2]
    assert lines[3] == lines[0]     # Borde inferior igual al superior


@pytest.mark.parametrize("text,expected_words", [
    ("Hola", ["Hola"]),
    ("Hola mundo", ["Hola", "mundo"]),
    ("Un dos tres", ["Un", "dos", "tres"]),
    ("¿Qué te parece el reto?", ["¿Qué", "te", "parece", "el", "reto?"]),
])
def test_stacking_words_word_count(text, expected_words, capsys):
    """Test para verificar que se procesan todas las palabras correctamente"""
    stacking_words(text)
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    # El número de líneas debe ser: 2 bordes + número de palabras
    expected_lines = 2 + len(expected_words)
    assert len(lines) == expected_lines

    # Verificar que cada palabra aparece en su línea correspondiente
    for i, word in enumerate(expected_words):
        word_line = lines[i + 1]  # +1 porque la primera línea es el borde
        assert word in word_line
        assert word_line.startswith("*")
        assert word_line.endswith("*")


@pytest.mark.parametrize("text,expected_lines_count", [
    ("Prueba", 3),  # 2 bordes + 1 palabra
])
def test_stacking_words_single_word(text, expected_lines_count, capsys):
    """Test con una sola palabra"""
    stacking_words(text)
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    assert len(lines) == expected_lines_count
    assert lines[0] == "**********"  # "Prueba" tiene 6 letras, +4 = 10
    assert "* Prueba *" in lines[1]
    assert lines[2] == "**********"


@pytest.mark.parametrize("text,expected_max_length", [
    ("El gato", 4),  # "gato" tiene 4 letras
])
def test_stacking_words_different_lengths(text, expected_max_length, capsys):
    """Test con palabras de diferentes longitudes"""
    stacking_words(text)
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    # La palabra más larga determina el ancho del marco
    expected_border = "*" * (expected_max_length + 4)

    assert lines[0] == expected_border
    assert lines[3] == expected_border

    # Verificar alineación
    assert "El  " in lines[1]  # "El" debe estar alineado a la izquierda
    assert "gato" in lines[2]


@pytest.mark.parametrize("invalid_input", [
    123,   # Número en lugar de string
    None,  # None
    [],    # Lista
    {},    # Diccionario
])
def test_stacking_words_invalid_input(invalid_input):
    """Test con tipos de entrada inválidos"""
    with pytest.raises(TypeError, match="El texto debe ser una cadena de caracteres"):
        stacking_words(invalid_input)


@pytest.mark.parametrize("empty_text", [
    "",
])
def test_stacking_words_empty_string(empty_text):
    """Test con string vacío"""
    # Un string vacío debería generar una excepción por max() de secuencia vacía
    with pytest.raises(ValueError):
        stacking_words(empty_text)


@pytest.mark.parametrize("text,expected_lines", [
    ("A", ["*****", "* A *", "*****"]),
])
def test_stacking_words_single_character(text, expected_lines, capsys):
    """Test con una sola letra"""
    stacking_words(text)
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    assert len(lines) == 3
    assert lines == expected_lines


@pytest.mark.parametrize("text", [
    "¿Hola?",
])
def test_stacking_words_special_characters(text, capsys):
    """Test con caracteres especiales"""
    stacking_words(text)
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    assert len(lines) == 3  # 2 bordes + 1 palabra
    assert text in lines[1]


@pytest.mark.parametrize("text", [
    "Test de consistencia",
])
def test_stacking_words_frame_consistency(text, capsys):
    """Test para verificar que los bordes superior e inferior son iguales"""
    stacking_words(text)
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    # El primer y último línea deben ser idénticos
    assert lines[0] == lines[-1]
    assert lines[0].startswith("*")
    assert lines[0].endswith("*")
