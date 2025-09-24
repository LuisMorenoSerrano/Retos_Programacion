"""Tests para RETO #018: CARRERA DE OBSTÁCULOS"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest  # pylint: disable=wrong-import-position
from reto_018 import check_obstacle_race  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("actions,track,expected_result,expected_msg_contains", [
    # Casos exitosos
    (["run"], "_", True, "sin errores"),
    (["jump"], "|", True, "sin errores"),
    (["run", "jump", "run"], "_|_", True, "sin errores"),
    (["run", "run", "jump", "run", "run", "jump", "run", "run", "jump", "jump",
      "run", "run", "run", "run", "run"],
     "__|__|___|___|_", False, "errores"),  # Tiene run en valla (posición 13)

    # Casos con errores
    (["jump"], "_", False, "errores"),  # Jump en suelo
    (["run"], "|", False, "errores"),   # Run en valla
    (["jump", "run", "run"], "_|_", False, "errores"),  # Jump incorrecto al inicio
    (["run", "run", "jump", "run", "run", "jump", "run", "run", "run", "jump",
      "run", "run", "run", "jump", "run"],
     "__|__|___|___|_", True, "sin errores"),  # Todas las acciones correctas

    # Casos especiales
    ([], "", True, "sin errores"),  # Carrera vacía
])
def test_check_obstacle_race_valid_cases(actions, track, expected_result, expected_msg_contains):
    """Test para casos válidos de carrera de obstáculos"""
    result, message = check_obstacle_race(actions, track)
    assert result == expected_result
    assert expected_msg_contains in message.lower()


@pytest.mark.parametrize("actions,track", [
    # Casos con errores de longitud
    ([], "_"),  # Menos acciones que secciones
    (["run"], "__"),  # Menos acciones que secciones
    (["run", "run", "run"], "_"),  # Más acciones que secciones

    # Casos con acciones inválidas
    (["runn"], "_"),  # Acción inválida
    (["walk"], "_"),  # Acción no permitida
    ([""], "_"),      # Acción vacía

    # Casos con pista inválida
    (["run"], "*"),   # Símbolo de pista inválido
    (["run"], "a"),   # Carácter no permitido
])
def test_check_obstacle_race_invalid_cases(actions, track):
    """Test para casos inválidos (deberían retornar False)"""
    result, message = check_obstacle_race(actions, track)
    assert result is False
    assert "errores" in message.lower()


@pytest.mark.parametrize("actions,track,expected_result", [
    # Jump en suelo debe cambiar a 'x'
    (["jump"], "_", False),
    # Run en valla debe cambiar a '/'
    (["run"], "|", False),
    # Combinaciones correctas no deben cambiar la pista
    (["run", "jump"], "_|", True),
])
def test_check_obstacle_race_track_modification(actions, track, expected_result):
    """Test para verificar modificación correcta de la pista"""
    result, _ = check_obstacle_race(actions, track)
    assert result == expected_result


@pytest.mark.parametrize("actions,track,expected_result", [
    # Carrera vacía
    ([], "", True),
    # Una sola acción correcta
    (["run"], "_", True),
    (["jump"], "|", True),
])
def test_check_obstacle_race_edge_cases(actions, track, expected_result):
    """Test para casos límite"""
    result, _ = check_obstacle_race(actions, track)
    assert result == expected_result
