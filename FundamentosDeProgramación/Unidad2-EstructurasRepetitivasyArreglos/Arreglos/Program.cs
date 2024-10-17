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
            // Bucles anidados para ingresar los elementos al arreglo bidimensional
            for (int x = 0; x < numeros.GetLength(0); x++) // Metodo Get.Length - Especifica la dimensión del arreglo, toma un valor entero
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
                            Console.WriteLine("Error - Se debe ingresar un valor entre 3 y 6. Tampoco se permiten caracteres ni cadenas de texto"); // Mensaje de error 
                            Console.ResetColor();
                        }
                    }
                }
            }
            Console.WriteLine(); // Salto de línea
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
            // conteo de números repetidos
            int[] conteo = new int [16]; // arreglo para almacenar los números ingresados - 16 números en total, lo indices son 0,1,2,3,4,5,6... hasta 15

            foreach(int numeroRepetido in numeros) 
            {
                conteo[numeroRepetido]++; // incremento por cada número repetido
            }
            // Bucle for - para iterar sobre los numeros ingresados en el arreglo 'conteo[]'
            Console.WriteLine($"\nNúmeros repetidos");
            for(int x = 0; x <conteo.GetLength(0); x++) 
            {
                if(conteo[x] > 1)
                {
                    Console.WriteLine($"El número '{x}' se repite {conteo[x]} veces");
                    Console.WriteLine($"De acuerdo al número de veces que se repite '{x}' su potencia es {Math.Pow(x, conteo[x])}\n"); // Método  Math.Pow() - para calcular la potencia de un número, 'x' y 'conteo[]' como parametros
                }
            }
            
        }
    }
}
