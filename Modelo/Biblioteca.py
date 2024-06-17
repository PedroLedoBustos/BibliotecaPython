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