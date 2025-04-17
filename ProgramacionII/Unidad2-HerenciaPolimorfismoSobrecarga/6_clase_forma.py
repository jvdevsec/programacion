"""
EJercicio 6:
Define una clase Forma con métodos area() y perimetro() como 0.
Crea subclases Triangulo y Pentagono, cada una con su propia
implementación de estos métodos. Añade atributos encapsulados
para el número de lados y la longitud de cada lado.
"""


class Forma:  # Clase padre
    """
    Por simplicidad se declaro la clase como
    vacia (sin atributos).
    """

    def __init__(self):
        pass

    def area(self):
        return 0

    def perimetro(self):
        return 0


class Triangulo(Forma):
    def __init__(self, longitud_lados, base, altura):
        self.__numero_lados = 3
        self.__longitud_lados = longitud_lados
        # Se agregaron estos 2 atributos para calcular el area
        self.__base = base
        self.__altura = altura

    def area(self):
        """
        Metodo para acceder a los atributos encapsulados
        .__base y .__altura y realizar el calculo del area del triangulo.
        """

        return (self.__base * self.__altura) / 2  # Formula para el area

    def perimetro(self):
        """
        Metodo para calcular el perimetro, es la suma de cada lado.
        se puede simplificar multiplicando el numero de lados por
        la longitud.
        """
        # Perimetro -> 3 * longitud
        return self.__numero_lados * self.__longitud_lados


class Pentagono(Forma):
    def __init__(self, longitud_lados, apotema):
        self.__numero_lados = 5
        self.__longitud_lados = longitud_lados
        self.__apotema = apotema  # para calcular el area de poligonos

    def perimetro(self):
        """
        Metodo para el calculo del perimetro con implementacion
        propia de la clase Pentagono.
        """
        # Perimetro -> 5 * longitud
        return self.__numero_lados * self.__longitud_lados


if __name__ == "__main__":
    print("-- Cálculo del Perímetro y Área de Formas --")
