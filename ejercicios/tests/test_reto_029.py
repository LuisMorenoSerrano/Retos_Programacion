"""Tests para RETO #029: MÁQUINA EXPENDEDORA"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                        # pylint: disable=wrong-import-position
from reto_029 import supply_product  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("money,product_id,expected_name,expected_price,expected_change", [
    # Casos exitosos - dinero exacto
    ([100], 10, "Agua", 100, []),                   # Agua - precio exacto
    ([50], 16, "Chicle", 50, []),                   # Chicle - precio exacto
    ([200, 50], 14, "Chocolatina", 250, []),        # Chocolatina - precio exacto
    ([100, 100, 100], 18, "Energizante", 300, []),  # Energizante - precio exacto

    # Casos exitosos - con cambio
    ([200], 10, "Agua", 100, [100]),                           # Agua con cambio de 100
    ([200, 200], 14, "Chocolatina", 250, [100, 50]),           # Chocolatina con cambio de 150
    ([200, 200, 200], 18, "Energizante", 300, [200, 100]),     # Energizante con cambio
    ([100, 100, 100, 100, 100], 19, "Café", 100, [200, 200]),  # Café con cambio grande

    # Casos con diferentes combinaciones de monedas
    ([50, 50, 50, 50, 50, 50, 50, 50, 50, 50], 16, "Chicle", 50,
     [200, 200, 50]),                                            # 500 céntimos, chicle 50
    ([100, 50, 10, 10, 10, 10, 10], 11, "Refresco", 150, [50]),  # 200 céntimos, refresco 150
])
def test_supply_product_success(money, product_id, expected_name, expected_price, expected_change):
    """Test de casos exitosos de la máquina expendedora"""
    name, price, change = supply_product(money, product_id)
    assert name == expected_name
    assert price == expected_price
    assert change == expected_change


@pytest.mark.parametrize("money,product_id", [
    # Dinero insuficiente
    ([50, 10], 10),  # 60 céntimos para agua que cuesta 100 - insuficiente
    ([50], 10),      # 50 céntimos para agua que cuesta 100
    ([100], 14),     # 100 céntimos para chocolatina que cuesta 250
    ([200], 18),     # 200 céntimos para energizante que cuesta 300
])
def test_supply_product_insufficient_money(money, product_id):
    """Test de casos con dinero insuficiente"""
    with pytest.raises(ValueError, match="Dinero insuficiente"):
        supply_product(money, product_id)


@pytest.mark.parametrize("money,product_id", [
    # Producto no existe
    ([200], 20),   # Producto 20 no existe
    ([100], 9),    # Producto 9 no existe
    ([100], 100),  # Producto 100 no existe
    ([100], -1),   # Producto negativo
])
def test_supply_product_invalid_product(money, product_id):
    """Test de casos con productos inexistentes"""
    with pytest.raises(ValueError, match="Producto no encontrado"):
        supply_product(money, product_id)


@pytest.mark.parametrize("money,product_id", [
    # Monedas no soportadas
    ([5, 10, 4, 50, 125, 100], 10),  # Monedas 4 y 125 no válidas
    ([1, 100], 10),                  # Moneda de 1 céntimo no válida
    ([500], 10),                     # Moneda de 500 céntimos no válida
    ([25, 100], 10),                 # Moneda de 25 céntimos no válida
])
def test_supply_product_invalid_coins(money, product_id):
    """Test de casos con monedas no soportadas"""
    with pytest.raises(ValueError, match="La máquina no acepta las siguientes monedas"):
        supply_product(money, product_id)


@pytest.mark.parametrize("money,product_id", [
    # Tipos incorrectos en dinero
    ([5, 10, 50.5, 100], 10),  # Float en lugar de int
    (["5", "10"], 10),         # Strings en lugar de ints
    ([5, None, 10], 10),       # None en la lista
])
def test_supply_product_invalid_money_type(money, product_id):
    """Test de casos con tipos incorrectos en el dinero"""
    with pytest.raises(TypeError, match="El dinero enviado debe ser una lista de enteros"):
        supply_product(money, product_id)


@pytest.mark.parametrize("money,product_id", [
    # Tipos incorrectos en product_id
    ([100], "10"),  # String en lugar de int
    ([100], 19.5),  # Float en lugar de int
    ([100], None),  # None
])
def test_supply_product_invalid_product_type(money, product_id):
    """Test de casos con tipos incorrectos en product_id"""
    with pytest.raises(TypeError, match="El número de producto debe ser un entero"):
        supply_product(money, product_id)


@pytest.mark.parametrize("money,product_id,expected_total_change", [
    # Verificar que el cambio sea correcto en términos de valor total
    ([200, 200, 200], 10, 500),            # 600 - 100 = 500 de cambio
    ([200, 200, 200, 200, 200], 18, 700),  # 1000 - 300 = 700 de cambio
    ([100, 100, 50, 50, 50], 12, 230),     # 350 - 120 = 230 de cambio
])
def test_supply_product_change_amount(money, product_id, expected_total_change):
    """Test para verificar que el cambio total sea correcto"""
    _, _, change = supply_product(money, product_id)
    assert sum(change) == expected_total_change


@pytest.mark.parametrize("product_id", [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
def test_supply_product_products_available(product_id):
    """Test para verificar que todos los productos definidos están disponibles"""
    # Usar dinero suficiente para cualquier producto
    money = [200, 200, 200]  # 600 céntimos
    name, price, change = supply_product(money, product_id)

    # Verificar que se devuelve información válida
    assert isinstance(name, str)
    assert len(name) > 0
    assert isinstance(price, int)
    assert price > 0
    assert isinstance(change, list)
    assert sum(change) == 600 - price
