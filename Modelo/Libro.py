class Libro:
    def __init__(self, titulo, categoria, id):
        self.titulo=titulo
        self.categoria=categoria
        self.id= id
        self.prestado= False
        self.usuario=None

    def getTitulo(self):
        return self.titulo
    
    def getCategoria(self):
        return self.categoria
    
    def getId(self):
        return self.id
    
    def getPrestado(self):
        return self.prestado
    
    def getUsuario(self):
        return self.usuario
    
    def setPrestado(self, estaPrestado):
        self.prestado= estaPrestado

    def setUsuario(self, usuarioNuevo):
        self.usuario= usuarioNuevo

