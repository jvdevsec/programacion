/*
Nombre: Juan Esteban Valdés Rodriguez
Grupo: 213022A_1704
Programa: Ingeniería de Sistemas
Código Fuente: Autoría Propia

Problema #5 Funciones y Procedimientos:
En el curso de matemáticas se requiere un programa que calcule el
área y el perímetro de un rectángulo así:
• Se requiere captura por teclado de la base y la altura del rectángulo
(siendo la base y la altura números flotantes).
• Se debe implementar una función sin retorno que reciba como
parámetros la base y la altura, calcule e imprima en consola el valor
del área y del perímetro del rectángulo.
NOTA: El área de un rectángulo es base * altura. Es decir, base por
altura.
NOTA: El diámetro de un rectángulo es (base *2) + (altura * 2). Es
decir, base por dos sumas a altura por dos
*/
using System;
namespace FuncionesyProcedimientos2
{
    public class Program
    {
        public static void Main(string[] args) // Metodo principal
        {
            // Llamada a las funciones
            BannerAscii();     
            float baseRectangulo = EntradaDeDatos("Ingresa la base: ");
            float alturaRectangulo = EntradaDeDatos("Ahora la altura:  ");
            operaciones(baseRectangulo, alturaRectangulo);
        }

        static void BannerAscii() // Muestra en pantalla el banner decorativo
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine(@"
            $$$$$$$$\                            $$\                                         
            $$  _____|                           \__|                                        
            $$ |   $$\   $$\ $$$$$$$\   $$$$$$$\ $$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$$\ 
            $$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  _____|
            $$  __|$$ |  $$ |$$ |  $$ |$$ /      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  
            $$ |   $$ |  $$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |$$ |  $$ |$$   ____| \____$$\ 
            $$ |   \$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\ $$$$$$$  |
            \__|    \______/ \__|  \__| \_______|\__| \______/ \__|  \__| \_______|\_______/                                            
            ");
            Console.Write("== Calculadora Área y Perimetro de un rectangulo ==\n");
            Console.ResetColor();
        }
        // Para que el código sea más conciso uso esta función 
        // para pedir los valores de base y altura. La llamo
        // dos veces en el metodo principal
        public static float EntradaDeDatos(string mensajePrompt) // paso el parametro del mensaje predefinido
        {
            while(true) // Este bucle es para validar las entradas del usuario
            {
                Console.Write(mensajePrompt); 
                string? ingresoNumero = Console.ReadLine();
                if(!float.TryParse(ingresoNumero, out float numeroIngresado)) // La conversión al tipo de dato float. El operador '!' es una negación lógica
                {
                    // La conversión falla al ingresarse caracteres especiales como '/!"#$$%' 
                    Console.Write(mensajePrompt);
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Error - Solo se permiten valores númericos");
                    Console.ResetColor();
                    continue;
                }
                else if(numeroIngresado < 1 || numeroIngresado > float.MaxValue) // Este condicional define el rango de valores permitidos
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"Error - El numero debe ser positivo, diferente de 0 y no exceder {float.MaxValue} (valor máximo)");
                    Console.ResetColor();
                    continue;
                }
                return numeroIngresado; // Retorna el número ingresado
            }
        }
        public static void operaciones(float baseRectangulo, float alturaRectangulo) // Nota: las funciones void no retornan ningun valor
        {
           float areaRectangulo = baseRectangulo * alturaRectangulo; // base x altura 
           float diametroRectangulo = (baseRectangulo*2) + (alturaRectangulo * 2);
           Console.ForegroundColor = ConsoleColor.Green;
           Console.WriteLine($"El area del rectangulo es {areaRectangulo} ");
           Console.WriteLine($"El diametro del rectangulo es {diametroRectangulo}");
           Console.ResetColor();
        }
    }
}