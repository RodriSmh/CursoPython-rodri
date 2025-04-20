class Auto():
    def __init__(self,tanque):
        self.posicion=0
        self.tanque= tanque
        
    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print("has movido el auto")
        else:
            print("No hay suficiente combustible")
    def obtener_posicion(self):
        return self.posicion
        
class Tanque:
    def __init__(self):
        self.combustible=100
    
    def agregar_combustible(self,cantidad):
        self.combustible+=cantidad
    def obtener_combustible(self):
        return self.combustible
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad
t=Tanque()
coche= Auto(t)

print(coche.obtener_posicion())
coche.mover(10)
print(coche.obtener_posicion())
coche.mover(50)
print(coche.obtener_posicion())
coche.mover(30)
print(coche.obtener_posicion())
coche.mover(20)
print(coche.obtener_posicion())
coche.mover(80)
print(coche.obtener_posicion())
coche.mover(70)