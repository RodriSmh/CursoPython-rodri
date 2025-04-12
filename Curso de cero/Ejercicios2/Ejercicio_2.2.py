# funcion que regresa los numeros primos entre 0 y n
# def numeros_primos(n):
#     primos = []
#     for i in range(2, n + 1):
#         es_primo = True
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 es_primo = False
#                 break
#         if es_primo:
#             primos.append(i)
#     return primos

def es_primo(n):
    for i in range (2,n-1):
        if n % i == 0:
            return False
    return True

def primos_hasta(n):
    primos = []
    for i in range(2, n+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos
resultado = primos_hasta(13)
print(resultado)