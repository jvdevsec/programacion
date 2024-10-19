/*
Nombre: Juan Esteban Valdés Rodriguez
Grupo: 213022A_1704
Programa: Ingeniería de Sistemas
Código Fuente: Autoría Propia

Problema #3 Estructuras repetitivas:
Capturar por teclado un número entero mayor que 0 y menor que 5000, se debe establecer en qué rango 
se encuentra el número de acuerdo con las siguientes características: rango alto mayor que 4000, 
rango medio entre 2000 y 4000 ambos incluidos y rango bajo menor que 2000. 

El programa debe implementar un ciclo que permita validar que el número sea mayor a 0, en caso de que
el número ingresado sea menor a 0 se debe volver a solicitar al usuario que ingrese el número este 
procedimiento se debe repetir hasta que el número ingresado sea mayor a 0.
*/

using System;
namespace EstructurasRepetitivas
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.ForegroundColor=ConsoleColor.Green;
            Console.Write(@"
             _    _       _     _           _   ___     _____  _  _   
            | |  | |     (_)   | |         | | |__ \   / ____|| || |_ 
            | |  | |_ __  _  __| | __ _  __| |    ) | | |   |_  __  _|
            | |  | | '_ \| |/ _` |/ _` |/ _` |   / /  | |    _| || |_ 
            | |__| | | | | | (_| | (_| | (_| |  / /_  | |___|_  __  _|
             \____/|_| |_|_|\__,_|\__,_|\__,_| |____|  \_____||_||_|                                              
            ");
            Console.WriteLine("");
            Console.ResetColor();
            // Entrada
            while(true)
            {
                Console.WriteLine("Ingresa un número entre 0 y 65535");
                string? numIngresado = Console.ReadLine();
                ushort numero; // ushort es un tipo de dato entero que admite valores desde 0 hasta 65535
                if (!ushort.TryParse(numIngresado, out numero) || numero < 0 && numero > 65535) // Validar la entrada del numero ingresado por el usuario
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.Error.WriteLine("Error - No se admiten caracteres de texto, ni numeros fuera de rango");
                    Console.ResetColor();
                    Console.WriteLine("¿Intentar otra vez (s/n)?"); // Preguntar al usuario si desea ingresar otro valor que sea válido
                    string? respuestaUsuario = Console.ReadLine();
                    if(respuestaUsuario?.ToLower() != "s") 
                    {
                        Console.ForegroundColor=ConsoleColor.Cyan;
                        Console.WriteLine("Saliste del programa satisfactoriamente ( ˘_˘ )");
                        Console.ResetColor();
                        break; // Rompe el bucle 
                    }
                }
                else    // Si se ingresa un valor válido evaluarlo 
                {
                    if(numero > 4000) // Si el numero es mayor a 4000...
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("El numero se encuentra en un rango alto");
                        Console.ResetColor();
                        break; 
                    }
                    else if(numero >= 2000 && numero <= 4000) // Si el numero es mayor o igual a 2000 y el numero es menor o igual a 4000...
                    {
                        Console.ForegroundColor=ConsoleColor.Magenta;
                        Console.WriteLine("El numero se encuentra en un rango medio");
                        Console.ResetColor();
                        break;
                    }
                    else // Si el numero es menor a 2000...
                    {
                        Console.ForegroundColor = ConsoleColor.DarkGray;
                        Console.WriteLine("El número se encuentra en un rango bajo");
                        Console.ResetColor();
                        break;
                    }
                }
                
            }
        }
    }   
}