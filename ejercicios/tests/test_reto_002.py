"""Tests para RETO #002: ¿ES UN ANAGRAMA?"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                                         # pylint: disable=wrong-import-position
from reto_002 import es_anagrama, normalizar_palabra  # pylint: disable=import-error,wrong-import-position # type: ignore


# Tests para casos válidos (son anagramas)
@pytest.mark.parametrize("palabra1,palabra2", [
    # Casos básicos
    ("Pace", "Cepa"),
    ("Daba", "Abad"),
    ("Zorra", "Arroz"),
    ("Arroz", "Rozar"),
    ("Monja", "Jamón"),

    # Casos con acentos
    ("Monja", "Jamon"),    # Con y sin acento
    ("Alegan", "Ángela"),  # Con acento

    # Casos complejos
    ("Conservadora", "Conversadora"),
    ("SetecAstronomy", "MontereysCoast"),
    ("SetecAstronomy", "MySocratesNote"),
    ("SetecAstronomy", "TooManySecrets"),
])
def test_valid_anagrams(palabra1, palabra2):
    """Test para casos válidos que SÍ son anagramas"""
    assert es_anagrama(palabra1, palabra2)


# Tests para casos inválidos (NO son anagramas)
@pytest.mark.parametrize("palabra1,palabra2", [
    # Palabras exactamente iguales (no son anagramas por definición)
    ("NoEsAnagrama", "NoEsAnagrama"),
    ("Hola", "Hola"),
    ("Test", "test"),                  # Misma palabra, diferente case

    # Palabras diferentes que no son anagramas
    ("Legado", "Colega"),  # No tienen las mismas letras
    ("Casa", "Mesa"),
    ("Python", "Java"),
])
def test_invalid_anagrams(palabra1, palabra2):
    """Test para casos que NO son anagramas"""
    assert not es_anagrama(palabra1, palabra2)


# Tests para la función auxiliar normalizar_palabra
@pytest.mark.parametrize("palabra,expected", [
    ("Ángela", "angela"),
    ("Jamón", "jamon"),
    ("MAYÚSCULAS", "mayusculas"),
    ("MiXeD cAsE", "mixed case"),
    ("Niño", "nino"),
])
def test_normalizar_palabra(palabra, expected):
    """Test para la función de normalización"""
    assert normalizar_palabra(palabra) == expected


# Para ejecutar directamente este archivo de tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
