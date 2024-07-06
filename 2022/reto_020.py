"""
    RETO #020: CONVERSOR TIEMPO

    Crea una función que reciba días, horas, minutos y segundos (como enteros)
    y retorne su resultado en milisegundos.
"""

# Clase para definir lapsos de tiempo
class TimeLapse:
    # Constructor
    def __init__(self, days=0, hours=0, minutes=0, seconds=0):
        self.days    = days
        self.hours   = hours
        self.minutes = minutes
        self.seconds = seconds

    # Convertir a texto (sencillo)
    def __str__(self):
        return ("TimeLapse: "
            f"{self.days} días, {self.hours} horas, "
            f"{self.minutes} minutos, {self.seconds} segundos"
        )

    # Convertir a texto (con formato)
    def __format__(self, format_spec):
        return format(self.__str__(), format_spec)

    # Convertir a milisegundos
    def convert_to_millisecs(self) -> int:
        millisecs  = self.seconds
        millisecs += self.minutes * 60
        millisecs += self.hours   * 60 * 60
        millisecs += self.days    * 24 * 60 * 60
        millisecs *= 1000

        return millisecs


# Formatear número con separados de miles
def thousand_sep(n) -> str:
    return format(n, ',').replace(',', '.')


# Función principal
if __name__ == "__main__":
    timelapses = [
        (0, 0, 0, 0),
        (0, 0, 0, 1),
        (0, 0, 2, 0),
        (0, 3, 0, 0),
        (4, 0, 0, 0),
        (8, 7, 6, 5),
        (2, 5, -45, 10),
        (2000000000, 5, 45, 10)
    ]

    for timetuple in timelapses:
        timelapse = TimeLapse(*timetuple)
        print(
            f"{timelapse:<60} -> "
            f"{thousand_sep(timelapse.convert_to_millisecs()):>23} milisegundos"
        )
