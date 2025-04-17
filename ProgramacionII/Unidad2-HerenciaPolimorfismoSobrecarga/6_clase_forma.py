"""
EJercicio 6:
Define una clase Forma con métodos area() y perimetro() como 0.
Crea subclases Triangulo y Pentagono, cada una con su propia
implementación de estos métodos. Añade atributos encapsulados
para el número de lados y la longitud de cada lado.
"""


class Forma:
    def __init__(self):
        pass

    def area(self):
        return 0

    def perimetro(self):
        return 0


class Triangulo(Forma):
    def __init__(self, longitud_lados, base, altura):
        self.__numero_lados = 3  # Un triingulo siempre tiene 3 lados
        self.__longitud_lados = longitud_lados
        # Se agregaron estos 2 atributos para calcular el area
        self.__base = base
        self.__altura = altura

    def area(self, base, altura):
        return base * altura

    def perimetro(self):
        return self.__numero_lados * self.__longitud


if __name__ == "__main__":
    print("-- Cálculo del Perímetro y Área de Formas --")
