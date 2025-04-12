diccionario = {
    "nombre": "Rodri",
    "apellido": "smith",
    "frase":"motd",
    "value": 45
}
for keys in diccionario.items():
    key= keys[0]
    value= keys[1]
    if value == "motd":
        continue
    print(f"clave {key} con valor de {value}")
    
numeros= [2,5,8,10]
numeros_duplicados = [x*2 for x in numeros]
print( numeros_duplicados)