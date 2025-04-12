#### listas
##las listas se pueden modificar
print("1. lista")
list=["Rodrigo","27"]

list[1]="Alonso"
print(list)
print(list[1])
#### Tuplas
##las tuplas no se pueden modificar
print("\n2. Tupla")
Tupla=("Rodrigo","27")

# En este caso las tublas no se pueden modificar a diferencia de las listas
#Tupla[1]="Alonso"
print(Tupla)
print(f"\n resultado de solo una parte de la tupla{Tupla[1]}\n")
#### conjunto 
## los conjuntos se pueden redefinir por completo pero no se pueden modificar los elementos
## tampoco puede mostrar duplicados
print("\n3. Conjunto")
conjunto={"hola", Tupla, "rodrigo"}

print(conjunto)
#### diccionario
print("\n4. Diccionario ")
diccionario={
    'nombre' : 'rodrigo',
    'apellido': 'paez'
}
print(diccionario["nombre"], diccionario["apellido"])