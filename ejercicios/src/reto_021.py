"""
    RETO #021: PARANDO EL TIEMPO

    Crea una función que sume 2 números y retorne su resultado pasados
    unos segundos.
    - Recibirá por parámetros los 2 números a sumar y los segundos que
      debe tardar en finalizar su ejecución.
    - Si el lenguaje lo soporta, deberá retornar el resultado de forma
      asíncrona, es decir, sin detener la ejecución del programa principal.
      Se podría ejecutar varias veces al mismo tiempo.
"""

import asyncio
import time

DELAY = 2


# Sumar 2 números con retardo (versión síncrona)
def sum_delayed(num1: int, num2: int, delay: int) -> int:
    time.sleep(delay)

    return num1 + num2


# Sumar 2 números con retardo (versión asíncrona)
async def sum_delayed_async(num1: int, num2: int, delay: int) -> int:
    await asyncio.sleep(delay)

    return num1 + num2
