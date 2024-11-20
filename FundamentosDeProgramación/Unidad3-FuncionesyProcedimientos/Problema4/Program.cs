/*
Nombre: Juan Esteban Valdés Rodriguez
Grupo: 213022A_1704
Programa: Ingeniería de Sistemas
Código Fuente: Autoría Propia

Problema #4 Funciones y Procedimientos:
En el curso de matemáticas se requiere un programa que calcule el
área y el perímetro de un círculo así:

• Se requiere captura por teclado del radio (siendo el radio un
número flotante).
• Se debe implementar una función que reciba como parámetro
el radio ingresado y retorne el valor del diámetro.
• calcular e imprimir en consola el valor del área y del perímetro
del círculo.
*/
using System;
namespace FuncionesyProcedimientos1
{
    public class Program
    {
        // Tuve en cuenta el ambito de la variables o 'scope'. Como voy a acceder a las variables 
        // en otras funciones la declaro como un campo de la clase:
        private static float radioCirculo;
        private static double numeroPi = 3.1416;
        public static void Main(string[] args) // Método principal
        {
            // Llamado a las funciones
            mostrarBannerAscii();
            entradaPorTeclado();
            Console.WriteLine($"El diametro es {calcularDiametro(radioCirculo)}");
            Console.WriteLine($"El área es {calcularArea(radioCirculo, numeroPi)}");
            Console.WriteLine($"El perimetro es {calcularPerimetro(radioCirculo, numeroPi)}");
        }
         static void mostrarBannerAscii() // La funciónmuestra en pantalla el banner decorativo 
        {
            Console.Title = "Problema #4";
            Console.ForegroundColor = ConsoleColor.Green;
            Console.Write(@"
                                   __               __        __ __        __     
                            __    /\ \             /\ \      _\ \\ \__   /'__`\   
             __  __    ___ /\_\   \_\ \     __     \_\ \    /\__  _  _\ /\_\L\ \  
            /\ \/\ \ /' _ `\/\ \  /'_` \  /'__`\   /'_` \   \/_L\ \\ \L_\/_/_\_<_ 
            \ \ \_\ \/\ \/\ \ \ \/\ \L\ \/\ \L\.\_/\ \L\ \    /\_   _  _\ /\ \L\ \
             \ \____/\ \_\ \_\ \_\ \___,_\ \__/.\_\ \___,_\   \/_/\_\\_\/ \ \____/
              \/___/  \/_/\/_/\/_/\/__,_ /\/__/\/_/\/__,_ /      \/_//_/   \/___/ 
              
              ");
            Console.Write("\nCalculadora Diametro, Area y Perimetro de un Circulo\n");
            Console.WriteLine("");
            Console.ResetColor();
        }
        public static void entradaPorTeclado() // Este procedimiento es para el valor 
        {
            while(true) // Bucle para validar las entradas del usuario
            {
                Console.Write("Ingresa el radio del circulo: ");
                string? numeroIngresado = Console.ReadLine();
                if(!float.TryParse(numeroIngresado, out radioCirculo)) // Convierte el string a float/punto flotante
                {
                    // el operador '!' significa negación. Si la conversión falla se muestra el mensaje de error
                    Console.ForegroundColor = ConsoleColor.Yellow; 
                    Console.WriteLine("Advertencia - No se se admiten carácteres especiales");
                    Console.ResetColor();
                }
                else if(radioCirculo < 1 || radioCirculo > 999999999999999) // el rango de numeros que se puede ingresar
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("¡ERROR! - El valor ingresado para el radio no es válido");
                    Console.ResetColor();
                }
                else
                {
                    break; // Salir del bucle
                }
            }   
        }
        public static float calcularDiametro(float radioCirculo) // La función recibe el parametro 
        {
            return radioCirculo * 2; // el diametro de un circulo es el doble del radio (multiplicado por 2)
        }
        public static float calcularArea(float radioCirculo, double numeroPi)
        {
            // Conversión de tipo. Para que el compilador no arroje un error
            // coloque el tipo de dato deseado entre parentesis antes del valor que quiero convertir a float
            return (float)(numeroPi * Math.Pow(radioCirculo, 2)); // πr^2 - formula para calcular el área
        }
        public static float calcularPerimetro(float radioCirculo, double numeroPi)
        {
            return (float)(2* numeroPi * radioCirculo); // la formula del perimetro (circunferencia) es 2πr
        }
    }         
}