from Modelo.Libro import Libro
from Modelo.Usuario import Usuario
from Utilidades.Utilidades import Utilidades
import datetime


class Biblioteca:
    def __init__(self):
        self.usuarios= []
        self.libros= []

    def altaUsuario(self):
        nombre= Utilidades.leerString("Introduce el nombre del usuario: ")
        apellido= Utilidades.leerString("Introduce el apellido del usuario: ")

        usuario= Usuario(nombre,apellido)

        if any(user.getNombre()== usuario.getNombre() and user.getApellido()== usuario.getApellido() for user in self.usuarios):
            print("Lo siento el usuario ya esta dado de alta")
        else:
            self.usuarios.append(usuario)
            print("Usuario dado de alta")
    
    def bajaUsuario(self):
        nombre= Utilidades.leerString("Introduce el nombre del usuario: ")
        apellido= Utilidades.leerString("Introduce el apellido del usuario: ")

        usuario= Usuario(nombre,apellido)
        usuarioEncontrado= None

        for user in self.usuarios:
            if user.getNombre()== usuario.getNombre() and user.getApellido()== usuario.getApellido():
                usuarioEncontrado=user
        
        if usuarioEncontrado != None and usuarioEncontrado.tieneLibros() == False:
            self.usuarios.remove(usuarioEncontrado)
            print("Usuario dado de baja")
        else:
            print("El usuario no esta registrado o tiene libros prestados")

    def altaLibro(self):
        titulo= Utilidades.leerString("Introduce el título del libro: ")
        categoria= Utilidades.leerString("Introduce la categoria del libro: ")
        id= Utilidades.leerInteger("Introduce el id del libro: ")

        libro= Libro(titulo,categoria,id)

        if any(book.getId()== libro.getId() for book in self.libros):
            print("Lo siento, este libro ya esta dado de alta")
        else:
            self.libros.append(libro)
            print("Libro dado de alta")
    
    def bajaLibro(self):
        id= Utilidades.leerInteger("Introduce el id del libro que quieres dar de baja: ")
        libroEncontrado= None

        for book in self.libros:
            if book.getId()== id:
                libroEncontrado=book

        if libroEncontrado != None and libroEncontrado.getPrestado()==False:
            self.libros.remove(libroEncontrado)
            print(f"El libro con el titulo: {libroEncontrado.getTitulo()} ha sido dado de baja")
        else:
            print("El libro no se puede dar de baja porque no esta registrado o esta prestado")

    def prestarLibro(self):
        id= Utilidades.leerInteger("Introduce el id del libro que quieres prestar: ")
        libroEncontrado=None
        for book in self.libros:
            if book.getId()== id:
                libroEncontrado=book
        
        if libroEncontrado ==None or libroEncontrado.getPrestado()==True:
            print("El libro no esta registrado o ya esta prestado")
        else:
            nombre= Utilidades.leerString("Introduce el nombre del usuario al que se va a prestar el libro: ")
            apellido= Utilidades.leerString("Introduce el apellido del usuario al que se va a prestar el libro: ")
            usuario= Usuario(nombre,apellido)
            for user in self.usuarios:
                if user.getNombre()== usuario.getNombre() and user.getApellido()== usuario.getApellido():
                    user.agregarLibro(libroEncontrado)
                    libroEncontrado.setUsuario(user)
                    libroEncontrado.setPrestado(True)
                    fecha= datetime.datetime.now()
                    libroEncontrado.setFecha(fecha)
                    print(f"El libro: {libroEncontrado.getTitulo()} ha sido prestado al usuario {user.getNombre()}")
                else:
                    print("El usuario no esta registrado, no se puede prestar el libro")
    
    def librosDisponibles(self):
        self.libros.sort (key=lambda libro:libro.getCategoria())
        if not self.libros:
            print("No hay libros disponibles en la biblioteca")
        else:
            for libro in self.libros:
                if libro.getPrestado()== False:
                    print(f"TITULO: {libro.getTitulo()} CATEGORIA: {libro.getCategoria()} PRESTADO: {libro.getPrestado()}")

    def librosUsuario(self):
        nombre= Utilidades.leerString("Introduce el nombre del usuario: ")
        apellido= Utilidades.leerString("Introduce el apellido del usuario: ")
        usuario= Usuario(nombre,apellido)
        listaLibros=[]

        for user in self.usuarios:
            if user.getNombre()== usuario.getNombre() and user.getApellido()== usuario.getApellido():
                listaLibros= user.getLibros()
        
        if listaLibros== None:
            print("Este usuario no tiene libros prestados")
        else:
            print(f"LIBROS PRESTADOS AL USUARIO: {user.getNombre()}")
            for libro in listaLibros:
                print(f"Titulo: {libro.getTitulo()} Categoria: {libro.getCategoria()} Fecha: {libro.getFecha()}")

