"""
    RETO #005: ÁREA DE UN POLÍGONO

    Crea una única función (importante que sólo sea una) que sea capaz
    de calcular y retornar el área de un polígono.
    - La función recibirá por parámetro sólo UN polígono a la vez.
    - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
    - Imprime el cálculo del área de un polígono de cada tipo.
"""

from abc import ABC, abstractmethod


# Clase genérica: Polígono
class Poligono(ABC):
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    def mostrar_area(self):
        print(
            f"Área del {self.nombre} "
            f"({self.detalles_especificos()}) = "
            f"{self.calcular_area():.3f}"
        )

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def detalles_especificos(self):
        pass


# Clase Polígono: Triángulo
class Triangulo(Poligono):
    base: float
    altura: float

    def __init__(self, base: float, altura: float):
        super().__init__("triángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura / 2.0

    def detalles_especificos(self):
        return f"base = {self.base:.3f}, altura = {self.altura:.3f}"


# Clase Polígono: Rectángulo
class Rectangulo(Poligono):
    largo: float
    ancho: float

    def __init__(self, largo: float, ancho: float):
        super().__init__("rectángulo")
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self) -> float:
        return self.largo * self.ancho

    def detalles_especificos(self):
        return f"largo = {self.largo:.3f}, ancho = {self.ancho:.3f}"


# Clase Polígono: Cuadrado
class Cuadrado(Poligono):
    lado: float

    def __init__(self, lado: float):
        super().__init__("cuadrado")
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado**2

    def detalles_especificos(self):
        return f"lado = {self.lado:.3f}"


# Calcular y mostrar el área de un Polígono
def area(poligono: Poligono):
    poligono.mostrar_area()

    return poligono.calcular_area()


# Función principal
if __name__ == "__main__":
    # Calcular y mostrar el área de varios polígonos
    area(Triangulo(10.0, 4.0))
    area(Rectangulo(12.5, 3.5))
    area(Cuadrado(8.234))
