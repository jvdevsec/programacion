"""
Ejercicio 1:
Define una clase Persona con atributos encapsulados __nombre y
__edad. Crea una subclase Trabajador que añada un atributo
__salario. Agrega métodos para obtener y modificar el salario de
 manera segura.

Se usa la nomenclatura PEP 8 para formatear el codigo
- Juan Valdes(ツ)
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
        super().__init__(nombre, edad)  # funcion super()
        self.__salario = salario

    def get_salario(self):  # Metodo getter
        """
        Retorna el valor pasado como argumento en la instancia de la clase
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
                # Se verifica que no se ingresen valores negativo
                if nuevo_salario <= 0:
                    print("Valor no valido, ¡ingresa cantidades mayores a 0!")
                else:
                    self.__salario = nuevo_salario
                    print("\nSalario actualizado\n")
                    return self.__salario
            except ValueError:
                print("\nValor no permitido, intenta nuevamente\n")
            except EOFError:
                print("\nEjecucion terminada... x_x\n")
                exit()
            except KeyboardInterrupt:
                print("\nEjecucion terminada... x_x\n")
                exit()


# Esta condición simplemente hace una consulta para verificar
# si el archivo que se está ejecutando es el archivo principal
# No es obligatorio, pero es una buena práctica para separar
# la definición de las clases con la lógica de ejecución
if __name__ == "__main__":
    # Aqui se crea la instancia de la subclase trabajador
    # con algunos valores iniciales
    empleado = Trabajador(None, None, 1423500)
    print("\nSALARIO EMPLEADO")
    while (True):
        # Menu para interactuar con el usuario
        print("\nSelecciona una opcion:")
        print("1)Ver salario")
        print("2)Modificar Salario")
        print("3)SALIR")
        # Un bloque try-except para el manejo de errores
        # interrupciones de teclado: ctrl + d / ctrl + c
        try:
            respuesta_usuario = input(">: ")
            # Se validan las entradas del usuario
            if respuesta_usuario == "1":
                print(f"Salario del empleado: ${empleado.get_salario()} pesos")
            elif respuesta_usuario == "2":
                empleado.set_salario()
            elif respuesta_usuario == "3":
                print("\nSaliste del programa...")
                break
            else:
                (print("\nOpcion invalida. Selecciona 1, 2 o 3 (￣︿￣)\n"))
        except EOFError:
            print("\nEjecucion terminada... x_x\n")
            exit()
        except KeyboardInterrupt:
            print("\nEjecucion terminada.. x_x\n")
            exit()
