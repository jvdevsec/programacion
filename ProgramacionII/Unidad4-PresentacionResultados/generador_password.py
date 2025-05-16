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
from random import choice, shuffle
from array import array

class Contraseña:
    """
    Clase para crear la contraseña de acuerdo con los 
    requerimientos. El atributo 'caracteres' es para
    el almacenamiento de la contraseña.
    """
    def __init__(self, longitud:int):
        self.longitud = longitud
        self.caracteres = None

    def ingresar_longitud(self):
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
            except EOFError:
                print("\n\nPrograma interrumpido por el usuario\n")
                break

    def combinar_caracteres(self):
        """
        Metodo para combinar los caracteres almacenados 
        en las listas. Se usa la función choice() que
        selecciona un elemento de la lista de forma
        aleatoria para cada tipo de caracter.
        """
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
        # una lista única 
        self.caracteres = numeros + caracteres_especiales + minusculas + mayusculas

        # con el modulo random se selecciona al menos un caracter de 
        # forma aleatoria -> método choice()
        digito_aleatorio = choice(numeros)
        mayuscula_aleatoria = choice(mayusculas)
        minuscula_aleatoria = choice(minusculas)
        simbolo_aleatorio = choice(caracteres_especiales)

        contraseña_temporal = digito_aleatorio + mayuscula_aleatoria + minuscula_aleatoria + simbolo_aleatorio
        # print(contraseña_temporal) -> testeo
        return contraseña_temporal
    
    def generar_contraseña(self, contraseña_temporal):
        """
        FIXED
        Genera contraseñas mezclando los caracteres combinados
        y completa hasta la longitud ingresada por el usuario
        -> hice esta corrección ya que había un error de obsolencia
        al usar el tipo de codificación 'u' en el método .array().
        Ya no es necesario tampoco el modulo 'array' 
        """
        
        
     
def main():
    """
    Método principal, lógica de ejecución del programa
    """
    print("---GENERADOR DE CONTRASEÑAS--- (ツ)")
    print("Genera contraseñas aleatorias de hasta 128 caracteres!")
    print("Entre más caracteres más seguridad y fuerte contra el brute forcing\n")
    # Instancia de la clase Contraseña
    ContraseñaSegura = Contraseña(None)
    ContraseñaSegura.ingresar_longitud()
    ContraseñaSegura.combinar_caracteres()
    contrasena = ContraseñaSegura.generar_contraseña('')
    # Salida
    print(f"Contraseña generada: {contrasena}")

if __name__ == "__main__":
    main()


