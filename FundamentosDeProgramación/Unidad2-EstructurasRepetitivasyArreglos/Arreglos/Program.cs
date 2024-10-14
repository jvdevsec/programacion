/*
Nombre: Juan Esteban Valdés Rodriguez
Grupo: 213022A_1704
Programa: Ingeniería de Sistemas
Código Fuente: Autoría Propia

Problema #3 Areglos Bidimensionales:
Se solicita la creación de una aplicación que elabore una matriz de 4 × 4 
en la cual se almacenarán números entre el 3 y el 6 ambos incluidos que se deben capturar por teclado. 

Una vez obtenida la información se debe establecer cuantas veces se repiten cada uno de los números del 3 al 6 
y hallar la potencia de ellos de acuerdo con las veces que se repita. 

Se debe mostrar por pantalla la matriz generada y las potencias de los 4 números.
*/
using System;

namespace ArreglosBidimiensonales
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.ForegroundColor=ConsoleColor.Magenta;
            Console.WriteLine(@"
            
             __  __       _        _         ____  ____  
            |  \/  | __ _| |_ _ __(_)____   |___ \|  _ \ 
            | |\/| |/ _` | __| '__| |_  /     __) | | | |
            | |  | | (_| | |_| |  | |/ /     / __/| |_| |
            |_|  |_|\__,_|\__|_|  |_/___|   |_____|____/ 
            ");
            Console.ResetColor();
            // Matriz 4x4
            int [,] numeros = new int[4,4];
            Console.WriteLine("Ingresa los numeros para la matriz");
            // Bucles anidados para ingresar los 
            for (int x = 0; x < numeros.GetLength(0); x++) // E
            {
                for (int y = 0; y < numeros.GetLength(1); y++) 
                {
                    while(true)
                    {
                        Console.WriteLine($"Ingrese un valor para la fila {x+1} y la columna {y+1}: ");
                        string? entradaUsuario = Console.ReadLine();
                        if (int.TryParse(entradaUsuario, out int numero) && numero >= 3 && numero <= 6) // Validar la entrada del usuario - numeros entre 3 y 6, tampoco se permiten datos de tipo string
                        {
                            numeros[x,y] = numero;
                            break;
                        }
                        else
                        {
                            Console.ForegroundColor=ConsoleColor.Red;
                            Console.WriteLine("Error - Se debe ingresar un valor entre 3 y 6. Tampoco se permiten caracteres ni cadenas de texto");
                            Console.ResetColor();
                        }
                    }
                }
            }
            Console.WriteLine();
            Console.WriteLine("Matriz 4x4:");
            // Mostrar en la consola el arreglo - Se usan bucles for anidados para recorrer los elementos del arreglo bidimensional
            for(int x = 0; x < numeros.GetLength(0); x++)
            {
                for(int y = 0; y < numeros.GetLength(1); y++)
                {
                    Console.ForegroundColor=ConsoleColor.DarkGreen;
                    Console.Write(numeros[x,y] + " ");
                    Console.ResetColor();
                }
            Console.WriteLine(); // Salto de linea
            }
        }
    }
}
