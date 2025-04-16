"""
Ejercicio 5:
Define una clase Electrodomestico con métodos encender() y
apagar(). Crea subclases Lavadora y Microondas con métodos
específicos (iniciar_ciclo() para Lavadora y calentar() para
Microondas).
"""

# Superclase o clase padre


class Electrodomestico:
    def __init__(self):
        pass

    def encender(self):
        print("Maquina encendida")

    def apagar(self):
        print("Maquina apagada")

# Subclases o clases hijas


class Lavadora(Electrodomestico):
    def __init__(self):
        pass

    def iniciar_ciclo(self):
        print("La lavadora empezo el ciclo de lavado...")


class Microondas(Electrodomestico):
    def __init__(self):
        pass

    def calentar(self):
        print("EL microondas calienta la comida a 80° Celsius...")


if __name__ == "__main__":
    electrodomestico1 = Lavadora()
    electrodomestico1.iniciar_ciclo()
