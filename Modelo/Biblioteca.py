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