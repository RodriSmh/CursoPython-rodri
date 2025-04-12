# creando conjuntos con set()

conjunto = set(["dato1","dato2"])

#conjunto anidado
conjunto1= frozenset(["dato1","dato2"])
conjunto2={conjunto1,"dato3"}

# Teoria de conjuntos
conjunto1 ={1,3,5,7}
conjunto2 = {9,6,8}
# subconjunto
print(conjunto2.issubset(conjunto1))
print(conjunto2 <=(conjunto1))
# superconjunto
print(f"conjunto 1 es superconjunto de conjunto 2? {conjunto1>=conjunto2}")
print(f"los conjuntos tienen algun elemento en comun? {conjunto2.isdisjoint(conjunto1)}, si no tienen ninguno en comun es disjoint")