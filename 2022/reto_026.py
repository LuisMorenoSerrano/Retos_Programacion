"""
    RETO #026: PIEDRA, PAPEL, TIJERA

    Crea un programa que calcule quien gana más partidas al piedra,
    papel, tijera.
    - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
    - La función recibe un listado que contiene pares, representando cada jugada.
    - El par puede contener combinaciones de "R" (piedra), "P" (papel)
      o "S" (tijera).
    - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""


def rock_paper_scissors(playlist: list) -> str:
    # Declaraciones internas
    valid_moves = {"R", "P", "S"}
    winner_moves = {"R": "S", "P": "R", "S": "P"}

    # Control de errores
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in playlist):
        return "Error: La partida debe ser una lista de pares de movimientos"

    invalid_move = next(
        (move for pair in playlist for move in pair if move not in valid_moves), None
    )

    if invalid_move:
        return f"Error: El movimiento '{invalid_move}' no es válido"

    # Analizar movimientos de la partida
    player_1_wins = sum(1 for move in playlist if winner_moves[move[0]] == move[1])
    player_2_wins = sum(1 for move in playlist if winner_moves[move[1]] == move[0])

    result = f" ({player_1_wins}/{player_2_wins})"
    winner = (
             "Player 1" if player_1_wins > player_2_wins
        else "Player 2" if player_2_wins > player_1_wins
        else "Tie"
    )

    return winner + result


# Función principal
if __name__ == "__main__":
    # Lista de partidas a comprobar
    games = [
        [("R", "S"), ("S")],
        [("R", "S", "S"), ("S", "P")],
        [("R", "S"), ("Z", "R"), ("P", "S")],
        [("R", "S"), ("P", "R"), ("S", "R"), ("P", "S"), ("S", "P")],
        [("R", "S"), ("S", "R"), ("P", "S")],
        [("R", "S"), ("P", "R"), ("S", "R"), ("P", "S"), ("S", "P"), ("S", "R")],
    ]

    print("PARTIDAS: PIEDRA (R), PAPEL (P), TIJERA (S)")
    print("===========================================")

    for game in games:
        print(f"Partida: {game}")
        print(f"Ganador: {rock_paper_scissors(game)}\n")
