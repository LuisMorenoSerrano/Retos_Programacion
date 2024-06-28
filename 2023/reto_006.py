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

import requests
from PIL import Image


# Calcular el máximo común divisor (MCD) de dos números
def mcd(n1, n2: int):
    while n2:
        n1, n2 = n2, n1 % n2

    return n1


# Obtener el 'aspect ratio' de una imagen
def get_aspect_ratio(url: str) -> str:
    # Descargar la imagen
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        try:
            image = Image.open(BytesIO(response.content))
        except IOError:
            print("Error al intentar abrir la imagen.")
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la respuesta: {e}")

    response = requests.get(url, timeout=10)
    image = Image.open(BytesIO(response.content))

    # Obtener las dimensiones
    width, height = image.size

    # Calcular 'aspect ratio' y devolver
    common_div: int = mcd(width, height)
    ratio_width: int = width // common_div
    ratio_height: int = height // common_div

    return f"{ratio_width}:{ratio_height} ({width}*{height})"


# Función principal
if __name__ == "__main__":
    imagenes = [
        "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png",
        "https://images.unsplash.com/photo-1433086966358-54859d0ed716",
        "https://images.unsplash.com/photo-1542372712-fc07597133cd",
        "https://images.unsplash.com/photo-1553696590-4b3f68898333",
        "https://images.unsplash.com/photo-1551368321-dddf8a05c459",
        "https://wallpaperaccess.com/full/2638458.jpg",
        "https://cdn.wallpapersafari.com/9/71/6acbpn.jpg",
        "https://wallpaperaccess.com/full/121194.jpg",
        "https://wallpaperaccess.com/full/4205192.jpg",
    ]

    for imagen in imagenes:
        print(f"Imagen......: {imagen}\nAspect Ratio: {get_aspect_ratio(imagen)}\n")
