class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.__nombre=nombre