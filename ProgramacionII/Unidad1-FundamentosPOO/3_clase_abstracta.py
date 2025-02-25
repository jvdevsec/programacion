"""
Crear una clase abstracta Empleado con un método
calcular_salario. Luego crear Gerente y Vendedor, cada uno con su
propia fórmula para calcular el salario
"""

from abc import ABC, abstractmethod # Modulo abc para definir ABCs - Abstract Base Classes

class Empleado(ABC):
    @abstractmethod # Decorador - se usa para definir metodos abstractos
    def calcular_salario(self): # Este metodo tiene que ser implementado en las subclases para que tengan consistencia
        pass 

# Subclase Gerente
class Gerente(Empleado): 
    def __init__(self, numero_horas, valor_hora): # Constructor y atributos
        self.numero_horas = numero_horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return  self.valor_hora * self.numero_horas
# Subclase Vendedor
class Vendedor:
      def __init__(self, numero_horas, valor_hora): #
        self.numero_horas = numero_horas
        self.valor_hora = valor_hora
      def calcular_salario(self):
          return  self.valor_hora * self.numero_horas
      
"""
horas trabajadas a la semana: 46
46/6 = 7.66 horas al dia
7.66 x 30 = 230 horas al mes

valor hora de trabajo 2025: $6.189

Para el caso del gerente investigue el promedio del salario
salario gerente: $5.054.040
5.054.040/230 = 21974 x hora 
"""
# Instancias de los objetos vendedor y gerente - Simplemente se agregan los argumentos para el calculo de los salarios
#Nota: Solo se pueden crear instancias de las clases que implementen los metodos abstractos
vendedor = Vendedor(6189, 230) 
gerente = Gerente (21974, 230)

print("---- Calculadora Salarios ----")
print(f"Salario total vendedor: ${vendedor.calcular_salario()}")
print(f"Salario total gerente: ${gerente.calcular_salario()}")