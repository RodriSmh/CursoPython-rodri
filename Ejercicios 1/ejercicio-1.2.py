frase = input("Ingresa una frase y te calculará cuanto tardaras en decirla: ")
palabras_separadas=frase.split(" ")
cantidad_de_palabras = len (palabras_separadas)

print(f'Si dijiste {cantidad_de_palabras} palabras te tardarias {cantidad_de_palabras/2} segundos en decir la frase')

