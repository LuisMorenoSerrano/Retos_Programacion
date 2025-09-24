"""
    RETO #005: ÁREA DE UN POLÍGONO

    Crea una única función (importante que sólo sea una) que sea capaz
    de calcular y retornar el área de un polígono.
    - La función recibirá por parámetro sólo UN polígono a la vez.
    - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
    - Imprime el cálculo del área de un polígono de cada tipo.
"""

from abc import ABC, abstractmethod


class Poligono(ABC):
    """Clase genérica abstracta para polígonos."""

    def __init__(self, nombre: str):
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre

    def mostrar_area(self) -> None:
        """Muestra el área del polígono con formato específico."""
        print(
            f"Área del {self.nombre} "
            f"({self.detalles_especificos()}) = "
            f"{self.calcular_area():.3f}"
        )

    @abstractmethod
    def calcular_area(self) -> float:
        """Calcula el área del polígono."""

    @abstractmethod
    def detalles_especificos(self) -> str:
        """Retorna los detalles específicos del polígono."""


class Triangulo(Poligono):
    """Clase para polígono tipo triángulo."""

    def __init__(self, base: float, altura: float):
        super().__init__("triángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura / 2.0

    def detalles_especificos(self) -> str:
        return f"base = {self.base:.3f}, altura = {self.altura:.3f}"


class Rectangulo(Poligono):
    """Clase para polígono tipo rectángulo."""

    def __init__(self, largo: float, ancho: float):
        super().__init__("rectángulo")
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self) -> float:
        return self.largo * self.ancho

    def detalles_especificos(self) -> str:
        return f"largo = {self.largo:.3f}, ancho = {self.ancho:.3f}"


class Cuadrado(Poligono):
    """Clase para polígono tipo cuadrado."""

    def __init__(self, lado: float):
        super().__init__("cuadrado")
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado**2

    def detalles_especificos(self) -> str:
        return f"lado = {self.lado:.3f}"


def area(poligono: Poligono) -> float:
    """
    Calcular y mostrar el área de un Polígono.

    Args:
        poligono: Instancia de un polígono

    Returns:
        El área calculada del polígono
    """
    poligono.mostrar_area()
    return poligono.calcular_area()
