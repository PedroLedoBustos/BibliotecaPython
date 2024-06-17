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
        return self.titulo
    
    def getId(self):
        return self.titulo
    
    def getPrestado(self):
        return self.titulo
    
    def getUsuario(self):
        return self.titulo
    
    def setPrestado(self, estaPrestado):
        self.prestado= estaPrestado

    def setUsuario(self, usuarioNuevo):
        self.usuario= usuarioNuevo

