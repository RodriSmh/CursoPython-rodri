from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
class Comedor:
    @abstractmethod
    def comer(self):
        pass
class Durmiente:
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajador,Comedor,Durmiente):
    def trabajar(self):
        print("Trabajando...")
    def comer(self):
        print("Comiendo...")
    def dormir(self):
        print("Durmiendo...")

class Robot(Trabajador):
    def trabajar(self):
        print("Trabajando")