"""
Ejercicio 4:
Crea una clase Libro con atributos privados __titulo, __autor, y
__precio. Usa métodos get_precio() y set_precio() para acceder al
precio de manera controlada. Crea una subclase LibroDigital que
permita aplicar descuentos en el precio.
"""


class Libro():  # Clase padre
    def __init__(self, titulo, autor, precio):
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = precio

    def get_precio(self):
        print(f"Precio del libro: ${self.__precio}")
        return self.__precio
