"""Tests para RETO #021: OPERACIONES CON DELAY SÍNCRONAS Y ASÍNCRONAS"""
import sys
import os
import asyncio
import time

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest  # pylint: disable=wrong-import-position
from reto_021 import sum_delayed, sum_delayed_async  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("num1,num2,expected", [
    (0, 0, 0),
    (1, 1, 2),
    (-3, 0, -3),
    (12, 24, 36),
    (-37, -12, -49),
    (27, -28, -1),
    (3, 14, 17),
    (100, -50, 50),
    (-100, -100, -200),
])
def test_sum_delayed_sync(num1, num2, expected):
    """Test para suma síncrona con delay"""
    # Test con delay muy pequeño para no ralentizar las pruebas
    result = sum_delayed(num1, num2, 0.001)
    assert result == expected


@pytest.mark.parametrize("num1,num2,expected", [
    (0, 0, 0),
    (1, 1, 2),
    (-3, 0, -3),
    (12, 24, 36),
    (-37, -12, -49),
    (27, -28, -1),
    (3, 14, 17),
    (100, -50, 50),
    (-100, -100, -200),
])
@pytest.mark.asyncio
async def test_sum_delayed_async(num1, num2, expected):
    """Test para suma asíncrona con delay"""
    # Test con delay muy pequeño para no ralentizar las pruebas
    result = await sum_delayed_async(num1, num2, 0.001)
    assert result == expected


@pytest.mark.parametrize("num1,num2,delay,expected", [
    (1, 2, 0.1, 3),
])
def test_sum_delayed_sync_timing(num1, num2, delay, expected):
    """Test para verificar que la función síncrona efectivamente espera"""
    start_time = time.time()
    result = sum_delayed(num1, num2, delay)
    end_time = time.time()

    assert result == expected
    assert end_time - start_time >= delay


@pytest.mark.parametrize("num1,num2,delay,expected", [
    (1, 2, 0.1, 3),
])
@pytest.mark.asyncio
async def test_sum_delayed_async_timing(num1, num2, delay, expected):
    """Test para verificar que la función asíncrona efectivamente espera"""
    start_time = time.time()
    result = await sum_delayed_async(num1, num2, delay)
    end_time = time.time()

    assert result == expected
    assert end_time - start_time >= delay


@pytest.mark.parametrize("numbers,delay,expected_results", [
    ([(1, 2), (3, 4), (5, 6)], 0.1, [3, 7, 11]),
])
@pytest.mark.asyncio
async def test_sum_delayed_async_concurrency(numbers, delay, expected_results):
    """Test para verificar que las llamadas asíncronas son concurrentes"""
    start_time = time.time()

    # Ejecutar todas las tareas concurrentemente
    tasks = [sum_delayed_async(a, b, delay) for a, b in numbers]
    results = await asyncio.gather(*tasks)

    end_time = time.time()

    # Verificar resultados
    assert results == expected_results

    # El tiempo total debería ser aproximadamente el delay (no delay * cantidad)
    # porque se ejecutan concurrentemente
    assert end_time - start_time < delay * len(numbers)
    assert end_time - start_time >= delay


@pytest.mark.parametrize("numbers,delay,expected_results", [
    ([(1, 2), (3, 4), (5, 6)], 0.05, [3, 7, 11]),
])
def test_sum_delayed_sync_multiple_calls(numbers, delay, expected_results):
    """Test para verificar múltiples llamadas síncronas consecutivas"""
    start_time = time.time()

    results = []
    for a, b in numbers:
        result = sum_delayed(a, b, delay)
        results.append(result)

    end_time = time.time()

    # Verificar resultados
    assert results == expected_results

    # El tiempo total debería ser aproximadamente delay * cantidad
    # porque se ejecutan secuencialmente
    assert end_time - start_time >= delay * len(numbers)


@pytest.mark.parametrize("delay", [0, 0.001, 0.01, 0.1])
def test_sum_delayed_sync_different_delays(delay):
    """Test para diferentes valores de delay en función síncrona"""
    start_time = time.time()
    result = sum_delayed(10, 20, delay)
    end_time = time.time()

    assert result == 30
    assert end_time - start_time >= delay


@pytest.mark.parametrize("delay", [0, 0.001, 0.01, 0.1])
@pytest.mark.asyncio
async def test_sum_delayed_async_different_delays(delay):
    """Test para diferentes valores de delay en función asíncrona"""
    start_time = time.time()
    result = await sum_delayed_async(10, 20, delay)
    end_time = time.time()

    assert result == 30
    assert end_time - start_time >= delay


@pytest.mark.parametrize("num1,num2,delay,expected", [
    # Números muy grandes
    (1000000, 2000000, 0.001, 3000000),
    # Números muy pequeños
    (-1000000, -2000000, 0.001, -3000000),
    # Delay cero
    (1, 1, 0, 2),
])
def test_sum_delayed_edge_cases(num1, num2, delay, expected):
    """Test para casos límite"""
    result = sum_delayed(num1, num2, delay)
    assert result == expected


@pytest.mark.parametrize("num1,num2,delay,expected", [
    # Números muy grandes
    (1000000, 2000000, 0.001, 3000000),
    # Números muy pequeños
    (-1000000, -2000000, 0.001, -3000000),
    # Delay cero
    (1, 1, 0, 2),
])
@pytest.mark.asyncio
async def test_sum_delayed_async_edge_cases(num1, num2, delay, expected):
    """Test para casos límite de función asíncrona"""
    result = await sum_delayed_async(num1, num2, delay)
    assert result == expected
