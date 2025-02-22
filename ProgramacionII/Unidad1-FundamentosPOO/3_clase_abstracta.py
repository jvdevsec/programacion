"""
Crear una clase abstracta Empleado con un método
calcular_salario. Luego crear Gerente y Vendedor, cada uno con su
propia fórmula para calcular el salario
"""

from abc import ABC, abstractmethod # Modulo abc para definir ABCs - Abstract Base Classes

class Empleado(ABC):
    @abstractmethod # Decorador
    def calcular_salario(self):
        pass # Este es un metodo abstracto no hay implementacion

# Subclase Gerente
class Gerente(Empleado): 
    def __init__(self, numero_horas, valor_hora): # Constructor y atributos
        self.numero_horas = numero_horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return  self.valor_hora * self.numero_horas

class Vendedor:
      def __init__(self, numero_horas, valor_hora): # Constructor y atributos
        self.numero_horas = numero_horas
        self.valor_hora = valor_hora
      def calcular_salario(self):
          return  self.valor_hora * self.numero_horas
      
# Instancias de los objetos vendedor y gerente - Simplemente se agregan los argumentos para el calculo de los salarios
vendedor = Vendedor(6189, 230) # valor de la hora y el numero de horas
gerente = Gerente (27083, 230)

print("---- Calculadora Salarios ----")
print(f"Salario total vendedor: ${vendedor.calcular_salario()}")
print(f"Salario total gerente: ${gerente.calcular_salario()}")