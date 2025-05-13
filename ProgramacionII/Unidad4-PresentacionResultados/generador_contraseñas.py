"""
Generador de contraseñas aleatorias

Estudiante: Juan Esteban Valdés Rodriguez
Curso: Programación

• La contraseña debe tener una longitud especificada por el usuario
(mínimo 8 caracteres).
• Debe incluir al menos un número, una letra mayúscula, una letra
minúscula y un carácter especial de la siguiente lista: ¿¡?=)(/¨*+-
%&$#!.
• No se permiten datos repetidos en la contraseña.
• La asignación de los datos debe ser completamente aleatoria, es
decir, sin un orden específico.
"""
# Modulos necesarios para generar las contraseñas aleatorias
import random
import array

class Contraseña:
    def __init__(self, longitud, password):
        self.longitud = longitud
        self.caracteres = []

    def longitud_contraseña(self):
        """
        Método para ingresar la longitud de la contraseña 
        minimo 8 caracteres, máximo 128. 
        Me base en un gestor de contraseñas (bitwarden) 
        para definir el tope de caracteres.
        """
        while (True):
            try:
                self.longitud = int(input("Ingresa la longitud de la contraseña (minimo 8): "))
                if self.longitud <8:
                    print("La contraseña debe tener mínimo 8 caracteres")
                elif self.longitud >128:
                    print("No se puede sobrepasar el máximo de caracteres")
                else:
                    return self.longitud
             # Manejo de errores
            except ValueError:
                print("\nSolo se permiten valores númericos intenta nuevamente")
            except KeyboardInterrupt:
                print("\n\nPrograma interrumpido por el usuario\n")
                break
    
    def combinar_caracteres(self):
        # Listas/arreglos para los caracteres de nuestra contraseña
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        caracteres_especiales = ['¿','¡','?','=',')','(', '/', 
                                 '¨', '*', '+', '-', '%', '&'
                                 '*', '$','#','!']

        minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                      'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                      'z']
        
        mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
        
        # Se combinan todos los caracteres de las listas para formar
        # una sola contraseña
        self.caracteres = numeros + caracteres_especiales + minusculas + mayusculas

        # con el modulo random se selecciona al menos un caracter de 
        # forma aleatoria -> método choice()
        digito_aleatorio = random.choice(numeros)
        mayuscula_aleatoria = random.choice(mayusculas)
        minuscula_aleatoria = random.choice(minusculas)
        simbolo_aleatorio = random.choice(caracteres_especiales)










@staticmethod
def main():
    """
    Método principal, lógica de ejecución del programa
    """
    ContraseñaSegura = Contraseña(None, None)
    ContraseñaSegura.longitud_contraseña()

if __name__ == "__main__":
    print("Testing...")
    main()


