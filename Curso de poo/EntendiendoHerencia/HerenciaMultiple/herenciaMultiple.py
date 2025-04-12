class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
    def hablar():
        return f"Persona hablando"
class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad
    def mostrar_habilidad(self):
        return f"Mi habilidad es {habilidad}"
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    def hablar(self):
        return "empleado hablando"
    def toString(self):
        return f"""Nombre del empleado: {self.nombre}\nEdad del empleado: {self.edad}\nNacionalidad del empleado {self.nacionalidad}\nTrabajo del empleado: {self.trabajo}\nSalario del empleado: {self.salario}$"""
class EmpleadoArtista(Empleado,Artista):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario,habilidad):
        Empleado.__init__(self,nombre,edad,nacionalidad,trabajo,salario)
        Artista.__init__(self,habilidad)
    def presentarse(self):
        return f"{super()o.mostrar_habilidad()}"
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,grado,escuela):
        super().__init__(nombre,edad,nacionalidad)
        self.grado=grado
        self.escuela=escuela
    def hablar(self):
        return "estudiante hablando"
    def toString(self):
        return f"""Nombre del estudiante: {self.nombre}\nEdad del estudiante: {self.edad}\nNacionalidad del estudiante {self.nacionalidad}\nGrado del estudiante: {self.grado}\nEscuela del estudiante: {self.escuela}"""
    
emp = Empleado("rodrigo",20,"Mexicana","programador","20000")
est= Estudiante("rodri",20,"mexicana",10,"tecnm")
print(emp.hablar())
print(emp.toString())
print(est.hablar())
print(est.toString())
