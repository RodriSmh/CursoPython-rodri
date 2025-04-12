class Estudiante:
    def __init__(self,Nombre,Edad,Grado):
        self.Nombre=Nombre
        self.Edad=Edad
        self.Grado=Grado
    def toString(self):
        return f"""Nombre: {self.Nombre}
    Edad: {self.Edad}
    Grado: {self.Grado}"""
    def estudiar(self):
        return f"El estudiante {self.Nombre} está estudiando"

nombre = input("Ingresa el nombre del estudiante: ")
edad= input("Ingresa la edad del estudiante: ")
grado= input("Ingresa el grado del estudiante: ")
estudiante1=Estudiante(nombre,edad,grado)
print(estudiante1.toString())
print(estudiante1.estudiar())