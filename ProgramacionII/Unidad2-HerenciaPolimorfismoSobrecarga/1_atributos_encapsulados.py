"""
Ejercicio 1:
Define una clase Persona con atributos encapsulados __nombre y
__edad. Crea una subclase Trabajador que añada un atributo
__salario. Agrega métodos para obtener y modificar el salario de 
manera segura.

Empezare a usar la nomenclatura PEP 8 para formatear el codigo

(ツ)
"""
# Se inicializa la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        """
        Al usar doble '__'python interpreta los atributos como
        "privados", solo se podran modificar dentro de la 
        propia clase
        """
        self.__nombre = nombre 
        self.__edad = edad


# Subclase Trabajador
class Trabajador(Persona):
    def __init__(self, salario, nombre, edad):
        super().__init__(nombre, edad)
        self.__salario = salario

    # Metodo getter 
    def get_salario(salario):
        salario = 1423500
        return salario
        
    @staticmethod
    def main():
        print("\nSALARIO EMPLEADO")
        while(True):
            print(f"Selecciona una opcion:\n1-Ver salario\n2-Modificar Salario")
            try:
                respuesta_usuario = input(">: ")
                if respuesta_usuario == "1":
                    print(f"Salario del empleado: {Trabajador.get_salario(0)}")
                else:
                    print("")
            except EOFError:
                print("\nEjecucion terminada, saliendo del programa...\n")
                break

empleado = Trabajador(0,0,0)
empleado.main()