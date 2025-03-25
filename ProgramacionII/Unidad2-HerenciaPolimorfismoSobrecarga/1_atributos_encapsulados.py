"""
Ejercicio 1:
Define una clase Persona con atributos encapsulados __nombre y
__edad. Crea una subclase Trabajador que añada un atributo
__salario. Agrega métodos para obtener y modificar el salario de
 manera segura.

Empezare a usar la nomenclatura PEP 8 para formatear el codigo

(ツ)
"""


class Persona:  # Se inicializa la clase Persona
    def __init__(self, nombre, edad):
        """
        Al usar doble '__'python interpreta los atributos como
        privados, solo se podran modificar dentro de la propia clase
        """
        self.__nombre = nombre
        self.__edad = edad


class Trabajador(Persona):  # Subclase Trabajador
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.__salario = salario

    def get_salario(self):  # Metodo getter
        """
        Retorna el valor pasado como parametro en la instancia de la clase
        (cuando creamos el objeto)
        """
        return self.__salario

    def set_salario(self):  # Metodo setter
        """
        Este metodo lee la entrada del usuario para modificar el salario
        es decir que nos permite manipular este dato
        """
        while (True):
            try:
                nuevo_salario = int(
                    input("Ingresa el nuevo salario para el empleado: "))
                self.__salario = nuevo_salario
                print("\nSalario actualizado\n")
                return
            except ValueError:
                print("Valor no permitido, intenta nuevamente")


if __name__ == "__main__":
    # Aqui se crea la instancia de la subclase trabajador
    # con algunos valores iniciales
    empleado = Trabajador("J", 30, 1423500)
    print("\nSALARIO EMPLEADO")
    while (True):
        print("\nSelecciona una opcion:")
        print("1)Ver salario")
        print("2)Modificar Salario")
        print("3)SALIR")
        try:
            respuesta_usuario = input(">: ")
            if respuesta_usuario == "1":
                print(f"Salario del empleado: ${empleado.get_salario()} pesos")
            elif respuesta_usuario == "2":
                empleado.set_salario()
            else:
                print("\nSaliste del programa...")
                exit()
        except EOFError:
            print("\nEjecucion terminada, saliendo del programa...\n")
            exit()
