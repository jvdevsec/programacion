"""
Ejercicio 3:
Crea una clase Cuenta con atributos encapsulados __saldo y
métodos depositar() y retirar(). Crea una subclase CuentaAhorro
que añada un interés y un método aplicar_interes() que modifique
el saldo
"""


class Cuenta():  # Clase padre
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, monto: int):
        """
        Este metodo suma el monto al saldo
        """
        self.__saldo += monto
        return self.__saldo

    def retirar(self, monto: int):
        self.__saldo -= monto
        print(f"Se han retirado {monto}")
        return self.__saldo

    def mostrar_saldo(self):
        print(f"Saldo disponible: {self.__saldo}")


class CuentaAhorro(Cuenta):  # Subclase
    def __init__(self, saldo, interes):
        super().__init__(saldo)
        self.interes = interes

    def aplicar_interes(self):
        """
        Accede al atributo privado de la clase padre
        'self.__saldo'
        """
        calculo_interes = self._Cuenta__saldo * self.interes
        return calculo_interes


if __name__ == "__main__":
    print("--Cuenta de Banco--")
    cuenta1 = CuentaAhorro(saldo=1080900, interes=0.06)
    cuenta1.depositar(50)
    cuenta1.mostrar_saldo()
    # Retiro del valor
    cuenta1.retirar(300000)

    cuenta1.aplicar_interes()
    print(f"Saldo con interes del 6%: {cuenta1.mostrar_saldo()}")
