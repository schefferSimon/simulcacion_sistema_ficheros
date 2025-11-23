class Archivo:
    def __init__(self, nombre, contenido):
        self.__nombre = nombre
        self.__contenido = contenido

    def getNombre(self):
        return self.__nombre

    def setContenido(self, nuevoContenido):
        self.__contenido = nuevoContenido
    
    def getContenido(self):
        return self.__contenido
     
    def mostrarInfo(self):
        return f"nombre: {self.__nombre}, Contenido: {self.__contenido}"