def decorador(funcion):
    def funcionModificada():
        print("antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcionModificada
def saludo():
    return "hola rodirgo"
saludoModificado=decorador(saludo)
@decorador
def saludo()