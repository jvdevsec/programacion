"""
Ejercicio 2:
Crea una clase Vehiculo con métodos arrancar() y parar(). Luego,
crea subclases Coche y Moto con un método específico para cada
una (tocar_claxon() en Coche y hacer_wheelie() en Moto), y
prueba sus métodos únicos.
"""


class Vehiculo:  # Clase Padre o Superclase
    def __init__(self):
        """
        Uso la palabra reservada 'pass' para definir una clase
        sin los atributos implementados para el desarrollo del
        ejercico
        """
        pass

    # Metodos de instancia
    def arrancar(self):
        print("El vehiculo arranca...")

    def parar(self):
        print("El vehiculo se detiene")


class Coche(Vehiculo):
    def __init__(self):
        pass

    def tocar_claxon(self):
        print("BEEEP BEEP!")


class Moto(Vehiculo):
    def __init__(self):
        pass

    def hacer_wheelie(self):
        print("!La moto se levanta en la llanta trasera¡")


if __name__ == "__main__":
    """
    Aqui tenemos un buen ejemplo de herencia, es mejor escribir
    el codigo una vez y reutilizarlo:
    """
    # Instancia de Coche
    print("--Coche--")
    volkswagen = Coche()
    volkswagen.arrancar()
    volkswagen.tocar_claxon()
    print("\n--Moto--")
    # Instancia de Moto
    kawasaki = Moto()
    kawasaki.arrancar()
    kawasaki.hacer_wheelie()
