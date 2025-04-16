class Auto():
    def __init__(self):
        self.__estado = "apagado"
    def encender(self):
        self.__estado = "encendido"
        print("El auto está encendido")
    def conducir(self):
        if self.__estado =="apagado":
            self.encender()
        print("condiciendo el auto")

miAuto = Auto()
miAuto.conducir()