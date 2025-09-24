"""Tests para RETO #005: ÁREA DE UN POLÍGONO"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                                               # pylint: disable=wrong-import-position
from reto_005 import Triangulo, Rectangulo, Cuadrado, area  # pylint: disable=import-error,wrong-import-position # type: ignore


# Tests para Triángulo
@pytest.mark.parametrize("base,altura,expected_area", [
    (10.0, 4.0, 20.0),
    (5.0, 6.0, 15.0),
    (1.0, 1.0, 0.5),
    (7.5, 2.4, 9.0),
])
def test_triangulo_area(base, altura, expected_area):
    """Test para cálculo de área de triángulos"""
    triangulo = Triangulo(base, altura)
    assert triangulo.calcular_area() == expected_area
    assert triangulo.nombre == "triángulo"


# Tests para Rectángulo
@pytest.mark.parametrize("largo,ancho,expected_area", [
    (12.5, 3.5, 43.75),
    (10.0, 5.0, 50.0),
    (1.0, 1.0, 1.0),
    (2.5, 4.0, 10.0),
])
def test_rectangulo_area(largo, ancho, expected_area):
    """Test para cálculo de área de rectángulos"""
    rectangulo = Rectangulo(largo, ancho)
    assert rectangulo.calcular_area() == expected_area
    assert rectangulo.nombre == "rectángulo"


# Tests para Cuadrado
@pytest.mark.parametrize("lado,expected_area", [
    (8.234, 67.798756),  # 8.234^2
    (5.0, 25.0),
    (1.0, 1.0),
    (10.0, 100.0),
])
def test_cuadrado_area(lado, expected_area):
    """Test para cálculo de área de cuadrados"""
    cuadrado = Cuadrado(lado)
    assert abs(cuadrado.calcular_area() - expected_area) < 0.000001
    assert cuadrado.nombre == "cuadrado"


@pytest.mark.parametrize("poligono_tipo,params,expected_area", [
    ("triangulo", (6.0, 4.0), 12.0),
    ("rectangulo", (5.0, 3.0), 15.0),
    ("cuadrado", (4.0,), 16.0),
])
def test_area_function(poligono_tipo, params, expected_area):
    """Test para la función area() que calcula y muestra el área"""
    if poligono_tipo == "triangulo":
        poligono = Triangulo(*params)
    elif poligono_tipo == "rectangulo":
        poligono = Rectangulo(*params)
    elif poligono_tipo == "cuadrado":
        poligono = Cuadrado(*params)
    else:
        raise ValueError(f"Tipo de polígono no soportado: {poligono_tipo}")

    result = area(poligono)
    assert result == expected_area


@pytest.mark.parametrize("poligono_tipo,params,expected_detalles", [
    ("triangulo", (10.0, 4.0), "base = 10.000, altura = 4.000"),
    ("rectangulo", (12.5, 3.5), "largo = 12.500, ancho = 3.500"),
    ("cuadrado", (8.234,), "lado = 8.234"),
])
def test_detalles_especificos(poligono_tipo, params, expected_detalles):
    """Test para verificar los detalles específicos de cada polígono"""
    if poligono_tipo == "triangulo":
        poligono = Triangulo(*params)
    elif poligono_tipo == "rectangulo":
        poligono = Rectangulo(*params)
    elif poligono_tipo == "cuadrado":
        poligono = Cuadrado(*params)
    else:
        raise ValueError(f"Tipo de polígono no soportado: {poligono_tipo}")

    assert poligono.detalles_especificos() == expected_detalles


# Tests para casos especiales (valores decimales)
@pytest.mark.parametrize("poligono,expected_area", [
    (Triangulo(3.5, 2.8), 4.9),   # (3.5 * 2.8) / 2
    (Rectangulo(2.5, 1.2), 3.0),  # 2.5 * 1.2
    (Cuadrado(1.5), 2.25),        # 1.5^2
])
def test_casos_decimales(poligono, expected_area):
    """Test para casos con valores decimales"""
    assert abs(poligono.calcular_area() - expected_area) < 0.000001
