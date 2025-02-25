
"""
Implementa una clase Persona con los atributos nombre, edad, y
ciudad. Incluye un método saludar que imprima un saludo como:
“Hola, me llamo [nombre], tengo [edad] años y vivo en [ciudad]”.
Crea dos o tres instancias de Persona y llama al método saludar
para cada una.
"""
class Persona:
    def __init__(self, nombre, edad, ciudad): # Constructor 
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def saludar(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}")

# Uso de la clase 'Persona' - instancias pasando argumentos 
persona1= Persona("Camilo", 21, "Pereira")
persona2= Persona("Steven", 19, "Palmira")
persona3= Persona("Isabella", 24, "Tunja")
# Llamado a los metodos
persona1.saludar()
persona2.saludar()
persona3.saludar() 
