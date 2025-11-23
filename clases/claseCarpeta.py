from claseArchivo import *
class Carpeta:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__listaArchivos = []


    def agregarArchivo(self,nombre, contenido):

        nuevoArchivo = Archivo(nombre, contenido)
        self.__listaArchivos.append(nuevoArchivo)

    def eliminarArchivo(self, nombreArchivo):
        for archivo in self.__listaArchivos:
            if archivo.getNombre() == nombreArchivo:
                self.__listaArchivos.remove(archivo)

    def mostrarArchivos(self):
        for i in self.__listaArchivos:
            print(i.mostrarInfo())
         
            
carpetauno = Carpeta("prueba")

carpetauno.agregarArchivo("archivo", "hola mundo")
#carpetauno.eliminarArchivo("archivo")

carpetauno.mostrarArchivos()






    