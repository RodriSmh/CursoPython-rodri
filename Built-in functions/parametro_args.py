# # primera forma de definir una función
# def suma(a, b):
#     return a + b
# resultado = suma(1, 2)
# print(resultado)
# # segunda forma de definir una función, pasando una lista como argumento
# def suma(lista):
#     numeros_sumados=0
#     for numeros in lista:
#         numeros_sumados += numeros
#     return numeros_sumados
# usando parametros args
def suma(*a):
    """
    Suma de números.
    :param a: Números a sumar
    :return: Suma de los números
    """
    return sum(a)

def suma(nombre,*args):
    """
    Suma de números.
    :param args: Números a sumar
    :return: Suma de los números
    """
    return f"{nombre} la suma de los numeros es {sum(args)}"
resultado = suma("Juan", 5, 3, 9, 10, 20, 3)
print(resultado)

