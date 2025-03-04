"""
Crear una clase Calculadora con métodos sumar, restar,
multiplicar, y un método estático convertir_a_entero que convierta
números de coma flotante a enteros
"""
from math import trunc, ceil # modulo math y funciones trunc() y ceil()
from sys import exit # Para salir del programa 

class Calculadora:
    def __init__(self): # Constructor- los atributos sin valores asignados, van a ingresarse por el usuario
        self.primer_numero = None 
        self.segundo_numero = None
    # Metodo para el ingreso de valores
    def ingreso_de_datos(self):
        while (True):
            # Bloque try-except para el manejo de errores
            try:
                self.primer_numero = int(input("Ingresa el primer numero: "))
                self.segundo_numero = int(input("Ingresa el segundo numero: "))
                break
            except ValueError: # Validacion de entradas
                print("\nError: Solo se permiten valores numericos. Intente nuevamente ")
            except EOFError: # Cuando se sale del programa con el atajo de tecaldo (ctrl + c / ctrl + d)
                print("\nEjecucion cancelada (×_×)\n")
                exit()
    # Metodos para el calculo de las operaciones           
    def sumar(self):
        print(f"\nLa suma de ambos numeros es {self.primer_numero + self.segundo_numero}\b")
    
    def restar(self):
        print(f"\nLa resta de ambos numeros es {self.primer_numero - self.segundo_numero}\b")

    def multiplicar(self):
        print(f"\nLa multiplicacion de ambos numeros es {self.primer_numero * self.segundo_numero}\b")

    # Metodo estatico - no es necesario pasar el parametro self ni tampoco crear una instancia de la clase
    @staticmethod # Decorador para definir un metodo como metodo estatico
    def convertir_a_entero():
        primer_numero = float(input("Ingresa el numero decimal: "))
        numero_convertido = trunc(primer_numero) # Descartando la parte decimal
        numero_truncado = ceil(primer_numero) # Redondeando al entero mas cercano
        return print(f"Convertido a entero: {numero_convertido}\nTruncado al entero mas cercano: {numero_truncado}")
    # Este metodo imprime el menu y maneja la seleccion de opciones
    def menu(self): 
        while(True):
            # Menu
            print("\n--Calculadora--\nSeleccione una opcion(1-5)\n1-Sumar\n2-Restar\n3-Multiplicar\n4-Convertir decimal a entero\n5-SALIR")
            # Bloque try-catch para manejo de errores cuando se interrumpe la ejecucion del programa 
            try:
                opcion_seleccionada = (input("> ")) # Se almacena el valor ingresado
                 # Dependiendo del valor ingresado se llama al metodo
                match opcion_seleccionada: # match-case para manejar multiples condiciones. 
                    case "1":
                        calculadora.ingreso_de_datos()
                        calculadora.sumar()
                    case "2":
                        calculadora.ingreso_de_datos()
                        calculadora.restar()
                    case "3":
                        calculadora.ingreso_de_datos()
                        calculadora.multiplicar()
                    case "4":   
                        calculadora.convertir_a_entero()
                    case "5":
                        print("\nSaliste del programa satisfactoriamente (^-^)\n")
                        break
                    case _:
                        print("\nValor no permitido, ingresa numeros de 1-5")
            except EOFError:
                print("\nEjecucion cancelada (×_×)\n") # ctrl+d
                exit() # sale del programa
            except KeyboardInterrupt: # ctrl+c
                print("\n\nEjecucion cancelada (×_×)\n")
                exit() 
# Instancia de la clase          
calculadora = Calculadora()
calculadora.menu()
