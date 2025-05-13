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
import secrets 
import random

class ContraseñaSegura:
    def __init__(self, longitud, password):
        self.longitud = longitud
        self.password = password

def longitud_contraseña():
    """
    Método para ingresar la longitud de la contraseña 
    minimo 8 caracteres, máximo 128. 
    Me base en un gestor de contraseñas (bitwarden) 
    para definir el tope de caracteres.
    """
    while (True):
        try:
            longitud = int(input("Ingresa la longitud de la contraseña (minimo 8): "))
            if longitud <8:
                print("La contraseña debe tener mínimo 8 caracteres")
            elif longitud >128:
                print("No se puede sobrepasar el máximo de caracteres")
            else:
                return longitud
        # Manejo de errores
        except ValueError:
            print("\nSolo se permiten valores númericos intenta nuevamente")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario\n")
            break


@staticmethod
def main():
    """
    Método principal, lógica de ejecución del programa
    """
    longitud_contraseña()

if __name__ == "__main__":
    print("Testing...")
    main()


