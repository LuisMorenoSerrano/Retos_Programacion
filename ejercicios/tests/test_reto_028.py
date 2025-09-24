"""Tests para RETO #028: VECTORES ORTOGONALES"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                                            # pylint: disable=wrong-import-position
from reto_028 import scalar_product, orthogonal_vectors  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("vector1,vector2,expected", [
    # Casos básicos de producto escalar
    ((1, 2), (3, 4), 11),       # 1*3 + 2*4 = 3 + 8 = 11
    ((0, 0), (5, 10), 0),       # Vector cero
    ((1, -1), (1, 1), 0),       # Vectores ortogonales
    ((1, 0, 0), (0, 1, 0), 0),  # Vectores unitarios ortogonales

    # Casos con números negativos
    ((-1, 2), (3, -4), -11),   # -1*3 + 2*(-4) = -3 - 8 = -11
    ((-1, -2), (-3, -4), 11),  # (-1)*(-3) + (-2)*(-4) = 3 + 8 = 11

    # Casos con ceros
    ((0, 5), (10, 0), 0),
    ((0, 0, 0), (1, 2, 3), 0),

    # Casos más complejos
    ((1, 2, 3, 4), (2, 1, 0, -1), 0),     # 1*2 + 2*1 + 3*0 + 4*(-1) = 2 + 2 + 0 - 4 = 0
    ((1, 4, 0, -3), (2, -3, 0, -1), -7),  # 1*2 + 4*(-3) + 0*0 + (-3)*(-1) = 2 - 12 + 0 + 3 = -7
])
def test_scalar_product(vector1, vector2, expected):
    """Test del producto escalar de vectores"""
    result = scalar_product(vector1, vector2)
    assert result == expected


@pytest.mark.parametrize("vector1,vector2,expected", [
    # Vectores ortogonales (producto escalar = 0)
    ((1, 0), (0, 1), True),
    ((1, -1), (1, 1), True),
    ((1, 0, 0), (0, 1, 0), True),
    ((1, 2, 2), (2, -1, 0), True),        # 1*2 + 2*(-1) + 2*0 = 2 - 2 + 0 = 0
    ((1, 2, 3, 4), (2, 1, 0, -1), True),  # 1*2 + 2*1 + 3*0 + 4*(-1) = 0

    # Vectores NO ortogonales
    ((1, 2), (3, 4), False),        # producto escalar = 11
    ((1, 1, 1), (1, 2, 3), False),  # producto escalar = 6
    ((1, -3), (2, 5), False),       # producto escalar = -13

    # Vector cero es ortogonal a cualquier vector
    ((0, 0), (5, 10), True),
    ((0, 0, 0), (1, 2, 3), True),
])
def test_orthogonal_vectors(vector1, vector2, expected):
    """Test de detección de vectores ortogonales"""
    result = orthogonal_vectors(vector1, vector2)
    assert result == expected


@pytest.mark.parametrize("vector1,vector2", [
    # Casos de error: diferentes longitudes
    ((1,), (1, 2, 3)),
    ((1, 2, 3), (1, 2)),
    ((1, 0), (0, 1, 0)),
    ((1, 2, 3, 4), (1, 2)),
])
def test_scalar_product_different_lengths(vector1, vector2):
    """Test de error por vectores de diferentes longitudes"""
    with pytest.raises(ValueError, match="Las tuplas deben tener la misma longitud"):
        scalar_product(vector1, vector2)


@pytest.mark.parametrize("vector1,vector2", [
    # Casos de error: tipos incorrectos
    (1, (2,)),         # Primer argumento no es tupla
    ((1,), 2),         # Segundo argumento no es tupla
    ([1, 2], (3, 4)),  # Lista en lugar de tupla
    ((1, 2), [3, 4]),  # Lista en lugar de tupla
])
def test_scalar_product_invalid_types(vector1, vector2):
    """Test de error por tipos incorrectos"""
    with pytest.raises(TypeError, match="Ambos argumentos deben ser tuplas"):
        scalar_product(vector1, vector2)


@pytest.mark.parametrize("vector1,vector2", [
    # Los mismos casos de error deberían aplicar a orthogonal_vectors
    ((1,), (1, 2, 3)),
    ((1, 2, 3), (1, 2)),
])
def test_orthogonal_vectors_different_lengths(vector1, vector2):
    """Test de error en orthogonal_vectors por vectores de diferentes longitudes"""
    with pytest.raises(ValueError, match="Las tuplas deben tener la misma longitud"):
        orthogonal_vectors(vector1, vector2)


@pytest.mark.parametrize("vector1,vector2", [
    (1, (2,)),
    ((1,), 2),
])
def test_orthogonal_vectors_invalid_types(vector1, vector2):
    """Test de error en orthogonal_vectors por tipos incorrectos"""
    with pytest.raises(TypeError, match="Ambos argumentos deben ser tuplas"):
        orthogonal_vectors(vector1, vector2)
