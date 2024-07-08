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


# Función principal
async def main():
    numbers = [(0, 0), (-3, 0), (12, 24), (-37, -12), (27, -28), (3, 14)]

    # Llamada síncrona
    print("Sumas con retraso (llamada síncrona):")

    for numtuple in numbers:
        print(f"{numtuple[0]:3} + {numtuple[1]:3} = ", end="", flush=True)
        print(f"{sum_delayed(*numtuple, DELAY):3}")

    # Llamada asíncrona
    print("\nSumas con retraso (llamada asíncrona):")

    tasks = [sum_delayed_async(*numtuple, DELAY) for numtuple in numbers]
    results = await asyncio.gather(*tasks)

    for numtuple, result in zip(numbers, results):
        print(f"{numtuple[0]:3} + {numtuple[1]:3} = {result:3}")


if __name__ == "__main__":
    asyncio.run(main())
