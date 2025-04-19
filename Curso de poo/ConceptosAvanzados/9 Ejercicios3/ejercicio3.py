class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre=nombre
        self.fuerza=fuerza
        self.velocidad=velocidad
    def __repr__(self):
        return f"{self.nombre}\nfuerza: {self.fuerza}\nVelocidad: {self.velocidad}"
    def __add__(self,o):
    nuevo_nombre = self.nombre + "-" +o.nombre
    nueva_fuerza =round(((self.fuerza + o.fuerza)/2)**1.5)
    nueva_velocidad=round((self.velocidad+o.o.velocidad)/2**1.5)
    return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)