"""Tests para RETO #032: AÑOS BISIESTOS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                        # pylint: disable=wrong-import-position
from reto_032 import get_leap_years  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("init_year,max_years,expected", [
    # Casos básicos
    (2020, 5, [2024, 2028, 2032, 2036, 2040]),
    (2021, 3, [2024, 2028, 2032]),
    (2022, 4, [2024, 2028, 2032, 2036]),
    (2023, 2, [2024, 2028]),

    # Casos con años divisibles por 100 pero no por 400 (no bisiestos)
    (1896, 5, [1904, 1908, 1912, 1916, 1920]),  # Salta 1900 (no bisiesto)
    (1895, 3, [1896, 1904, 1908]),              # 1900 no es bisiesto

    # Casos con años divisibles por 400 (sí bisiestos)
    (1995, 5, [1996, 2000, 2004, 2008, 2012]),  # Incluye 2000 (bisiesto)
    (1999, 3, [2000, 2004, 2008]),              # 2000 es bisiesto

    # Casos alrededor de 2100 (no bisiesto por ser divisible por 100)
    (2096, 5, [2104, 2108, 2112, 2116, 2120]),  # Salta 2100
    (2099, 2, [2104, 2108]),                    # 2100 no es bisiesto

    # Casos con un solo año solicitado
    (2023, 1, [2024]),
    (2024, 1, [2028]),  # El siguiente después de 2024

    # Casos con número máximo de años por defecto (30)
    (2020, 30, [2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060,
                2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104,
                2108, 2112, 2116, 2120, 2124, 2128, 2132, 2136, 2140, 2144]),
])
def test_get_leap_years(init_year, max_years, expected):
    """Test de la función get_leap_years con diferentes parámetros"""
    result = get_leap_years(init_year, max_years)
    assert result == expected


@pytest.mark.parametrize("init_year,expected_len,expected_first", [
    (2020, 30, 2024),
])
def test_get_leap_years_default_parameter(init_year, expected_len, expected_first):
    """Test con parámetro max_years por defecto (30)"""
    result = get_leap_years(init_year)
    assert len(result) == expected_len
    assert result[0] == expected_first               # Primer año bisiesto después del año inicial
    assert all(year > init_year for year in result)  # Todos mayores al año inicial


@pytest.mark.parametrize("init_year,max_years", [
    (2020, 0),   # Cero años solicitados
    (2020, 10),  # 10 años
    (2020, 50),  # 50 años
])
def test_get_leap_years_correct_count(init_year, max_years):
    """Test para verificar que se devuelve el número correcto de años"""
    result = get_leap_years(init_year, max_years)
    assert len(result) == max_years


@pytest.mark.parametrize("init_year", [
    2000, 2004, 2020, 2024, 2100, 2200, 2400
])
def test_get_leap_years_all_returned_are_leap_years(init_year):
    """Test para verificar que todos los años devueltos son realmente bisiestos"""
    result = get_leap_years(init_year, 10)

    for year in result:
        # Verificar que cada año cumple la regla de año bisiesto
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        assert is_leap, f"El año {year} no es bisiesto"


@pytest.mark.parametrize("init_year", [
    2020, 2021, 2022, 2023
])
def test_get_leap_years_all_greater_than_init_year(init_year):
    """Test para verificar que todos los años devueltos son mayores al año inicial"""
    result = get_leap_years(init_year, 5)

    for year in result:
        assert year > init_year, f"El año {year} no es mayor que {init_year}"


@pytest.mark.parametrize("invalid_year", [
    "2020",  # String en lugar de int
    2020.5,  # Float en lugar de int
    None,    # None
    [],      # Lista
    {},      # Diccionario
])
def test_get_leap_years_invalid_year_type(invalid_year):
    """Test con tipos de año inválidos"""
    with pytest.raises(TypeError, match="El año debe ser un número entero"):
        get_leap_years(invalid_year, 5)


@pytest.mark.parametrize("init_year,max_years", [
    (2000, 10),
])
def test_get_leap_years_sorted_order(init_year, max_years):
    """Test para verificar que los años se devuelven en orden ascendente"""
    result = get_leap_years(init_year, max_years)

    # Verificar que la lista está ordenada
    assert result == sorted(result)


@pytest.mark.parametrize("init_year,expected_first", [
    # Verificar casos específicos de primer año bisiesto siguiente
    (1899, 1904),  # Después de 1899, el siguiente es 1904 (1900 no es bisiesto)
    (1999, 2000),  # Después de 1999, el siguiente es 2000
    (2099, 2104),  # Después de 2099, el siguiente es 2104 (2100 no es bisiesto)
    (2399, 2400),  # Después de 2399, el siguiente es 2400
])
def test_get_leap_years_first_year_edge_cases(init_year, expected_first):
    """Test de casos específicos para el primer año bisiesto"""
    result = get_leap_years(init_year, 1)
    assert result[0] == expected_first


@pytest.mark.parametrize("test_cases", [
    # Años divisibles por 4 pero no por 100: bisiestos
    (2020, 1, 2024, True),
    # Años divisibles por 100 pero no por 400: NO bisiestos
    (1896, 5, 1900, False),
    # Años divisibles por 400: bisiestos
    (1996, 5, 2000, True),
])
def test_get_leap_years_leap_year_rules(test_cases):
    """Test específico para verificar las reglas de años bisiestos"""
    init_year, max_years, test_year, should_be_included = test_cases
    result = get_leap_years(init_year, max_years)

    if should_be_included:
        assert test_year in result
    else:
        assert test_year not in result


@pytest.mark.parametrize("init_year,max_years,expected_len", [
    (2020, 0, 0),
])
def test_get_leap_years_negative_or_zero_max_years(init_year, max_years, expected_len):
    """Test con max_years igual a 0"""
    result = get_leap_years(init_year, max_years)
    assert len(result) == expected_len
    assert result == []
