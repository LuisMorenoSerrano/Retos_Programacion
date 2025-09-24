"""
    RETO #006: ASPECT RATIO DE UNA IMAGEN

    Crea un programa que se encargue de calcular el aspect ratio de una
    imagen a partir de una url.
    - Url de ejemplo:
      https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
    - Por ratio hacemos referencia por ejemplo a los "16:9" de una
      imagen de 1920*1080px.
"""

from io import BytesIO
from math import gcd

import requests
from PIL import Image


# Obtener el 'aspect ratio' de una imagen
def get_aspect_ratio(url: str) -> str:
    """
    Calcula el aspect ratio de una imagen desde una URL.

    Args:
        url: URL de la imagen

    Returns:
        String con formato "ratio_width:ratio_height (width*height)"
        o mensaje de error si no se puede procesar
    """
    try:
        # Descargar la imagen
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Abrir la imagen
        img = Image.open(BytesIO(response.content))

        # Obtener las dimensiones
        width, height = img.size

        # Calcular 'aspect ratio' y devolver
        common_div: int = gcd(width, height)
        ratio_width: int = width // common_div
        ratio_height: int = height // common_div

        return f"{ratio_width}:{ratio_height} ({width}*{height})"

    except requests.exceptions.RequestException as e:
        return f"Error al obtener la imagen: {e}"
    except IOError as e:
        return f"Error al procesar la imagen: {e}"


# Función principal
if __name__ == "__main__":
    # Ejemplo de uso
    example_url = ("https://raw.githubusercontent.com/mouredev/mouredev/"
                   "master/mouredev_github_profile.png")
    print(f"Imagen......: {example_url}")
    print(f"Aspect Ratio: {get_aspect_ratio(example_url)}")
