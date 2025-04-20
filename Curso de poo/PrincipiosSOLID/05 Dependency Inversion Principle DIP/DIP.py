# class Diccionario:
#     def verificar_palabra(self,palabra):
#         #logica para verificar palabras
#         pass
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario=Diccionario()
#     def corregir_texto(self,texto):
#         #usarmos el diccionario para corregir el texto
#         pass
## en el caso anterior Corrector no puede depender de diccionario ya que si se hace un cambio a la clase Diccionario se tendría que corregir tambien en Corrector
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass
class Diccionario(VerificadorOrtografico)
    def verificar_palabra(self,palabra):
        pass
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador=verificador
    def corregir_texto(self,texto):
        pass