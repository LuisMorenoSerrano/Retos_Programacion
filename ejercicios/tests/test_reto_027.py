"""Tests para RETO #027: CUADRADO Y TRIÁNGULO 2D"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                                                 # pylint: disable=wrong-import-position
from reto_027 import Triangle, Square, Diamond, show_polygon  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("side_length,expected_sides", [
    (3, 3),
    (5, 3),
    (10, 3),
])
def test_triangle_properties(side_length, expected_sides):
    """Test de las propiedades básicas del triángulo"""
    triangle = Triangle(side_length)
    assert triangle.num_sides == expected_sides
    assert triangle.side_length == side_length
    assert "Triángulo" in str(triangle)


@pytest.mark.parametrize("side_length,expected_sides", [
    (3, 4),
    (5, 4),
    (10, 4),
])
def test_square_properties(side_length, expected_sides):
    """Test de las propiedades básicas del cuadrado"""
    square = Square(side_length)
    assert square.num_sides == expected_sides
    assert square.side_length == side_length
    assert "Cuadrado" in str(square)


@pytest.mark.parametrize("side_length,expected_sides", [
    (3, 4),
    (5, 4),
    (10, 4),
])
def test_diamond_properties(side_length, expected_sides):
    """Test de las propiedades básicas del rombo"""
    diamond = Diamond(side_length)
    assert diamond.num_sides == expected_sides
    assert diamond.side_length == side_length
    assert "Rombo" in str(diamond)


@pytest.mark.parametrize("side_length", [0, 1, -1, -5])
def test_invalid_side_length_triangle(side_length, capsys):
    """Test de triángulos con longitudes inválidas"""
    triangle = Triangle(side_length)
    triangle.draw()
    captured = capsys.readouterr()
    assert "Error: La longitud del lado debe ser mayor que 1." in captured.out


@pytest.mark.parametrize("side_length", [0, 1, -1, -5])
def test_invalid_side_length_square(side_length, capsys):
    """Test de cuadrados con longitudes inválidas"""
    square = Square(side_length)
    square.draw()
    captured = capsys.readouterr()
    assert "Error: La longitud del lado debe ser mayor que 1." in captured.out


@pytest.mark.parametrize("side_length", [0, 1, -1, -5])
def test_invalid_side_length_diamond(side_length, capsys):
    """Test de rombos con longitudes inválidas"""
    diamond = Diamond(side_length)
    diamond.draw()
    captured = capsys.readouterr()
    assert "Error: La longitud del lado debe ser mayor que 1." in captured.out


@pytest.mark.parametrize("side_length,expected_lines", [
    (3, ["*", "* *", "* * *"]),
])
def test_triangle_drawing_small(side_length, expected_lines, capsys):
    """Test del dibujo de un triángulo pequeño"""
    triangle = Triangle(side_length)
    triangle.draw()
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    # Verificar que se dibujó correctamente
    assert len(lines) == side_length
    assert lines == expected_lines


@pytest.mark.parametrize("side_length,expected_lines", [
    (3, ["* * *", "*   *", "* * *"]),
])
def test_square_drawing_small(side_length, expected_lines, capsys):
    """Test del dibujo de un cuadrado pequeño"""
    square = Square(side_length)
    square.draw()
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    # Verificar que se dibujó correctamente
    assert len(lines) == side_length
    assert lines == expected_lines


@pytest.mark.parametrize("polygon_class,side_length,expected_in_output", [
    (Triangle, 2, ["Triángulo", "* *"]),
])
def test_show_polygon_function(polygon_class, side_length, expected_in_output, capsys):
    """Test de la función show_polygon"""
    polygon = polygon_class(side_length)
    show_polygon(polygon)
    captured = capsys.readouterr()

    # Verificar que se muestra la descripción y el dibujo
    for expected_text in expected_in_output:
        assert expected_text in captured.out


@pytest.mark.parametrize("polygon_class,side_length", [
    (Triangle, 5),
    (Square, 4),
    (Diamond, 3),
])
def test_polygon_drawing_produces_output(polygon_class, side_length, capsys):
    """Test que verifica que los polígonos válidos producen salida"""
    polygon = polygon_class(side_length)
    polygon.draw()
    captured = capsys.readouterr()

    # Verificar que se produjo alguna salida (contiene asteriscos)
    assert "*" in captured.out
    assert len(captured.out.strip()) > 0
