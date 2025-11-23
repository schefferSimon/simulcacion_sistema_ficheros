from clases.claseCarpeta import  *
from clases.claseArchivo import *
from abc import ABC, abstractmethod

class SistemaOperativo(ABC):
    
    __ficheros = []

    def __init__(self):
        pass
    
    @abstractmethod
    def OSInfo():
        pass

    @classmethod
    def compararContenido(cls, carpeta1, carpeta2):
        pass

    @classmethod
    def eliminarArchivo(cls, carpetaNombre):
        pass

    @classmethod
    def eliminarContenido(cls, path):
        pass

    @classmethod
    def crearCarpeta(cls, nombre):
        cls.__ficheros.append(Carpeta(nombre))
        for i in cls.__ficheros:
            print(i.getNombre())
    
    @classmethod
    def crearArchivo(cls, nombreCarpeta, nombreArchivo, contenidoArchivo):
        for i in cls.__ficheros:
            if i.getNombre() == nombreCarpeta:
                i.agregarArchivo(nombreArchivo, contenidoArchivo) 
                print("creado exitosamente.")
                return

