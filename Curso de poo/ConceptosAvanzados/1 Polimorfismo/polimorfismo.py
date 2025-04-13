class Gato:
    def sonido(self):
        return "Miau"
class Perro:
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    return animal.sonido()
def recorrer(elemento):
    for item in elemento:
        print(f"el elemento acutal es {item}")
gato = Gato()
hacer_sonido(gato)
lista1=[1,2,3,4]
lista2=["hola","como","estas"]
recorrer(lista2)
