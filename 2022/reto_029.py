"""
    Simula el funcionamiento de una máquina expendedora creando una operación
    que reciba dinero (array de monedas) y un número que indique la selección
    del producto.
    - El programa retornará el nombre del producto y un array con el dinero
      de vuelta (con el menor número de monedas).
    - Si el dinero es insuficiente o el número de producto no existe,
      deberá indicarse con un mensaje y retornar todas las monedas.
    - Si no hay dinero de vuelta, el array se retornará vacío.
    - Para que resulte más simple, trabajaremos en céntimos con monedas
      de 5, 10, 50, 100 y 200.
    - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""

from typing import List, Tuple

# Lista de productos para la máquina expendedora
products = [
    {"name": "Agua", "price": 100, "number": 10},
    {"name": "Refresco", "price": 150, "number": 11},
    {"name": "Zumo", "price": 120, "number": 12},
    {"name": "Galletas", "price": 200, "number": 13},
    {"name": "Chocolatina", "price": 250, "number": 14},
    {"name": "Patatas", "price": 180, "number": 15},
    {"name": "Chicle", "price": 50, "number": 16},
    {"name": "Barra de cereal", "price": 220, "number": 17},
    {"name": "Energizante", "price": 300, "number": 18},
    {"name": "Café", "price": 100, "number": 19},
]

# Lista de monedas soportadas por la máquina
coins = [5, 10, 50, 100, 200]


# Simular el funcionamiento de la máquina expendedora
def supply_product(money: List[int], product_id: int) -> Tuple[str, int, List[int]]:
    # Control de errores
    if not all(isinstance(coin, int) for coin in money):
        raise TypeError("El dinero enviado debe ser una lista de enteros.")

    invalid_coins = [coin for coin in money if coin not in coins]

    if invalid_coins:
        raise ValueError(
            f"La máquina no acepta las siguientes monedas: {invalid_coins}"
        )

    if not isinstance(product_id, int):
        raise TypeError("El número de producto debe ser un entero.")

    # Buscar el producto seleccionado
    product = next(
        (product for product in products if product["number"] == product_id), None
    )

    if product is None:
        raise ValueError(f"Producto no encontrado: {product_id}")

    # Calcular el total de dinero enviado
    total_money = sum(money)

    if total_money < product["price"]:
        raise ValueError(f"Dinero insuficiente: {total_money} < {product['price']}")

    # Calcular el cambio
    change = total_money - product["price"]
    change_coins = []

    for coin in sorted(coins, reverse=True):
        while change >= coin:
            change_coins.append(coin)
            change -= coin

    return product["name"], product["price"], change_coins


# Función principal
if __name__ == "__main__":
    # Lista de pruebas
    tests = [
        ([5, 10, 50.5, 100], 10),
        ([5, 10, 4, 50, 125, 100], 10),
        ([100, 100, 100, 100, 100], "10"),
        ([100, 100, 100, 100, 100], 19.5),
        ([100, 100, 100, 100, 100], 20),
        ([5, 10, 50], 10),
        ([200, 200], 14),
        ([50, 50, 50, 50, 50, 50, 50, 50, 50, 50], 16),
        ([200, 200, 200, 200, 200, 200, 200, 200, 200, 200], 18),
        ([50, 50], 10),
        ([100, 100, 100, 100, 100], 11),
        ([100, 100, 100, 100, 100], 12),
        ([100, 100, 100, 100, 100], 13),
        ([100, 100, 100, 100, 100], 14),
        ([100, 100, 100, 100, 100], 15),
        ([100, 100, 100, 100, 100], 16),
        ([100, 100, 100, 100, 100], 17),
        ([100, 100, 100, 100, 100], 18),
        ([100, 100, 100, 100, 100], 19),
    ]

    print("MÁQUINA EXPENDEDORA")
    print("====================", end="")

    for money_supplied, product_number in tests:
        print(f"\nDinero: {money_supplied} - Número: {product_number}")

        try:
            product_selected, price, change_returned = supply_product(
                money_supplied, product_number
            )
            print(
                f"Producto: {product_selected} - Precio: {price} - Cambio: {change_returned}"
            )
        except (TypeError, ValueError) as e:
            print(e)
