/*
Nombre: Juan Esteban Valdés Rodriguez
Grupo: 213022A_1704
Programa: Ingeniería de Sistemas
Código Fuente: Autoría Propia

Problema #3:
Un científico loco de la Universidad de la Vida, ha creado una alarma muy especial
y desea que usted le ayude a escribir un programa que diga cuando debe estar
encendida y cuando no. Las condiciones son las siguientes:

Debe estar encendida cuando la presión es de por lo menos 35 libras o cuando la
temperatura excede los 75 C°, pero inferior 95 C°.
En cualquier otro caso, la alarma debe estar apagada.
Se debe recibir por consola cantidad de libras y temperatura en C°, como
resultado debe indicar alarma encendida o alarma apagada. 
*/
using System;
namespace VariablesConstantesEstructurasdeControl
{
    public class Program  // Hay métodos separados para mostrar el banner, ingresar datos y evaluar la alarma
    {
        public void mostrarBanner()
        {
            Console.Title = "Problema #3";
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write(@"                  
                __  ___   __________  ___    ____       ___       ______  __ __ 
               / / / / | / /  _/ __ \/   |  / __ \     <  /      / ____/_/ // /_
              / / / /  |/ // // / / / /| | / / / /     / /      / /   /_  _  __/
             / /_/ / /|  // // /_/ / ___ |/ /_/ /     / /      / /___/_  _  __/ 
             \____/_/ |_/___/_____/_/  |_/_____/     /_/       \____/ /_//_/                                                                                                                                                                                   
            ");
            Console.WriteLine(); // 
            Console.ForegroundColor = ConsoleColor.Gray;
        }
        public void ingresarDatos()
        {
            Console.WriteLine("Ingresa la cantidad de libras por pulgada cuadrada (psi):");
            string? inputLibras = Console.ReadLine(); 
            double presion; // el tipo de dato 'double' tiene más precision que 'float', en el caso de que se ingresen decimales
            if (!double.TryParse(inputLibras, out presion) || presion <= 0) // Convierte la entrada del usuario en un valor 'double' y válida la entrada
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("ERROR - Por favor ingresa un valor válido, no se permiten caracteres, cadenas de texto ni números negativos"); // Si la conversión falla o el valor es inválido se muestra el mensaje de error
                Console.ForegroundColor = ConsoleColor.Gray;
                Environment.Exit(0); // Método para salir del programa cuando se ingresan datos no validos
                
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Presión válida: " + presion + " psi"); // Si la entrada es válida se muestra el mensaje de confirmación
                Console.ForegroundColor = ConsoleColor.Gray;

            }
            Console.WriteLine("Ingresa la temperatura (C°):");
            string? inputTemperatura = Console.ReadLine();
            double  temperaturaEnGradosCelsius;
            if (!double.TryParse(inputTemperatura, out temperaturaEnGradosCelsius)) 
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("ERROR - Por favor ingresa un valor válido, no se permiten caracteres ni cadenas de texto");
                Console.ForegroundColor = ConsoleColor.Gray;
                Environment.Exit(0);
                
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Temperatura válida: " + temperaturaEnGradosCelsius + " C°"); // Si la entrada es válida se muestra el mensaje de confirmación
                Console.ForegroundColor = ConsoleColor.Gray;
                evaluarAlarma(presion, temperaturaEnGradosCelsius);
            }
        }
        public void evaluarAlarma(double presion, double temperaturaEnGradosCelsius)
        {
            if (presion  >= 35 || (temperaturaEnGradosCelsius > 75 && temperaturaEnGradosCelsius < 95))
            {
                Console.ForegroundColor = ConsoleColor.Blue;
                Console.WriteLine("Alarma Encendida");
                Console.ForegroundColor = ConsoleColor.Gray;
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Black;
                Console.WriteLine("Alarma Apagada");
                Console.ForegroundColor = ConsoleColor.Gray;
            }
        }
        public static void Main(string[] args)
        {
            Program program = new Program(); 
            program.mostrarBanner(); // Llamo al metodo mostrarBanner, para imprimir en pantalla el ASCII ART  
            program.ingresarDatos(); // Llamo al metodo ingresarDatos, que se encarga de pedir la cantidad de libras y la temperatura y validar las entradas
        }
    }
}