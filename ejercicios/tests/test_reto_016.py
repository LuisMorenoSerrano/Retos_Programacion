"""Tests para RETO #016: DIFERENCIA DE DÍAS ENTRE FECHAS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                       # pylint: disable=wrong-import-position
from reto_016 import datediff_days  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("date1,date2,expected", [
    # Casos básicos
    ("01/01/2020", "01/01/2020", 0),    # Misma fecha
    ("01/01/2020", "02/01/2020", 1),    # Un día de diferencia
    ("01/01/2020", "31/01/2020", 30),   # Un mes menos un día
    ("01/01/2020", "01/01/2021", 366),  # Un año (bisiesto)
    ("01/01/2021", "01/01/2022", 365),  # Un año (no bisiesto)

    # Orden inverso (debe ser absoluto)
    ("02/01/2020", "01/01/2020", 1),
    ("31/01/2020", "01/01/2020", 30),
    ("01/01/2021", "01/01/2020", 366),

    # Casos con años bisiestos
    ("28/02/2020", "01/03/2020", 2),  # Año bisiesto
    ("28/02/2021", "01/03/2021", 1),  # Año no bisiesto
    ("29/02/2020", "01/03/2020", 1),  # 29 de febrero válido

    # Casos históricos
    ("15/01/1900", "01/01/1900", 14),
    ("06/06/1969", "30/06/2024", 20113),  # Diferencia grande
    ("02/06/1995", "30/06/2024", 10621),  # Diferencia mediana

    # Casos con diferentes meses
    ("01/01/2020", "01/02/2020", 31),  # Enero completo
    ("01/02/2020", "01/03/2020", 29),  # Febrero bisiesto
    ("01/02/2021", "01/03/2021", 28),  # Febrero no bisiesto
    ("01/12/2020", "01/01/2021", 31),  # Diciembre completo

    # Casos con formatos sin ceros iniciales (válidos)
    ("15/1/2020", "15/01/2020", 0),   # Mes sin cero inicial
    ("1/01/2020", "15/01/2020", 14),  # Día sin cero inicial
])
def test_datediff_days_valid_dates(date1, date2, expected):
    """Test para fechas válidas"""
    assert datediff_days(date1, date2) == expected


@pytest.mark.parametrize("invalid_date1,invalid_date2", [
    # Fechas inválidas
    ("30/02/1900", "15/01/1900"),  # 30 de febrero no existe
    ("29/02/1900", "15/01/1900"),  # 1900 no es bisiesto
    ("32/01/2020", "15/01/2020"),  # 32 de enero no existe
    ("15/13/2020", "15/01/2020"),  # Mes 13 no existe
    ("15/00/2020", "15/01/2020"),  # Mes 0 no existe
    ("00/01/2020", "15/01/2020"),  # Día 0 no existe

    # Formatos incorrectos
    ("2020/01/15", "15/01/2020"),  # Formato incorrecto
    ("15-01-2020", "15/01/2020"),  # Separador incorrecto
    ("15/01/20", "15/01/2020"),    # Año con 2 dígitos

    # Cadenas vacías o inválidas
    ("", "15/01/2020"),
    ("15/01/2020", ""),
    ("abc", "15/01/2020"),
    ("15/01/2020", "xyz"),
])
def test_datediff_days_invalid_dates(invalid_date1, invalid_date2):
    """Test para fechas inválidas (debe retornar -1)"""
    result = datediff_days(invalid_date1, invalid_date2)
    assert result == -1


@pytest.mark.parametrize("date1,date2,expected_days", [
    # 2020 es bisiesto, 2021 no
    ("01/01/2020", "01/01/2021", 366),
    ("01/01/2021", "01/01/2022", 365),
    # Febrero en año bisiesto
    ("28/02/2020", "29/02/2020", 1),
    ("29/02/2020", "01/03/2020", 1),
    # 29/02 válido en año bisiesto
    ("29/02/2020", "29/02/2020", 0),
])
def test_datediff_days_leap_years(date1, date2, expected_days):
    """Test específico para años bisiestos"""
    assert datediff_days(date1, date2) == expected_days


@pytest.mark.parametrize("date1,date2,expected_days", [
    # 1900 no es bisiesto (divisible por 100 pero no por 400)
    ("28/02/1900", "01/03/1900", 1),  # No hay 29/02/1900
    # 2000 sí es bisiesto (divisible por 400)
    ("28/02/2000", "01/03/2000", 2),  # Sí hay 29/02/2000
])
def test_datediff_days_century_years(date1, date2, expected_days):
    """Test para años de siglo (reglas especiales de bisiesto)"""
    assert datediff_days(date1, date2) == expected_days


@pytest.mark.parametrize("date1,date2", [
    ("01/01/2020", "15/06/2021"),
    ("29/02/2020", "28/02/2021"),
    ("31/12/2019", "01/01/2020"),
])
def test_datediff_days_symmetry(date1, date2):
    """Test para verificar que la función es simétrica (orden no importa)"""
    assert datediff_days(date1, date2) == datediff_days(date2, date1)
