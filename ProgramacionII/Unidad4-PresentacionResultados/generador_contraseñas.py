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

class GeneradorContraseña():
    def __init__(self, longitud, password):
        self.longitud = longitud
        self.password = password

if __name__ == "__main__":
    print("Testing...")


