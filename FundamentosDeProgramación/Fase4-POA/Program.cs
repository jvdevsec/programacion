/*
Nombre: Juan Esteban Valdés Rodriguez
Grupo: 213022A_1704
Programa: Ingeniería de Sistemas
Código Fuente: Autoría Propia

Problema #1:
Una universidad requiere analizar el proceso de matrícula para
el tercer período académico del 2020 de cada uno de los estudiantes. La
universidad consta de cinco (5) programas académicos. Cada programa
académico tiene un número de créditos asociados. El valor de cada crédito
académico es de $200.000.

Se requiere desarrollar una solución básica de programación que permita
matricular un número X de estudiantes. Al finalizar, la solución de
programación debe mostrar los siguientes resultados:
• Cantidad de estudiantes inscritos por programa académico.
• Total, de créditos inscritos en el tercer período académico del 2020.
• Valor total pagado por los estudiantes sin tener en cuenta el descuento.
• Valor total de descuentos aplicados por la universidad a los
estudiantes.
• Valor neto de las inscripciones del primer semestre del 2020.
*/
using System;
namespace POA
{
    public class Program
    {
        public const int VALOR_CREDITO_ACADEMICO = 200000; // valor credito academico
        private static string [,] carrerasYCreditos= 
        {
            {"Ingeniería Sistemas", "20"},
            {"Psicología", "16"},
            {"Economía", "18"},
            {"Comunicación Social", "18"},
            {"Administración de Empresas", "20"} 
        };
        public static void Main(string[] args)
        {
        
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("PROGRAMA DE GESTIÓN MATRICULA ESTUDIANTES");
            Console.ResetColor();
            int totalEstudiantes = SolicitarNumeroEstudiantes(); // invocar a la función
            for (int x = 1;x < totalEstudiantes + 1 ; x++)
            {
                Console.WriteLine($"\nPara el estudiante #{x}");
                DesplegarCarreras();
                int carreraSeleccionada = SeleccionarCarrera();
                ContarEstudiantesInscritos(carreraSeleccionada);
            }
            MostrarTotalEstudiantesPorCarrera();
            MostrarCreditosPeriodoAcademico();
            CalcularDescuentos(VALOR_CREDITO_ACADEMICO);
        }
        static int SolicitarNumeroEstudiantes()
        {
            while(true)
            {
                Console.WriteLine("Ingresa el número total de estudiantes a matricular (max. 100)");
                string? ingresoNumeroEstudiantes = Console.ReadLine();
                if (!int.TryParse(ingresoNumeroEstudiantes, out int totalEstudiantes))
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Error - no se permiten caracteres especiales");
                    Console.ResetColor(); // !"#!"#
                    continue;
                }
                if (totalEstudiantes < 1 || totalEstudiantes > 100)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Error - Valor fuera del rango permitido");
                    Console.ResetColor();
                    continue;
                }
                return totalEstudiantes;
            }
        }
        static void DesplegarCarreras()
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Seleccione una de las carreras disponibles: ");
            Console.ResetColor();
            Console.WriteLine("1-Ingeniería de Sistemas\n2-Psicología\n3-Economía\n4-Comunicación Social\n5-Administración de Empresas");
        }

        static int SeleccionarCarrera()
        {
            while(true)
            {
                Console.Write("> ");
                string? ingresoNumeroCarrera = Console.ReadLine();
                if (!int.TryParse(ingresoNumeroCarrera, out int carreraSeleccionada))
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Error - no se permiten caracteres especiales");
                    Console.ResetColor();
                    continue;
                    
                }
                if (carreraSeleccionada < 1 || carreraSeleccionada > 5)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Opción no válida");
                    Console.ResetColor();
                    continue;
                }
                return carreraSeleccionada;
            }
        }     
        public static int contadorIngenieriaSistemas;
        public static int contadorPsicologia;
        public static int contadorEconomia;
        public static int contadorComunicacionSocial;
        public static int contadorAdministracionEmpresas;
        
        static int ContarEstudiantesInscritos(int carreraSeleccionada)
        {
            return carreraSeleccionada switch
            {
                1 => ++contadorIngenieriaSistemas, // Pre-incremento
                2 => ++contadorPsicologia,
                3 => ++contadorEconomia,
                4 => ++contadorComunicacionSocial,
                5 => ++contadorAdministracionEmpresas,
                _ => 0,
            };
        }
        static void MostrarTotalEstudiantesPorCarrera()
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("\nTotal de estudiantes inscritos por carrera");
            Console.ResetColor();
            /*Console.WriteLine($"Ingeniería de Sistemas: {contadorIngenieriaSistemas} estudiantes");
            Console.WriteLine($"Psicología: {contadorPsicologia} estudiantes");
            Console.WriteLine($"Economía: {contadorEconomia} estudiantes");
            Console.WriteLine($"Comunicación Social: {contadorComunicacionSocial} estudiantes");
            Console.WriteLine($"Administración de Empresas: {contadorAdministracionEmpresas} estudiantes");*/
            for (int x = 0; x < carrerasYCreditos.GetLength(0); x++)
            {
                int[] contadoresEstudiantes = [contadorIngenieriaSistemas, contadorPsicologia, contadorEconomia, contadorComunicacionSocial, contadorAdministracionEmpresas];
    
                string nombreCarrera = carrerasYCreditos[x, 0];
                Console.WriteLine($"{nombreCarrera}: {contadoresEstudiantes[x]}");
            }
        }
        
        static void MostrarCreditosPeriodoAcademico()
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("\nCréditos por Periodo Académico");
            Console.ResetColor();

            for (int x = 0; x < carrerasYCreditos.GetLength(0); x++)
            {
                // Acceder al nombre de la carrera (primera columna)
                string nombreCarrera = carrerasYCreditos[x, 0];
                // Acceder a los créditos (segunda columna)
                string creditos = carrerasYCreditos[x, 1];
                // Mostrar en pantalla la información
                Console.WriteLine($"{nombreCarrera}: {creditos} créditos");
            }
            //int totalCreditos = contadorIngenieriaSistemas * 20 + contadorPsicologia * 16 + contadorEconomia * 18 + contadorComunicacionSocial * 18 + contadorAdministracionEmpresas * 20;
            //Console.ForegroundColor = ConsoleColor.DarkMagenta;
            //Console.WriteLine($"Total de Creditos Inscritos en el III periodo académico: {totalCreditos}");
            //Console.ResetColor();
        }
        static void TotalCreditosInscritosPeriodo()
        {
            int[] contadoresEstudiantes = [contadorIngenieriaSistemas, contadorPsicologia, contadorEconomia, contadorComunicacionSocial, contadorAdministracionEmpresas];
            int totalCreditos = 0;
            for (int i = 0; i < carrerasYCreditos.GetLength(0); i++) // 0,1,2,3,4 index/indice
            {
                int creditos = int.Parse(carrerasYCreditos[i, 1]);
                totalCreditos += contadoresEstudiantes[i] * creditos;
            }
            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            Console.WriteLine($"Total de Creditos Inscritos en el III periodo académico: {totalCreditos}");
            Console.ResetColor();
        }
        /*static int CalcularValorCarrera(int VALOR_CREDITO_ACADEMICO)
        {
            int[] creditosPorCarrera = { 20, 16, 18, 18, 20 };
            int[] valoresPorCarrera = new int[creditosPorCarrera.Length];
            
            for (int i = 0; i < creditosPorCarrera.Length; i++)
            {
                valoresPorCarrera[i] = VALOR_CREDITO_ACADEMICO * creditosPorCarrera[i];
            }

            return valoresPorCarrera[4];
        }*/

        static void CalcularDescuentos(int VALOR_CREDITO_ACADEMICO)
        {
            // Arreglos para almacenar los valores
            int[] valoresOriginales = new int[carrerasYCreditos.GetLength(0)];
            int[] descuentos = new int[carrerasYCreditos.GetLength(0)];
            int[] valoresConDescuento = new int[carrerasYCreditos.GetLength(0)];
            // Calcular valores originales
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("\nCosto Original de Carreras");
            Console.ResetColor();
            for (int i = 0; i < carrerasYCreditos.GetLength(0); i++)
            {
                string nombreCarrera = carrerasYCreditos[i, 0];
                int creditos = int.Parse(carrerasYCreditos[i, 1]);
                int valorCarrera = VALOR_CREDITO_ACADEMICO * creditos;
                valoresOriginales[i] = valorCarrera;
                Console.WriteLine($"{nombreCarrera}: ${valorCarrera:N0}");
            }
            // Aplicar descuentos
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("\nDescuentos Aplicados");
            Console.ResetColor();
            
            for (int i = 0; i < carrerasYCreditos.GetLength(0); i++)

            {
                string nombreCarrera = carrerasYCreditos[i, 0];
                int valorOriginal = valoresOriginales[i];
                // Lógica de descuentos 
                int descuento = CalcularDescuentoIndividual(nombreCarrera, valorOriginal); // invoco a la función auxiliar
                
                descuentos[i] = descuento;
                valoresConDescuento[i] = valorOriginal - descuento;
                
                Console.WriteLine($"{nombreCarrera}:");
                Console.WriteLine($"  Valor Original: ${valorOriginal:N0}");
                Console.WriteLine($"  Descuento:      ${descuento:N0}");
                Console.WriteLine($"  Valor Final:    ${valoresConDescuento[i]:N0}");
            }
            // Totales 
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\nResumen General");
            Console.ResetColor();
            
            int totalOriginal = valoresOriginales.Sum(); //metodo .Sum - suma los valores de una secuencia
            int totalDescuentos = descuentos.Sum();
            int totalFinal = valoresConDescuento.Sum();
            Console.WriteLine($"Valor Total Inscripciones Sin Tener en Cuenta Descuentos: ${totalOriginal:N0}");
            Console.WriteLine($"Valor Total Descuentos Aplicados:                         ${totalDescuentos:N0}");
            Console.WriteLine($"Valor Neto Total (con descuentos):                        ${totalFinal:N0}");
            TotalCreditosInscritosPeriodo(); // Invoco a la función para mostrar el total de creditos inscritos 
        }
        // Esta fucnión calcula los descuentos individuales para cada carrera
        static int CalcularDescuentoIndividual(string nombreCarrera, int valorOriginal)
        {
            // Ejemplos de reglas de descuento
            switch (nombreCarrera)
            {
                case "Ingeniería Sistemas":
                // Descuentos
                return (int)(valorOriginal * 0.18); // 18% de descuento

                case "Psicología":
                return (int)(valorOriginal * 0.12); // 12%% de descuento

                case "Economía":
                return (int)(valorOriginal * 0.10); // 10% de descuento
                
                case "Comunicación Social":
                return (int)(valorOriginal * 0.05); // 5% de descuento

                case "Administración de Empresas":
                return (int)(valorOriginal * 0.15); // 15% de descuento
            }
            return 0;
        }
    }
}