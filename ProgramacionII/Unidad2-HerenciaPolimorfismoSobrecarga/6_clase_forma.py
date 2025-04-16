"""
EJercicio 6:
Define una clase Forma con métodos area() y perimetro() como 0.
Crea subclases Triangulo y Pentagono, cada una con su propia
implementación de estos métodos. Añade atributos encapsulados
para el número de lados y la longitud de cada lado.
"""


class Forma():
    def __init__(self):
        pass

    def area(self):
        return 0

    def perimetro(self):
        return 0


class Triangulo(Forma):
    def __init__(self, numero_lados, longitud):
        self.__numero_lados = numero_lados
        self.__longitud = longitud

    def area(self, base, altura):
        return base * altura

    def perimetro(self):
        return self.__numero_lados * self.__longitud
