# numero mayor
numeros = [1, 2, 3, 4, 5]
mayor = max(numeros)
print(mayor)  
# numero menor
menor = min(numeros)
print(menor)
# usando round
pi = 3.14159
pi_redondeado = round(pi, 3)
print(pi_redondeado)
# usando abs
numero_negativo = -10
numero_positivo = abs(numero_negativo)
print(f"abs {numero_positivo}")
# usando bool
numero = 0
booleano = bool(numero)
print(f"bool {booleano}")
# usando all
numeros = [1, 2, 3, 4, 5]
resultado = all(n > 0 for n in numeros)
print(f"all {resultado}")
# usando sum
resultado = sum(numeros)
print(f"sum {resultado}")