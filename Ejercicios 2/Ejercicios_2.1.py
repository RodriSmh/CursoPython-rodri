def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        
        nombre = input(f"Introduce el nombre del compañero {i+1}: ")
        edad = int(input(f"Introduce la edad del compañero {i+1}: "))
        compilero = (nombre, edad)
        compañeros.append(compilero)
    compañeros.sort(key=lambda x: x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente, profesor = obtener_compañeros(5)
print(f"El profesor es: {profesor} y el asistente es: {asistente}")