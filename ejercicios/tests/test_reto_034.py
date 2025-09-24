"""Tests para RETO #034: CICLO SEXAGENARIO CHINO"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                                            # pylint: disable=wrong-import-position
from reto_034 import get_chinese_zodiac, chinese_zodiac  # pylint: disable=import-error,wrong-import-position # type: ignore


# Tests para casos válidos conocidos
@pytest.mark.parametrize("year,expected_element,expected_animal", [
    # Años de referencia
    (1984, "Madera", "Rata"),  # Año base
    (1985, "Madera", "Buey"),  # Segundo año

    # Años específicos conocidos
    (1992, "Agua", "Mono"),
    (2000, "Metal", "Dragón"),
    (2005, "Madera", "Gallo"),
    (2010, "Metal", "Tigre"),
    (2024, "Madera", "Dragón"),
    (2025, "Madera", "Serpiente"),
])
def test_valid_known_years(year, expected_element, expected_animal):
    """Test para años específicos con resultados conocidos"""
    element, animal = get_chinese_zodiac(year)
    assert element == expected_element
    assert animal == expected_animal


# Tests para casos válidos con validación general
@pytest.mark.parametrize("year", [0, -100, 1000, 2050, -500])
def test_valid_general_years(year):
    """Test para años válidos con validación general"""
    element, animal = get_chinese_zodiac(year)

    # Verificar que los resultados están en los diccionarios válidos
    assert element in chinese_zodiac["elements"]
    assert animal in chinese_zodiac["animals"]

    # Verificar que devuelve una tupla de exactamente 2 elementos
    result = get_chinese_zodiac(year)
    assert isinstance(result, tuple)
    assert len(result) == 2


# Tests para casos inválidos que deben lanzar excepciones
@pytest.mark.parametrize("invalid_year", [
    1984.5,          # Float
    "1984",          # String
    None,            # None
    [1984],          # Lista
    {"year": 1984},  # Dict
])
def test_invalid_year_types(invalid_year):
    """Test para tipos de año inválidos"""
    with pytest.raises(TypeError, match="El año debe ser un número entero"):
        get_chinese_zodiac(invalid_year)


@pytest.mark.parametrize("base_year", [
    1984, 2000, 2020
])
def test_cycle_consistency(base_year):
    """Verificar consistencia del ciclo de 60 años"""
    # El mismo elemento y animal deben repetirse cada 60 años
    element1, animal1 = get_chinese_zodiac(base_year)
    element2, animal2 = get_chinese_zodiac(base_year + 60)
    element3, animal3 = get_chinese_zodiac(base_year + 120)

    assert element1 == element2 == element3
    assert animal1 == animal2 == animal3


@pytest.mark.parametrize("base_year", [
    1984, 2000, 2020
])
def test_element_two_year_cycle(base_year):
    """Verificar que cada elemento se repite dos años seguidos"""
    element1, _ = get_chinese_zodiac(base_year)
    element2, _ = get_chinese_zodiac(base_year + 1)
    element3, _ = get_chinese_zodiac(base_year + 2)

    # Mismo elemento en años consecutivos
    assert element1 == element2
    # Elemento diferente en el tercer año
    assert element1 != element3


# Para ejecutar directamente este archivo de tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
