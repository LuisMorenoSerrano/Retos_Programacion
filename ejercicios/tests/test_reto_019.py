"""Tests para RETO #019: TRES EN RAYA"""
import sys
import os
from io import StringIO

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                                                     # pylint: disable=wrong-import-position
from reto_019 import check_tic_tac_toe_board, State, print_board  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("board,expected_result", [
    # Casos de victoria para X
    ([["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]], State.X.value),  # Fila superior
    ([[" ", " ", " "], ["X", "X", "X"], ["O", "O", " "]], State.X.value),  # Fila media
    ([[" ", " ", " "], ["O", "O", " "], ["X", "X", "X"]], State.X.value),  # Fila inferior
    ([["X", "O", " "], ["X", "O", " "], ["X", " ", " "]], State.X.value),  # Columna izquierda
    ([["O", "X", " "], [" ", "X", "O"], [" ", "X", " "]], State.X.value),  # Columna media
    ([["O", " ", "X"], [" ", "O", "X"], [" ", " ", "X"]], State.X.value),  # Columna derecha
    ([["X", "O", " "], [" ", "X", "O"], [" ", " ", "X"]], State.X.value),  # Diagonal principal
    ([["O", " ", "X"], [" ", "X", "O"], ["X", " ", " "]], State.X.value),  # Diagonal secundaria

    # Casos de victoria para O
    ([["O", "O", "O"], ["X", "X", " "], [" ", " ", " "]], State.O.value),  # Fila superior
    ([[" ", " ", " "], ["O", "O", "O"], ["X", "X", " "]], State.O.value),  # Fila media
    ([[" ", " ", " "], ["X", "X", " "], ["O", "O", "O"]], State.O.value),  # Fila inferior
    ([["O", "X", " "], ["O", "X", " "], ["O", " ", " "]], State.O.value),  # Columna izquierda
    ([["X", "O", " "], [" ", "O", "X"], [" ", "O", " "]], State.O.value),  # Columna media
    ([["X", " ", "O"], [" ", "X", "O"], [" ", " ", "O"]], State.O.value),  # Columna derecha
    ([["O", "X", " "], [" ", "O", "X"], [" ", " ", "O"]], State.O.value),  # Diagonal principal
    ([["X", " ", "O"], [" ", "O", "X"], ["O", " ", " "]], State.O.value),  # Diagonal secundaria

    # Casos de empate
    ([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]], State.DRAW.value),
    ([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]], State.DRAW.value),

    # Casos nulos
    ([["X", "X", "X"], ["O", "O", "O"], [" ", " ", " "]], State.NULL.value),  # Dos ganadores
    ([["X", "X", "X"], ["X", "X", "X"], ["O", "O", " "]], State.NULL.value),  # Demasiadas X
    ([["O", "O", "O"], ["O", "O", "O"], ["X", "X", " "]], State.NULL.value),  # Demasiadas O

    # Partidas en progreso (válidas)
    ([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], State.DRAW.value),  # Tablero vacío
    ([["X", " ", " "], [" ", "O", " "], [" ", " ", " "]], State.DRAW.value),  # Partida en curso
    ([["X", "O", " "], ["O", "X", " "], [" ", " ", " "]], State.DRAW.value),  # Partida en curso
])
def test_check_tic_tac_toe_board(board, expected_result):
    """Test para verificar el estado del tablero de tres en raya"""
    result, _ = check_tic_tac_toe_board(board)
    assert result == expected_result


@pytest.mark.parametrize("invalid_board", [
    # Tableros con dimensiones incorrectas
    [["X", "O"], ["O", "X"]],  # 2x2
    [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"]],  # 4x4
    [["X", "O", "X"], ["O", "X", "O"]],  # 3x2

    # Tableros con filas de longitud incorrecta
    [["X", "O"], ["O", "X", "O"], ["X", "O", "X"]],  # Fila 1 corta
    [["X", "O", "X"], ["O", "X"], ["X", "O", "X"]],  # Fila 2 corta
])
def test_check_tic_tac_toe_board_invalid_dimensions(invalid_board):
    """Test para tableros con dimensiones incorrectas"""
    result, message = check_tic_tac_toe_board(invalid_board)
    assert result == State.NULL.value
    assert "dimensiones" in message.lower()


@pytest.mark.parametrize("board,expected_state", [
    # Demasiadas X (más de 5)
    ([["X", "X", "X"], ["X", "X", "X"], ["O", "O", " "]], State.NULL.value),
    # Demasiadas O (más de 4 si X tiene 5, o más de 5 en general)
    ([["O", "O", "O"], ["O", "O", "X"], ["X", "X", " "]], State.NULL.value),
])
def test_check_tic_tac_toe_board_proportions(board, expected_state):
    """Test para verificar proporciones correctas de X y O"""
    result, _ = check_tic_tac_toe_board(board)
    assert result == expected_state


@pytest.mark.parametrize("board,expected_state", [
    # Tablero completamente vacío
    ([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], State.DRAW.value),
    # Un solo movimiento
    ([["X", " ", " "], [" ", " ", " "], [" ", " ", " "]], State.DRAW.value),
])
def test_check_tic_tac_toe_board_edge_cases(board, expected_state):
    """Test para casos especiales"""
    result, _ = check_tic_tac_toe_board(board)
    assert result == expected_state


@pytest.mark.parametrize("board", [
    [["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]],
])
def test_check_tic_tac_toe_board_return_format(board):
    """Test para verificar el formato de retorno"""
    result = check_tic_tac_toe_board(board)

    # Debe retornar una tupla de 2 elementos
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Primer elemento debe ser el estado, segundo el mensaje
    state, message = result
    assert isinstance(state, str)
    assert isinstance(message, str)


# Tests para la función print_board
@pytest.mark.parametrize("board_id,board,status,txt", [
    # Tablero con victoria de X
    (0, [["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]], "X",
     "Partida finalizada correctamente"),
    # Tablero con victoria de O
    (1, [["O", "O", "O"], ["X", "X", " "], [" ", " ", " "]], "O",
     "Partida finalizada correctamente"),
    # Tablero con empate
    (2, [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]], "Empate",
     "Partida finalizada correctamente"),
    # Tablero con error
    (3, [["X", "X"], ["O", "O"]], "Nulo", "El tablero debe tener dimensiones 3x3"),
])
def test_print_board(board_id, board, status, txt, capsys):
    """Test para verificar la salida de la función print_board"""
    # Ejecutar la función que imprime
    print_board(board_id, board, status, txt)

    # Capturar la salida
    captured = capsys.readouterr()

    # Verificar que contiene elementos esperados
    assert f"TABLERO {board_id + 1:02}" in captured.out
    assert "===========" in captured.out
    assert f"Resultado: {status} -> {txt}" in captured.out

    # Verificar que tiene el formato de tablero (con | y ---)
    if len(board) == 3 and all(len(row) == 3 for row in board):
        assert "|" in captured.out  # Separadores de columnas
        assert "---" in captured.out  # Separadores de filas


def test_print_board_empty_cells():
    """Test específico para verificar el manejo de celdas vacías"""
    # Capturar salida manualmente
    old_stdout = sys.stdout
    sys.stdout = buffer = StringIO()

    try:
        board = [[" ", "", " "], ["X", " ", "O"], [" ", " ", " "]]
        print_board(0, board, "Empate", "Tablero con espacios")

        output = buffer.getvalue()

        # Verificar que las celdas vacías se muestran como espacios
        assert " " in output
        assert "X" in output
        assert "O" in output

    finally:
        sys.stdout = old_stdout


def test_print_board_format_consistency():
    """Test para verificar la consistencia del formato de salida"""
    old_stdout = sys.stdout
    sys.stdout = buffer = StringIO()

    try:
        board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
        print_board(5, board, "X", "Test message")

        output = buffer.getvalue()
        lines = output.strip().split('\n')

        # Verificar estructura esperada:
        # TABLERO 06
        # ===========
        # | X | O | X |
        # |---|---|---|
        # | O | X | O |
        # |---|---|---|
        # | X | O | X |
        #
        # Resultado: X -> Test message

        assert "TABLERO 06" in lines[0]
        assert "===========" in lines[1]
        assert "Resultado: X -> Test message" in output

    finally:
        sys.stdout = old_stdout
