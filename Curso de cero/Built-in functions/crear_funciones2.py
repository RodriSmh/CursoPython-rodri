def saludar(sexo):
    sexo.lower()
    if (sexo == "hombre"):
        adjetivo = "caballero"
    elif (sexo == "mujer"):
        adjetivo = "dama"
    else:
        adjetivo = "persona"
    print(f"¡Hola, {adjetivo})!")
    
# saludar("hombre")

def aceleracion(velocidad_final, velocidad_inicial, tiempo):
    """
    Esta función calcula la aceleración dada la velocidad final, la velocidad inicial y el tiempo.
    """
    return (velocidad_final - velocidad_inicial) / tiempo

velocidad_final = int(input("ingresa la velocidad final: "))  # Velocidad final en m/s
velocidad_inicial = int(input("ingresa la velocidad inicial: "))  # Velocidad inicial en m/s
tiempo = int(input("ingresa la velocidad en segundos: "))  # Tiempo en segundos
print(f'La aceleración es: {aceleracion(velocidad_final, velocidad_inicial, tiempo)} m/s²')
