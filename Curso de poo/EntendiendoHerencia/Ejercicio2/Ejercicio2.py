class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def datos(self):
        return f"""El nombre de la persona es: {self.nombre}\nLa edad es: {self.edad}"""
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado
    def datos(self):
        return f"""{super().datos()}\nEl grado es: {self.grado}"""
est= Estudiante("Jorge",33,"5to grado")
print(est.datos())