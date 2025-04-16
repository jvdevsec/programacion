"""
Ejercicio 5:
Define una clase Electrodomestico con métodos encender() y
apagar(). Crea subclases Lavadora y Microondas con métodos
específicos (iniciar_ciclo() para Lavadora y calentar() para
Microondas).
"""


class Electrodomestico:  # Superclase o clase padre

    def __init__(self):
        pass

    def encender(self):
        print("Maquina encendida")

    def apagar(self):
        print("Maquina apagada")


class Lavadora(Electrodomestico):  # Subclases o clases hijas
    def __init__(self):
        pass

    def iniciar_ciclo(self):
        print("La lavadora empezo el ciclo de lavado...")


class Microondas(Electrodomestico):
    def __init__(self):
        pass

    def calentar(self):
        print("EL microondas calienta la comida a 80° Celsius...")


# Ejecucion del programa
if __name__ == "__main__":
    print("--ELectrodomesticos--")
    electrodomestico1 = Lavadora()
    electrodomestico1.iniciar_ciclo()
    electrodomestico1.apagar()

    electrodomestico2 = Microondas()
    electrodomestico2.encender()  # Heredo el metodo de la clase padre
    electrodomestico2.calentar()
