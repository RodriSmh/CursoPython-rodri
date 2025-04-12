numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Funciones lambda
multiplicar_por_dos = lambda x: x *2
# sin lambda
def multiplicar_por_tres(x):
    return x * 3

es_par = lambda x: x % 2 == 0
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))
