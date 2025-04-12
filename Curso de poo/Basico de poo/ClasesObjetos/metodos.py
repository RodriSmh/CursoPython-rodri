class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca =marca
        self.modelo = modelo
        self.camara = camara
    def llamar(self):
        return "haciendo llamada"
    
celular1 = Celular("apple","15 pro max","1000MP")
print(celular1.marca)
print(celular1.llamar())