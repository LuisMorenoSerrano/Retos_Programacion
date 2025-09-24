"""Tests para RETO #006: ASPECT RATIO DE UNA IMAGEN"""
import sys
import os

from unittest.mock import Mock, patch
from io import BytesIO
from PIL import Image
import requests

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest                          # pylint: disable=wrong-import-position
from reto_006 import get_aspect_ratio  # pylint: disable=import-error,wrong-import-position # type: ignore


@pytest.mark.parametrize("width,height,expected_ratio", [
    (1920, 1080, "16:9"),
    (800, 600, "4:3"),
    (500, 500, "1:1"),
    (640, 480, "4:3"),
    (1280, 720, "16:9"),
    (1024, 768, "4:3"),
])
@patch('reto_006.requests.get')
def test_aspect_ratios_parametrized(mock_get, width, height, expected_ratio):
    """Test parametrizado para diferentes aspect ratios"""
    # Crear una imagen mock
    img = Image.new('RGB', (width, height), color='red')
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    mock_response = Mock()
    mock_response.content = img_bytes.getvalue()
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    resultado = get_aspect_ratio("http://test.com/image.png")
    expected = f"{expected_ratio} ({width}*{height})"
    assert resultado == expected


@pytest.mark.parametrize("exception,expected_message", [
    (requests.exceptions.ConnectionError("No connection"), "Error al obtener la imagen"),
    (requests.exceptions.Timeout("Timeout"), "Error al obtener la imagen"),
    (requests.exceptions.HTTPError("404 Not Found"), "Error al obtener la imagen"),
])
@patch('reto_006.requests.get')
def test_errores_parametrized(mock_get, exception, expected_message):
    """Test parametrizado para diferentes tipos de errores"""
    mock_get.side_effect = exception

    resultado = get_aspect_ratio("http://invalid.url/image.png")
    assert expected_message in resultado


@pytest.mark.parametrize("mock_content,url,expected_message", [
    (b"Esto no es una imagen", "http://test.com/notimage.txt", "Error al procesar la imagen"),
])
@patch('reto_006.requests.get')
def test_error_imagen_invalida(mock_get, mock_content, url, expected_message):
    """Test para contenido que no es una imagen válida"""
    mock_response = Mock()
    mock_response.content = mock_content
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    resultado = get_aspect_ratio(url)
    assert expected_message in resultado


# URLs reales para tests de integración (se saltan por defecto)
REAL_IMAGE_URLS = [
    "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png",
    "https://images.unsplash.com/photo-1433086966358-54859d0ed716",
    "https://images.unsplash.com/photo-1542372712-fc07597133cd",
]


@pytest.mark.parametrize("url", REAL_IMAGE_URLS)
@pytest.mark.integration
def test_imagenes_reales_integration(url):
    """Test de integración con URLs reales (usar -m integration para ejecutar)"""
    resultado = get_aspect_ratio(url)

    # Verificar que el resultado tiene el formato esperado o es un error de conexión
    assert (":" in resultado and "*" in resultado) or "Error" in resultado
