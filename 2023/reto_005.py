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
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def mostrar_area(self):
        pass

# Clase Polígono: Triángulo
class Triangulo(Poligono):
    def __init__(self, base: float, altura: float):
        self.base   = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura / 2.0

    def mostrar_area(self):
        print("Área del triángulo ("
            f"base = {self.base:.3f}, "
            f"altura = {self.altura:.3f}) = "
            f"{self.calcular_area():.3f}"
        )

# Clase Polígono: Rectángulo
class Rectangulo(Poligono):
    def __init__(self, largo: float, ancho: float):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self) -> float:
        return self.largo * self.ancho

    def mostrar_area(self):
        print("Área del rectángulo ("
            f"largo = {self.largo:.3f}, "
            f"ancho = {self.ancho:.3f}) = "
            f"{self.calcular_area():.3f}"
        )

# Clase Polígono: Cuadrado
class Cuadrado(Poligono):
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado

    def mostrar_area(self):
        print("Área del cuadrado ("
            f"lado = {self.lado:.3f}) = "
            f"{self.calcular_area():.3f}"
        )

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
