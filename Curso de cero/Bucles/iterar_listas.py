animales = ["perro","gato","loro","cocodrilo"]
numeros = [6,5,3,6,7,3,4]
for animal in animales:
    print(animal)
    
for numero in numeros:
    print(numero*7),
    
# iterando dos listas al mismo tiempo
#numeros = [1,2,3,4]
for numero,animal in zip(numeros, animales):
    print(f"{numero} {animal}")
    
# iterar usando la funcion range
for numero in range(5,10):
    print(numero)

for numero in enumerate(numeros):
    indice= numero[0]
    valor=numero[1]
    print(f"El indice es {indice} con valor de: {valor}")