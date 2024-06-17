class Utilidades:

    @staticmethod
    def leerString(dato):
        respuesta= input(dato)
        return respuesta
    
    @staticmethod
    def leerInteger(dato):
        while True:
            try:
                respuesta= int(input(dato))
                return respuesta
            except:
                print("Introduce un valor válido")