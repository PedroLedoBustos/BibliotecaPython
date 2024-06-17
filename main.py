from Modelo.Biblioteca import Biblioteca
from Utilidades.Utilidades import Utilidades


biblioteca= Biblioteca

def menu():
    salir=False
    print("#############################")
    print("###### Menu Principal #######")
    print("#############################")
    print("1 Alta usuario")
    print("2 Baja usuario")
    print("3 Alta Libro")
    print("4 Baja Libro")
    print("5 Préstamo Libro")
    print("6 Listado libros disponibles")
    print("7 Libros usuario")
    print("9 Salir")

    opcion= Utilidades.leerString("Escoge una opción: ")

    if opcion=="1":
        biblioteca.altaUsuario()
    elif opcion== "2":
        biblioteca.bajaUsuario()
    elif opcion== "3":
        biblioteca.altaLibro()
    elif opcion== "4":
        biblioteca.bajaLibro()
    elif opcion== "5":
        biblioteca.prestarLibro()
    elif opcion== "6":
        biblioteca.librosDisponibles()
    elif opcion== "7":
        biblioteca.librosUsuario()
    elif opcion== "9":
        print("Saliendo...")
        salir=True
    else:
        print("Escoge una opción válida")
    
    return salir

def aplicacion():
    salir=False
    while salir==False:
        salir=menu()

aplicacion()