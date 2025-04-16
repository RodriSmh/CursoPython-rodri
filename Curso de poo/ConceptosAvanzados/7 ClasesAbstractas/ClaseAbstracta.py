from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.actividad=actividad
    
    @abstractclassmethod
    def actividad(self):
        pass
    def presentarse(self):
        print(f"hola, me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
    super().__init__(self,nombre,edad,sexo,actividad):
    
    def actividad(self):
        print(f"Estoy estudiando {self.actividad}")
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
    super().__init__(self,nombre,edad,sexo,actividad):
    
    def actividad(self):
        print(f"Estoy trabajando de {self.actividad}")
