"""
    RETO #036: BATALLA POKÉMON

    Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
    - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
    - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
    - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
    - El programa recibe los siguientes parámetros:
      - Tipo del Pokémon atacante.
      - Tipo del Pokémon defensor.
      - Ataque: Entre 1 y 100.
      - Defensa: Entre 1 y 100.
"""

from enum import Enum
from typing import Union


class TipoPokemon(Enum):
    """Enumera los tipos de Pokémon disponibles"""
    AGUA = "Agua"
    FUEGO = "Fuego"
    PLANTA = "Planta"
    ELECTRICO = "Eléctrico"


class Efectividad(Enum):
    """Enumera los tipos de efectividad"""
    SUPER_EFECTIVO = 2.0
    NEUTRAL = 1.0
    NO_MUY_EFECTIVO = 0.5


def obtener_efectividad(tipo_atacante: TipoPokemon, tipo_defensor: TipoPokemon) -> float:
    """
    Obtiene la efectividad del ataque según los tipos de Pokémon.

    Args:
        tipo_atacante: Tipo del Pokémon que ataca
        tipo_defensor: Tipo del Pokémon que defiende

    Returns:
        Multiplicador de efectividad (0.5, 1.0 o 2.0)
    """
    # Tabla de efectividades tipo vs tipo
    efectividades = {
        # Agua
        (TipoPokemon.AGUA, TipoPokemon.FUEGO): Efectividad.SUPER_EFECTIVO,
        (TipoPokemon.AGUA, TipoPokemon.PLANTA): Efectividad.NO_MUY_EFECTIVO,
        (TipoPokemon.AGUA, TipoPokemon.ELECTRICO): Efectividad.NEUTRAL,
        (TipoPokemon.AGUA, TipoPokemon.AGUA): Efectividad.NEUTRAL,

        # Fuego
        (TipoPokemon.FUEGO, TipoPokemon.PLANTA): Efectividad.SUPER_EFECTIVO,
        (TipoPokemon.FUEGO, TipoPokemon.AGUA): Efectividad.NO_MUY_EFECTIVO,
        (TipoPokemon.FUEGO, TipoPokemon.ELECTRICO): Efectividad.NEUTRAL,
        (TipoPokemon.FUEGO, TipoPokemon.FUEGO): Efectividad.NEUTRAL,

        # Planta
        (TipoPokemon.PLANTA, TipoPokemon.AGUA): Efectividad.SUPER_EFECTIVO,
        (TipoPokemon.PLANTA, TipoPokemon.FUEGO): Efectividad.NO_MUY_EFECTIVO,
        (TipoPokemon.PLANTA, TipoPokemon.ELECTRICO): Efectividad.NEUTRAL,
        (TipoPokemon.PLANTA, TipoPokemon.PLANTA): Efectividad.NEUTRAL,

        # Eléctrico
        (TipoPokemon.ELECTRICO, TipoPokemon.AGUA): Efectividad.SUPER_EFECTIVO,
        (TipoPokemon.ELECTRICO, TipoPokemon.FUEGO): Efectividad.NEUTRAL,
        (TipoPokemon.ELECTRICO, TipoPokemon.PLANTA): Efectividad.NEUTRAL,
        (TipoPokemon.ELECTRICO, TipoPokemon.ELECTRICO): Efectividad.NEUTRAL,
    }

    return efectividades[(tipo_atacante, tipo_defensor)].value


def calcular_dano_pokemon(
    tipo_atacante: Union[str, TipoPokemon],
    tipo_defensor: Union[str, TipoPokemon],
    ataque: int,
    defensa: int
) -> float:
    """
    Calcula el daño de un ataque Pokémon usando la fórmula oficial.

    Args:
        tipo_atacante: Tipo del Pokémon atacante ("Agua", "Fuego", "Planta", "Eléctrico")
        tipo_defensor: Tipo del Pokémon defensor ("Agua", "Fuego", "Planta", "Eléctrico")
        ataque: Estadística de ataque (entre 1 y 100)
        defensa: Estadística de defensa (entre 1 y 100)

    Returns:
        Daño calculado usando la fórmula: 50 * (ataque / defensa) * efectividad

    Raises:
        ValueError: Si los tipos no son válidos o las estadísticas están fuera de rango
        TypeError: Si los tipos de datos no son correctos
    """
    # Validar tipos de datos
    if not isinstance(ataque, int) or not isinstance(defensa, int):
        raise TypeError("Las estadísticas de ataque y defensa deben ser números enteros")

    # Validar rangos de estadísticas
    if not 1 <= ataque <= 100:
        raise ValueError("El ataque debe estar entre 1 y 100")
    if not 1 <= defensa <= 100:
        raise ValueError("La defensa debe estar entre 1 y 100")

    # Convertir strings a enums si es necesario
    if isinstance(tipo_atacante, str):
        try:
            tipo_atacante = TipoPokemon(tipo_atacante)
        except ValueError as exc:
            tipos_validos = [t.value for t in TipoPokemon]
            raise ValueError(f"Tipo atacante '{tipo_atacante}' no válido. "
                             f"Tipos válidos: {tipos_validos}") from exc

    if isinstance(tipo_defensor, str):
        try:
            tipo_defensor = TipoPokemon(tipo_defensor)
        except ValueError as exc:
            tipos_validos = [t.value for t in TipoPokemon]
            raise ValueError(f"Tipo defensor '{tipo_defensor}' no válido. "
                             f"Tipos válidos: {tipos_validos}") from exc

    # Validar que son enums TipoPokemon
    if not isinstance(tipo_atacante, TipoPokemon):
        raise TypeError("tipo_atacante debe ser string o TipoPokemon")
    if not isinstance(tipo_defensor, TipoPokemon):
        raise TypeError("tipo_defensor debe ser string o TipoPokemon")

    # Obtener efectividad del matchup
    efectividad = obtener_efectividad(tipo_atacante, tipo_defensor)

    # Calcular daño usando la fórmula: 50 * (ataque / defensa) * efectividad
    dano = 50 * (ataque / defensa) * efectividad

    return dano


def mostrar_resultado_batalla(
    tipo_atacante: Union[str, TipoPokemon],
    tipo_defensor: Union[str, TipoPokemon],
    ataque: int,
    defensa: int,
    dano: float
) -> str:
    """
    Muestra el resultado de la batalla de forma formateada.

    Returns:
        String con el resultado de la batalla
    """
    # Convertir a string si son enums
    if isinstance(tipo_atacante, TipoPokemon):
        tipo_atacante = tipo_atacante.value
    if isinstance(tipo_defensor, TipoPokemon):
        tipo_defensor = tipo_defensor.value

    # Determinar tipo de efectividad para el mensaje
    if isinstance(tipo_atacante, str):
        tipo_atk = TipoPokemon(tipo_atacante)
    else:
        tipo_atk = tipo_atacante

    if isinstance(tipo_defensor, str):
        tipo_def = TipoPokemon(tipo_defensor)
    else:
        tipo_def = tipo_defensor

    efectividad = obtener_efectividad(tipo_atk, tipo_def)

    if efectividad == 2.0:
        efectividad_msg = "¡Es súper efectivo!"
    elif efectividad == 0.5:
        efectividad_msg = "No es muy efectivo..."
    else:
        efectividad_msg = "Es efectivo."

    return (f"Pokémon {tipo_atacante} (ATQ: {ataque}) ataca a "
            f"Pokémon {tipo_defensor} (DEF: {defensa})\n"
            f"Daño causado: {dano:.1f}\n"
            f"{efectividad_msg}")
