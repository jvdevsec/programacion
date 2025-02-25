"""
Crear una clase Calculadora con métodos sumar, restar,
multiplicar, y un método estático convertir_a_entero que convierta
números de coma flotante a enteros
"""
class Calculadora:
    def __init__(self): # Constructor 
        self.primer_numero = 0
        self.segundo_numero = 0
    
    def sumar(self):
        self.primer_numero = int(input("Ingresa el primer numero: "))
        self.segundo_numero = int(input("Ingresa el segundo numero: "))
        print(f"\nLa suma de ambos numeros es {self.primer_numero + self.segundo_numero}\b")
    
    def restar(self):
        self.primer_numero = int(input("Ingresa el primer numero: "))
        self.segundo_numero = int(input("Ingresa el segundo numero: "))
        print(f"\nLa resta de ambos numeros es {self.primer_numero - self.segundo_numero}\b")

    def multiplicar(self):
        self.primer_numero = int(input("Ingresa el primer numero: "))
        self.segundo_numero = int(input("Ingresa el segundo numero: "))
        print(f"\nLa multiplicacion de ambos numeros es {self.primer_numero * self.segundo_numero}\b")
    
    def ingresar_numeros(self): # Este metodo es para el ingreso de datos
        while(True):
            print("\n--Calculadora--\nSeleccione una opcion\n1-Sumar\n2-Restar\n3-Multiplicar\n5)Convertir decimal a entero") # Menu
            opcion_seleccionada = (input("> ")) # La variable almacena el valor ingresado
            # Dependiendo del valor ingresado se llama al metodo
            match opcion_seleccionada: # match-case - util para manejar multiples condiciones y legible. Similar a switch-case 
                case "1":
                    calculadora.sumar()
                case "2":
                    calculadora.restar()
                case "3":
                    calculadora.multiplicar()
                case "4":
                    print("No implementado todavia!") # To Do: Agregar la formula de conversion de float a entero
                case _:
                    print("Valor no permitido, ingresa numeros de 1-5")

                
calculadora = Calculadora()
calculadora.ingresar_numeros()