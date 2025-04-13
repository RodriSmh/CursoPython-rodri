class Animal:
    def comer(self):
        return "El animal está comiendo"
class Ave(Animal):
    def volar(self):
        return "El Ave está volando"
class Mamifero(Animal):
    def amamantar(self):
        return "El mamifero amamanta"
class Murcielago(Mamifero,Ave):
    pass

mur= Murcielago()
print(f"{mur.comer()}\n{mur.volar()}\n{mur.amamantar()}")