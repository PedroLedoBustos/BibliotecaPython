from Modelo.Libro import Libro
from Modelo.Usuario import Usuario
from Utilidades.Utilidades import Utilidades
import datetime


class Biblioteca:
    usuarios= []
    libros= []

    def altaUsuario():
        nombre= Utilidades.leerString("Introduce el nombre del usuario: ")
        apellido= Utilidades.leerString("Introduce el apellido del usuario: ")

        usuario= Usuario(nombre,apellido)

        if any(user.getNombre()== usuario.getNombre() and user.getApellido()== usuario.getApellido() for user in Biblioteca.usuarios):
            print("Lo siento el usuario ya esta dado de alta")
        else:
            Biblioteca.usuarios.append(usuario)
            print("Usuario dado de alta")
    
    def bajaUsuario():
        nombre= Utilidades.leerString("Introduce el nombre del usuario: ")
        apellido= Utilidades.leerString("Introduce el apellido del usuario: ")

        usuario= Usuario(nombre,apellido)
        usuarioEncontrado= None

        for user in Biblioteca.usuarios:
            if user.getNombre()== usuario.getNombre() and user.getApellido()== usuario.getApellido():
                usuarioEncontrado=user
        
        if usuarioEncontrado != None and usuarioEncontrado.tieneLibros() == False:
            Biblioteca.usuarios.remove(usuarioEncontrado)
            print("Usuario dado de baja")
        else:
            print("El usuario no esta registrado o tiene libros prestados")

    def altaLibro():
        titulo= Utilidades.leerString("Introduce el título del libro: ")
        categoria= Utilidades.leerString("Introduce la categoria del libro: ")
        id= Utilidades.leerInteger("Introduce el id del libro: ")

        libro= Libro(titulo,categoria,id)

        if any(book.getId()== libro.getId() for book in Biblioteca.libros):
            print("Lo siento, este libro ya esta dado de alta")
        else:
            Biblioteca.libros.append(libro)
            print("Libro dado de alta")
    
    def bajaLibro():
        id= Utilidades.leerInteger("Introduce el id del libro que quieres dar de baja: ")
        libroEncontrado= None

        for book in Biblioteca.libros:
            if book.getId()== id:
                libroEncontrado=book

        if libroEncontrado != None and libroEncontrado.getPrestado()==False:
            Biblioteca.libros.remove(libroEncontrado)
            print(f"El libro con el titulo: {libroEncontrado.getTitulo()} ha sido dado de baja")
        else:
            print("El libro no se puede dar de baja porque no esta registrado o esta prestado")

    def prestarLibro():
        id= Utilidades.leerInteger("Introduce el id del libro que quieres prestar: ")
        libroEncontrado=None
        for book in Biblioteca.libros:
            if book.getId()== id:
                libroEncontrado=book
        
        if libroEncontrado ==None or libroEncontrado.getPrestado()==True:
            print("El libro no esta registrado o ya esta prestado")
        else:
            nombre= Utilidades.leerString("Introduce el nombre del usuario al que se va a prestar el libro: ")
            apellido= Utilidades.leerString("Introduce el apellido del usuario al que se va a prestar el libro: ")
            usuario= Usuario(nombre,apellido)
            for user in Biblioteca.usuarios:
                if user.getNombre()== usuario.getNombre() and user.getApellido()== usuario.getApellido():
                    user.agregarLibro(libroEncontrado)
                    libroEncontrado.setUsuario(user)
                    libroEncontrado.setPrestado(True)
                    fecha= datetime.datetime.now()
                    libroEncontrado.setFecha(fecha)
                    print(f"El libro: {libroEncontrado.getTitulo()} ha sido prestado al usuario {user.getNombre()}")
                else:
                    print("El usuario no esta registrado, no se puede prestar el libro")
    
    def librosDisponibles():
        Biblioteca.libros.sort (key=lambda libro:libro.getCategoria())
        if not Biblioteca.libros:
            print("No hay libros disponibles en la biblioteca")
        else:
            for libro in Biblioteca.libros:
                if libro.getPrestado()== False:
                    print(f"TITULO: {libro.getTitulo()} CATEGORIA: {libro.getCategoria()} PRESTADO: {libro.getPrestado()}")

    def librosUsuario():
        nombre= Utilidades.leerString("Introduce el nombre del usuario: ")
        apellido= Utilidades.leerString("Introduce el apellido del usuario: ")
        usuario= Usuario(nombre,apellido)
        listaLibros=[]

        for user in Biblioteca.usuarios:
            if user.getNombre()== usuario.getNombre() and user.getApellido()== usuario.getApellido():
                listaLibros= user.getLibros()
        
        if listaLibros== None:
            print("Este usuario no tiene libros prestados")
        else:
            print(f"LIBROS PRESTADOS AL USUARIO: {user.getNombre()}")
            for libro in listaLibros:
                print(f"Titulo: {libro.getTitulo()} Categoria: {libro.getCategoria()} Fecha: {libro.getFecha()}")

