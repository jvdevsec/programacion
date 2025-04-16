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
        print(f"Se han depositado {monto}")
        return self.__saldo

    def retirar(self, monto: int):
        """
        Se valida que no se retire un valor mayor
        """
        if monto > self.__saldo:
            print("No hay fondos suficientes para hacer el retiro (-_-)")
            return self.__saldo
        self.__saldo -= monto
        print(f"Se han retirado {monto}")
        return self.__saldo

    def mostrar_saldo(self):
        print(f"Saldo disponible: {self.__saldo}")
        # Se retorna el saldo para usarlo en otra(s) operacion(es)
        return self.__saldo


class CuentaAhorro(Cuenta):  # Subclase
    def __init__(self, saldo, interes):
        super().__init__(saldo)
        self.interes = interes

    def aplicar_interes(self):
        """
        Accede al atributo privado de la clase padre
        'self.__saldo'
        """
        calculo_interes = int(self._Cuenta__saldo * self.interes)

        # Se invoca al metodo .depositar() para sumar el interes al saldo
        self.depositar(calculo_interes)
        print(f"Total intereses: {calculo_interes}")
        return self._Cuenta__saldo  # Retorna el saldo actualizado


if __name__ == "__main__":
    print("--Cuenta de Banco--")
    cuenta1 = CuentaAhorro(saldo=1080900, interes=0.06)
    # Nota: descomentar la linea de codigo para verificar el metodo
    # .depositar():
    # cuenta1.depositar(100000)
    cuenta1.mostrar_saldo()
    # Retiro del valor
    cuenta1.retirar(300000)
    print("")
    cuenta1.mostrar_saldo()  # Se llama nuevamente al metodo para ver el saldo

    # Se declara una variable para llamar al metodo
    saldo_con_interes = cuenta1.aplicar_interes()
    print(f"Saldo con interes del 6%: {(saldo_con_interes)}")
