"""
    RETO #004: ¿ES UN NÚMERO PRIMO?

    Escribe un programa que se encargue de comprobar si un número es o no primo.
    Hecho esto, imprime los números primos entre 1 y 100.
"""
# Comprobar si un número es primo (divisible sólo por sí mismo y por 1)
def es_primo(numero: int) -> bool:
    if numero <= 1:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True

# Función principal
if __name__ == "__main__":
    print("NÚMEROS PRIMOS ENTRE 1 Y 100")
    print("============================")

    for valor in range(1, 101):
        if es_primo(valor):
            print(f"{valor:2d}")
