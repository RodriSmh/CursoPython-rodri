class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,new):
        self.__nombre=new
persona= Persona("Rodri",21)
nombre = persona.nombre
print(nombre)
persona.nombre= "otro nombre"
nombre = persona.nombre
print(nombre)
