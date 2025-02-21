"""
Crear una clase Rectangulo con atributos largo y ancho. Agregar
un método que calcule el área.
"""
class Rectangulo: 
    def __init__(self, largo, ancho): # Constructor
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho # Retorna el area 
    
# Uso de la clase Rectangulo y sus metodos
rectangulo = Rectangulo(3.0, 5.0) # Argumentos
area = rectangulo.calcular_area()
print(f"El area del rectangulo es: {area}")

