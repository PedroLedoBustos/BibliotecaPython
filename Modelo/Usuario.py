class Usuario:
    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        self.libros=[]
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def tieneLibros(self):
        if not self.libros:
            return False
        else:
            return True
    
    def agregarLibro(self,libro):
        self.libros.append(libro)
    
    def getLibros(self):
        if not self.libros:
            return None
        else:
            return self.libros