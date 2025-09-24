"""Tests para RETO #020: CONVERSOR DE TIEMPO A MILISEGUNDOS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest  # pylint: disable=wrong-import-position
from reto_020 import TimeLapse, thousand_sep  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("days,hours,minutes,seconds,expected_ms", [
    # Casos básicos
    (0, 0, 0, 0, 0),
    (0, 0, 0, 1, 1000),
    (0, 0, 1, 0, 60000),
    (0, 1, 0, 0, 3600000),
    (1, 0, 0, 0, 86400000),

    # Casos combinados
    (0, 0, 2, 0, 120000),
    (0, 3, 0, 0, 10800000),
    (4, 0, 0, 0, 345600000),
    (8, 7, 6, 5, 716765000),  # 8 días + 7 horas + 6 minutos + 5 segundos

    # Casos con valores negativos (el código los maneja)
    (2, 5, -45, 10, 188110000),  # Resultado: (2*86400 + 5*3600 - 45*60 + 10) * 1000

    # Casos extremos
    (0, 0, 0, 60, 60000),     # 60 segundos = 1 minuto
    (0, 0, 60, 0, 3600000),   # 60 minutos = 1 hora
    (0, 24, 0, 0, 86400000),  # 24 horas = 1 día
])
def test_timelapse_convert_to_millisecs(days, hours, minutes, seconds, expected_ms):
    """Test para conversión a milisegundos"""
    timelapse = TimeLapse(days, hours, minutes, seconds)
    assert timelapse.convert_to_millisecs() == expected_ms


@pytest.mark.parametrize("days,hours,minutes,seconds", [
    # Constructor con todos los parámetros
    (1, 2, 3, 4),
    # Constructor con valores por defecto
    (0, 0, 0, 0),
    # Constructor con algunos parámetros
    (5, 0, 30, 0),
])
def test_timelapse_constructor(days, hours, minutes, seconds):
    """Test para el constructor de TimeLapse"""
    if days == 0 and hours == 0 and minutes == 0 and seconds == 0:
        tl = TimeLapse()
    elif days == 5 and hours == 0 and minutes == 30 and seconds == 0:
        tl = TimeLapse(days=5, minutes=30)
    else:
        tl = TimeLapse(days, hours, minutes, seconds)

    assert tl.days == days
    assert tl.hours == hours
    assert tl.minutes == minutes
    assert tl.seconds == seconds


@pytest.mark.parametrize("days,hours,minutes,seconds,expected", [
    (1, 2, 3, 4, "TimeLapse: 1 días, 2 horas, 3 minutos, 4 segundos"),
    (0, 0, 0, 0, "TimeLapse: 0 días, 0 horas, 0 minutos, 0 segundos"),
])
def test_timelapse_str_representation(days, hours, minutes, seconds, expected):
    """Test para la representación en cadena"""
    tl = TimeLapse(days, hours, minutes, seconds)
    assert str(tl) == expected


@pytest.mark.parametrize("number,expected", [
    (0, "0"),
    (1000, "1.000"),
    (1000000, "1.000.000"),
    (1234567, "1.234.567"),
    (86400000, "86.400.000"),
    (720365000, "720.365.000"),
    (716765000, "716.765.000"),
])
def test_thousand_sep(number, expected):
    """Test para formateo de números con separador de miles"""
    assert thousand_sep(number) == expected


@pytest.mark.parametrize("days,expected_ms", [
    # Números muy grandes
    (2000000000, 2000000000 * 24 * 60 * 60 * 1000),
    # Solo segundos (3661 = 1 hora, 1 minuto, 1 segundo)
    (0, 0),  # Control case for days=0
])
def test_timelapse_edge_cases(days, expected_ms):
    """Test para casos límite"""
    if days == 0:
        tl = TimeLapse(seconds=3661)
        assert tl.convert_to_millisecs() == 3661000
    else:
        tl = TimeLapse(days=days)
        assert tl.convert_to_millisecs() == expected_ms


@pytest.mark.parametrize("tl1_params,tl2_params,should_equal", [
    # 1 día debe ser igual a 24 horas
    ({"days": 1}, {"hours": 24}, True),
    # 1 hora debe ser igual a 60 minutos
    ({"hours": 1}, {"minutes": 60}, True),
    # 1 minuto debe ser igual a 60 segundos
    ({"minutes": 1}, {"seconds": 60}, True),
])
def test_timelapse_mathematical_consistency(tl1_params, tl2_params, should_equal):
    """Test para verificar consistencia matemática"""
    tl1 = TimeLapse(**tl1_params)
    tl2 = TimeLapse(**tl2_params)
    if should_equal:
        assert tl1.convert_to_millisecs() == tl2.convert_to_millisecs()
    else:
        assert tl1.convert_to_millisecs() != tl2.convert_to_millisecs()


@pytest.mark.parametrize("days,hours,minutes,seconds", [
    (1, 2, 3, 4),
])
def test_timelapse_format(days, hours, minutes, seconds):
    """Test para el método __format__"""
    tl = TimeLapse(days, hours, minutes, seconds)
    # Debe usar el formato del __str__
    formatted = f"{tl:<60}"
    assert "TimeLapse: 1 días, 2 horas, 3 minutos, 4 segundos" in formatted
