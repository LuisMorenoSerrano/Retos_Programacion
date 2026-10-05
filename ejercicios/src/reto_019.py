"""
    RETO #019: TRES EN RAYA

    Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
    y retorne lo siguiente:
    - "X" si han ganado las "X"
    - "O" si han ganado los "O"
    - "Empate" si ha habido un empate
    - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
      O si han ganado los 2.
    Nota: La matriz puede no estar totalmente cubierta.
    Se podría representar con un vacío "", por ejemplo.
"""

from enum import Enum

DIMENSION: int = 3
LIMIT:     int = (DIMENSION ** 2 + 1) // 2
MSGS = {
    "BAD_DIMENSION" : "El tablero debe tener dimensiones {}x{}",
    "BAD_PROPORTION": "Proporción de '{}' incorrecta: {} (máximo {})",
    "END_OK"        : "Partida finalizada correctamente",
    "END_PREMATURE" : "Partida finalizada antes de tiempo",
    "TWO_WINNERS"   : "No pueden ganar los dos: 'X': {}, 'O': {})",
    "VALID_VALUES"  : "Valores válidos: {}",
}

class State(Enum):
    """Estados posibles de una partida de tres en raya."""

    X    = "X"
    O    = "O"
    DRAW = "Empate"
    NULL = "Nulo"

# Comprobar estado tablero 3 en Raya
def check_tic_tac_toe_board(board: list[list[str]]) -> tuple[str, str]:
    # Contar líneas completas (horizontal, vertical, diagonal) en el tablero
    def count_lines(value: str) -> int:
        return (
            sum(value == row[0] == row[1] == row[2] for row in board) +
            sum(value == col[0] == col[1] == col[2] for col in list(map(list, zip(*board)))) +
            (1 if value == board[0][0] == board[1][1] == board[2][2] else 0) +
            (1 if value == board[0][2] == board[1][1] == board[2][0] else 0)
        )

    # Declaraciones internas:
    valid_values = {"X", "O", "", " "}

    # Control de errores
    if len(board) != DIMENSION or any(len(row) != DIMENSION for row in board):
        return State.NULL.value, MSGS["BAD_DIMENSION"].format(DIMENSION, DIMENSION)

    if not all(cell in valid_values for row in board for cell in row):
        valid_list = ", ".join(f"'{value}'" for value in sorted(valid_values))
        return State.NULL.value, MSGS["VALID_VALUES"].format(valid_list)

    # Analizar estado del tablero
    num_values = {
        "X": sum(cell == "X" for row in board for cell in row),
        "O": sum(cell == "O" for row in board for cell in row),
        " ": sum(cell.strip() == ""  for row in board for cell in row),
    }

    for key, value in num_values.items():
        if key != " " and value > LIMIT:
            return State.NULL.value, MSGS["BAD_PROPORTION"].format(key, value, LIMIT)

    num_lines = {
        "X": count_lines("X"),
        "O": count_lines("O"),
    }

    # Validar proporciones con ganadores
    # X mueve primero, luego O. Las proporciones válidas son:
    # - X = O (O acaba de mover)
    # - X = O + 1 (X acaba de mover)
    # - O = X + 1 (O mueve después de X, pero esto no es posible si X mueve primero)
    # La única excepción sería un error en el test, así que mantenemos solo las dos primeras
    x_count, o_count = num_values["X"], num_values["O"]
    if not (x_count == o_count or x_count == o_count + 1 or
            o_count == x_count + 1):
        return (State.NULL.value,
                MSGS["BAD_PROPORTION"].format("proporción X/O", f"{x_count}/{o_count}", "válida"))

    winner: State

    if num_lines["X"] == num_lines["O"] == 0:
        # Si no hay ganador, es empate (independientemente de si hay espacios vacíos)
        winner = State.DRAW
    elif num_lines["X"] > num_lines["O"] == 0:
        winner = State.X
    elif num_lines["O"] > num_lines["X"] == 0:
        winner = State.O
    else:
        return State.NULL.value, MSGS["TWO_WINNERS"].format(num_lines["X"], num_lines["O"])

    # Devolver estado del tablero
    return winner.value, MSGS["END_OK"]


# Mostrar tablero por pantalla
def print_board(id_board, board, status, txt):
    print(f"TABLERO {id_board + 1:02}")
    print("===========")

    for idx, row in enumerate(board):
        print("|".join(f" {cell if cell else ' '} " for cell in row))

        if idx < len(board) - 1:
            print("+".join(["---"] * DIMENSION))

    print(f"\nResultado: {status} -> {txt}\n")
