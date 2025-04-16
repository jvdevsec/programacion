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

    # Los metodos para acceder al atributo .__precio
    def get_precio(self):
        return self.__precio

    def set_precio(self, valor):
        self.__precio = valor
        return self.__precio


class LibroDigital(Libro):
    def __init__(self, titulo, autor, precio):
        super().__init__(titulo, autor, precio)

    def aplicar_descuento(self, valor_descuento):
        """
        En este metodo por medio del bucle y los condicionales se verifica
        la respuesta del usuario para validar si se trata de un libro fisico
        o digital. A partir de esto se aplica el descuento del 25%.

        El bloque try-catch maneja los errores al interrumpir la ejecucion
        del programa
        """
        while True:
            try:
                # el metodo strip() elimina los espacios en blanco
                # upper() convierte caracteres a mayusculas
                # si se ingresa s/n se cumple la condicion
                respuesta_usuario = input(
                    "¿Es un libro digital?- S/N: ").strip().upper()
                if respuesta_usuario == "S":
                    valor_descuento = self.get_precio() * 0.25
                    total = self.get_precio() - valor_descuento
                    print(f"Precio con descuento del 25%: {int(total)}")
                    return total

                elif respuesta_usuario == "N":
                    print("El descuento no aplica para libros físicos")
                    break

                else:
                    print("Entrada no válida, intenta nuevamente.")
            except KeyboardInterrupt:
                print("\n\nEjecucion terminada x_x")
                exit()
            except EOFError:
                print("\n\nEjercucion terminada x_x")
                exit()


# Aqui empieza la jecucion del programa. Es buena practica usar esta condicion
if __name__ == "__main__":
    libro1 = LibroDigital(None, None, 0)
    libro1.set_precio(55000)
    print("--Libreria--")
    print(f"Precio original del libro ${libro1.get_precio()}")
    libro1.aplicar_descuento(0)
