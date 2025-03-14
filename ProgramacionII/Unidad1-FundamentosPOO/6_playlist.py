"""
Define una clase Playlist que contenga una lista de canciones.
Cada canción puede representarse como un diccionario con
atributos titulo, artista, y duracion. Agrega métodos
agregar_cancion(cancion) y eliminar_cancion(titulo), así como
duracion_total() que devuelva la duración total de todas las
canciones. Crea una instancia de Playlist, añade y elimina
canciones, y calcula la duración total.
"""
class Playlist: 
    def __init__(self): 
        # Una lista de diccionarios. Aqui se van a almacenar los datos ingresados. Puse algunos datos de ejemplo
        self.lista_canciones = [
            {"titulo": "Smells Like Teen Spirit", "artista": "Nirvana", "duracion": 4},
            {"titulo": "Like a Stone", "artista": "AudioSlave", "duracion": 5},
            {"titulo": "Man in The Box", "artista": "Alice In Chains", "duracion": 4},
            {"titulo": "Go", "artista": "Pearl Jam", "duracion": 3}
        ] 
    
    def agregar_cancion(self): 
        atributos = ["titulo", "artista", "duracion"] # lista
        cancion = {} # Diccionario para almacenar las canciones
        try:
            for atributo in atributos: # El bucler recorre nuestra lista de atributos
                if atributo == "duracion": # Condicion unica para el atributo 'duracion'
                    while(True):
                        try:
                            valor_ingresado = int(input(f"Ingresa la {atributo} de la canción: "))
                            # Validacion para que el valor ingresadosea positivo
                            if valor_ingresado > 0:
                                cancion[atributo] = valor_ingresado
                                break
                            else:
                                print("\nERROR: La duración debe ser un valor positivo (mayor a 0), intenta ingresar otro número")
                        except ValueError: # El bloque try-except verifica que no se ingresen datos de tipo string (texto)
                            print("\nERROR: La duración de la canción debe ser un número entero, intente nuevamente")
                else: # Para los demas atributos
                    valor_ingresado = input(f"ingresa el {atributo} de canción: ")
                    cancion[atributo] = valor_ingresado
            # Se agrega el diccionario a la lista con el metodo append()
            self.lista_canciones.append(cancion)
            print(f"Nuevo track añadido -'{cancion["artista"]}'- '{cancion["titulo"]}' ")
        # Manejo de errores cuando se interrumpa el programa
        except EOFError:
            print("\n\nEjecucion cancelada (×_×)\n")
            exit()
        except KeyboardInterrupt:
            print("\n\nEjecucion cancelada (×_×)\n")
            exit()

    def eliminar_cancion(self): # Este metodo elimina el ultimo diccionario (la ultima cancion) agregado a la lista
        self.lista_canciones.pop() # metodo pop() 
        print(f"Canción - '{self.lista_canciones[-1]}' eliminada...")
        

    def duracion_total(self):
        # Para sumar los valores en la ultima columna (columna 3)
        total_duracion = 0
        for cancion in self.lista_canciones:
            total_duracion += cancion["duracion"]
        return total_duracion
    
    def mostrar_playlist(self): # Este metodo recorre los elementos de la lista de diccionarios 
        print("\n---PLAYLIST ▶︎ ─•────")
        for cancion in self.lista_canciones:
            print(cancion)

    @staticmethod # Decorador para definir un metodo estatico
    def main(): # El metodo principal. Al ser estatico no recibe parametros
        while(True):
            print("\n\t---REPRODUCTOR---\n\t")
            print("¿Que desea hacer?\n1)Agregar una cancion a la playlist\n2)Eliminar una cancion\n3)Ver la duracion total\n4)Mostrar lista de reproduccion\n5)Salir del programa ")
            try:
                opcion_seleccionada = input("-->: ")
                match opcion_seleccionada:
                    case "1":
                        playlist.agregar_cancion()
                        # Llamo a este metodo para mostrar los datos añadidos
                    case "2":
                        playlist.eliminar_cancion()
                    case "3":
                        print(f"\n{playlist.duracion_total()} minutos de música en total (¬‿¬)")
                    case "4":
                        playlist.mostrar_playlist()
                    case"5":
                        print(f"\nSaliste del programa satisfactoriamente")
                        break
            except EOFError: # al oprimir ctrl + d3
                print("\n\nEjecucion cancelada (×_×)\n") 
                exit() # sale del programa
            except KeyboardInterrupt: # al oprimir ctrl + c
                print("\n\nEjecucion cancelada (×_×)\n")
                exit() 
# Instancia de la clase
playlist = Playlist()
playlist.main()

