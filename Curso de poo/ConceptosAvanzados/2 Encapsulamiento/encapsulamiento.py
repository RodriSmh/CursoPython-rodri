class MiClase:
    def __init__(self):
        self._atributoProtegido= "Protegido" #con el primer guion bajo se denota protegido
        self.__atributoPrivado="privado" #con el doble guion bajo se denota privado

o=MiClase()
print(o._atributoProtegido)
print(o.__atributoPrivado)