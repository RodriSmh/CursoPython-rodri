# Lista de metodos LIST

"""
    List - crea una lista
    len - longitud de la cadena
    
    Append - agrega un elemento a la lista
    insert - agrega un elemento a la lista en el indice especificado
    Extend - agrega varios elementos a la lista
    
    pop - elimina un elemento de una lista, pide indice y devuelve un valor
    remove - remueve un elemento de una lista, pide valor
    clear - elimina todos los elementos de una lista
    
    sort - ordena una lista de forma ascendente a descendente
    reverse - invierte los elementos de una lista

"""

lista = list (["hola","Rodri",32])
lista
lista.append("append")
lista.insert(0, "inicio")
lista.extend([False,3030,13,"adios","adios 2"])
# lista.pop(len(lista)-1)
# print(lista.pop(len(lista)-1))
# lista.pop(-1)
lista.remove("adios 2")

lista2= list([1,6,7,4,6,7,4,6,7,9,4,5,6])
# lista2.sort(reverse=True)
lista2.reverse()
# print(lista2)
print(dir(list))
