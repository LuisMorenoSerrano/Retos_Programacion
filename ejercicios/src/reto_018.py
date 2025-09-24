"""
    RETO #018: LA CARRERA DE OBSTÁCULOS

    Crea una función que evalúe si un/a atleta ha superado correctamente una
    carrera de obstáculos.
    - La función recibirá dos parámetros:
         - Un array que sólo puede contener String con las palabras
           "run" o "jump"
         - Un String que represente la pista y sólo puede contener "_" (suelo)
           o "|" (valla)
    - La función imprimirá cómo ha finalizado la carrera:
         - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
           será correcto y no variará el símbolo de esa parte de la pista.
         - Si hace "jump" en "_" (suelo), se variará la pista por "x".
         - Si hace "run" en "|" (valla), se variará la pista por "/".
    - La función retornará un Boolean que indique si ha superado la carrera.
    Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""


# Comprobar estado ejecución de carrera
def check_obstacle_race(actions: list[str], track: str) -> tuple[bool, str]:
    # Declaraciones internas
    valid_actions = {"run": "_", "jump": "|"}

    # Control de errores
    num_actions        = len(actions)
    num_track_sections = len(track)

    if num_actions < num_track_sections:
        return False, (
            f"La carrera finaliza prematuramente con errores: {num_actions} acciones "
            f"< {num_track_sections} secciones de pista"
        )

    if num_actions > num_track_sections:
        return False, (
            f"Hay más acciones que longitud de pista - errores: ({num_actions}) "
            f"acciones vs ({num_track_sections}) secciones"
        )

    if not all(action in valid_actions for action in actions):
        valid_keys = ", ".join(f"'{action}'" for action in list(valid_actions.keys()))
        return False, f"Acciones inválidas - errores. Válidas: {valid_keys}"

    if not all(track_section in valid_actions.values() for track_section in track):
        valid_keys = ", ".join(f"'{action}'" for action in list(valid_actions.values()))
        return False, f"Secciones de pista inválidas - errores. Válidas: {valid_keys}"

    # Mostrar progreso carrera
    action_result: str
    race_result: bool = True

    print("CARRERA")
    print("=======")

    for action, track_section in zip(actions, track):
        if action == "jump" and track_section == "_":
            action_result = "x"
            race_result = False
        elif action == "run" and track_section == "|":
            action_result = "/"
            race_result = False
        else:
            action_result = track_section

        print(action_result, end="")

    print()

    # Devolver resultado carrera
    return race_result, "¡Carrera sin errores!" if race_result else "Carrera con errores..."
