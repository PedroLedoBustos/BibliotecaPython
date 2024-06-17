from Modelo.Libro import Libro
from Modelo.Usuario import Usuario
from Utilidades.Utilidades import Utilidades


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