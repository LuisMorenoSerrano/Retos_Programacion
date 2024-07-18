"""
    RETO #027: CUADRADO Y TRIÁNGULO 2D

    Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
    - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
    - EXTRA: ¿Eres capaz de dibujar más figuras?
"""

from abc import ABC, abstractmethod


# Clase genérica: Polígono regular
class RegularPolygon(ABC):
    def __init__(self, num_sides: int, side_length: int):
        self._num_sides: int = num_sides
        self._side_length: int = side_length

    @property
    def num_sides(self) -> int:
        return self._num_sides

    @property
    def side_length(self) -> int:
        return self._side_length

    def _check_side_length(self) -> bool:
        if self._side_length < 2:
            print("Error: La longitud del lado debe ser mayor que 1.")
            return False
        return True

    def __str__(self) -> str:
        return (
            f": Polígono regular de {self.num_sides} "
            f"lados de longitud {self.side_length}"
        )

    @abstractmethod
    def draw(self):
        pass


# Clase Polígono regular: Triángulo
class Triangle(RegularPolygon):
    def __init__(self, side_length: int):
        super().__init__(3, side_length)

    def __str__(self) -> str:
        return f"Triángulo{super().__str__()}"

    def draw(self) -> None:
        if self._check_side_length():
            for line in range(self.side_length - 1):
                if line == 0:
                    print("*")
                else:
                    internal_spaces = " " * (2 * line - 1)
                    print(f"*{internal_spaces}*")

            print(" ".join(["*"] * self.side_length))


# Clase Polígono regular: Cuadrado
class Square(RegularPolygon):
    def __init__(self, side_length: int):
        super().__init__(4, side_length)

    def __str__(self) -> str:
        return f"Cuadrado{super().__str__()}"

    def draw(self) -> None:
        if self._check_side_length():
            body_length = self.side_length - 2
            horizontal_edge = " ".join(["*"] * self.side_length)
            internal_spaces = " " * (2 * body_length + 1)

            print(horizontal_edge)

            for _ in range(body_length):
                print(f"*{internal_spaces}*")

            print(horizontal_edge)


# Clase Polígono regular: Rombo
class Diamond(RegularPolygon):
    def __init__(self, side_length: int):
        super().__init__(4, side_length)

    def __str__(self) -> str:
        return f"Rombo{super().__str__()}"

    def draw(self) -> None:
        if self._check_side_length():
            total_lines = 2 * self.side_length - 1
            side_length = self.side_length - 1

            for line in range(total_lines):
                leading_spaces = " " * (2 * abs(side_length - line))

                if line in (0, total_lines - 1):
                    print(f"{leading_spaces}*")
                else:
                    internal_spaces = " " * (
                        4 * ((side_length) - abs((side_length) - line)) - 1
                    )
                    print(f"{leading_spaces}*{internal_spaces}*")


# Mostrar características de un polígono regular
def show_polygon(polygon: RegularPolygon):
    print(polygon)
    polygon.draw()
    print()


# Función principal
if __name__ == "__main__":
    # Crear y mostrar varios polígonos regulares
    show_polygon(Triangle(0))
    show_polygon(Square(-1))

    for side in range(2, 10):
        show_polygon(Triangle(side))
        show_polygon(Square(side))
        show_polygon(Diamond(side))
