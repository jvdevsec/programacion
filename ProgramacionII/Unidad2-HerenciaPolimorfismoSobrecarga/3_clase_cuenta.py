"""
Ejercicio 3:
Crea una clase Cuenta con atributos encapsulados __saldo y
métodos depositar() y retirar(). Crea una subclase CuentaAhorro
que añada un interés y un método aplicar_interes() que modifique
el saldo
"""


class Cuenta():
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, monto: float):
        self.__saldo += monto
        return self.__saldo

    def retirar(self, monto: float):
        self.__saldo -= monto
        return self.__saldo

    def mostrar_saldo(self):
        print(f"Saldo disponible: {self.__saldo}")


class CuentaAhorro(Cuenta):
    def __init__(self, interes):
        # super().__init__(__)
        self.interes = interes

    # def aplicar_interes(self, interes):
        # print("...")


if __name__ == "__main__":
    print("--Cuenta de Banco--")
    cuenta1 = CuentaAhorro(0)
    cuenta1.depositar(50)
