"""
Añadir un método en la clase Persona llamado presentarse, que
imprima una presentación usando el nombre y edad de la persona.
"""
import sys # Importacion del modulo sys - Se va a hacer uso de la funcion .exit() para interrumpir el programa

class Persona:
    def _init_(self, nombre, edad): # Constructor 
        self.nombre = nombre
        self.edad = edad
    # Metodo para la entrada de datos y personalizar el mensaje de presentacion
    def ingresar_datos(self):
        # Validacion de entrada -> nombre
        while(True):
            try:
                self.nombre = input("Ingrese el nombre: ")
                # Se verifica que no se ingresen caracteres vacios con el metodo strip(). Este borra espacios en blanco
                if self.nombre.strip() == "": 
                    print("\nError: El nombre no puede ser vacio, intente nuevamente\n")  
                else: 
                    break
            except EOFError: # Manejo del error EOF(End of File) cuando se interrumpe el programa con ctrl+D en la consola
                print("\n\nSaliste del programa satisfactoriamente")
                sys.exit() # La funcion sys.exit() termina la ejecucion del programa
         # Validacion de entrada -> edad
        while(True):
            # Para manejar el error de ingresar un dato no valido se usa un try-except
            try: 
                self.edad = int(input("Ingrese la edad: "))
                if self.edad > 0: # Verifica que la edad sea un numero positivo
                    break
                else:
                    print("\nError: la edad debe ser un numero positivo, intente nuevamente\n")
            except ValueError: # El programa no se va a detener sino que imprime un mensaje de error
                print("\nError: Solo se permiten datos numericos, intente nuevamente\n")
            except EOFError: 
                print("\n\nSaliste del programa satisfactoriamente")
                sys.exit()
    
    def presentarse(self):
        print(f"\nHola, mi nombre es {self.nombre} y tengo {self.edad} años (°▽°)/")

# Salidas - Llamada a las funciones
persona = Persona()
persona.ingresar_datos()
persona.presentarse()