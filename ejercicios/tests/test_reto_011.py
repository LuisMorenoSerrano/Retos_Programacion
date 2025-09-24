"""Tests para RETO #011: EXPRESIONES EQUILIBRADAS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                     # pylint: disable=wrong-import-position
from reto_011 import is_balanced  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("expression,expected", [
    # Casos con expresiones balanceadas
    ("{ [ a * ( c + d ) ] - 5 }", True),
    ("()", True),
    ("[]", True),
    ("{}", True),
    ("([{}])", True),
    ("{[()]}", True),
    ("", True),     # Expresión vacía
    ("abc", True),  # Sin delimitadores

    # Casos con expresiones no balanceadas
    ("{ a * ( c + d ) ] - 5 }", False),
    ("{a + b [c] * (2x2)}}}", False),
    ("{a^4 + (((ax4)}", False),
    ("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }", False),
    ("{{{{{{(}}}}}}", False),
    ("(a", False),
    (")", False),
    ("(()", False),
    ("())", False),
    ("([)]", False),  # Entrelazados incorrectamente
    ("{[}]", False),  # Entrelazados incorrectamente
])
def test_is_balanced(expression, expected):
    """Test para verificar si una expresión está equilibrada"""
    assert is_balanced(expression) == expected


@pytest.mark.parametrize("expression,expected", [
    # Solo caracteres sin delimitadores
    ("abcdef123", True),
    # Múltiples tipos de delimitadores anidados
    ("{[()]}", True),
    ("({[]})", True),
    # Delimitadores sin contenido
    ("()[]{}", True),
])
def test_is_balanced_edge_cases(expression, expected):
    """Test para casos especiales"""
    assert is_balanced(expression) == expected
