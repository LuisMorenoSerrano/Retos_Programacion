"""Tests para RETO #026: PIEDRA, PAPEL, TIJERA"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                             # pylint: disable=wrong-import-position
from reto_026 import rock_paper_scissors  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("playlist,expected", [
    # Casos de error - formato incorrecto
    ([("R", "S"), ("S")], "Error: La partida debe ser una lista de pares de movimientos"),
    ([("R", "S", "S"), ("S", "P")], "Error: La partida debe ser una lista de pares de movimientos"),

    # Casos de error - movimiento inválido
    ([("R", "S"), ("Z", "R"), ("P", "S")], "Error: El movimiento 'Z' no es válido"),

    # Casos de victoria Player 1
    ([("R", "S")], "Player 1 (1/0)"),
    ([("R", "S"), ("P", "R")], "Player 1 (2/0)"),

    # Casos de victoria Player 2
    ([("S", "R")], "Player 2 (0/1)"),
    ([("S", "R"), ("R", "P")], "Player 2 (0/2)"),

    # Casos de empate
    ([("R", "R")], "Tie (0/0)"),
    ([("R", "S"), ("S", "R")], "Tie (1/1)"),

    # Casos complejos
    ([("R", "S"), ("P", "R"), ("S", "R"), ("P", "S"), ("S", "P")], "Player 1 (3/2)"),
    ([("R", "S"), ("S", "R"), ("P", "S")], "Player 2 (1/2)"),
    ([("R", "S"), ("P", "R"), ("S", "R"), ("P", "S"), ("S", "P"), ("S", "R")], "Tie (3/3)"),
])
def test_rock_paper_scissors(playlist, expected):
    """Test de la función rock_paper_scissors con diferentes casos"""
    result = rock_paper_scissors(playlist)
    assert result == expected


@pytest.mark.parametrize("playlist,expected_winner", [
    # Casos específicos para verificar lógica de victoria
    ([("R", "S"), ("R", "S"), ("R", "S")], "Player 1"),  # Piedra gana a tijera
    ([("P", "R"), ("P", "R"), ("P", "R")], "Player 1"),  # Papel gana a piedra
    ([("S", "P"), ("S", "P"), ("S", "P")], "Player 1"),  # Tijera gana a papel

    ([("S", "R"), ("S", "R"), ("S", "R")], "Player 2"),  # Piedra gana a tijera
    ([("R", "P"), ("R", "P"), ("R", "P")], "Player 2"),  # Papel gana a piedra
    ([("P", "S"), ("P", "S"), ("P", "S")], "Player 2"),  # Tijera gana a papel
])
def test_rock_paper_scissors_winner_logic(playlist, expected_winner):
    """Test para verificar que la lógica de victoria es correcta"""
    result = rock_paper_scissors(playlist)
    assert expected_winner in result


@pytest.mark.parametrize("playlist,expected", [
    ([], "Tie (0/0)"),
])
def test_rock_paper_scissors_empty_playlist(playlist, expected):
    """Test con lista vacía"""
    result = rock_paper_scissors(playlist)
    assert result == expected


@pytest.mark.parametrize("playlist,expected", [
    ([("R", "R")], "Tie (0/0)"),
])
def test_rock_paper_scissors_single_tie(playlist, expected):
    """Test con un solo empate"""
    result = rock_paper_scissors(playlist)
    assert result == expected
