with open("Aleer.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Hola mundo\n")
    archivo.write("Esto es una prueba\n")
    archivo.write("Adios mundo\n")
    # No es necesario cerrar el archivo, se cierra automáticamente al salir del bloque with
#     archivo.close()

# w escribe el archivo desde cero, si existe lo sobreescribe
# a añade al final del archivo, si no existe lo crea
# # r solo lectura, no se puede escribir en el archivo
# # x crea el archivo, si existe lanza un error

# with open("Aleer.txt", "w", encoding="utf-8") as archivo:
#     archivo.write("Hola mundo\n")
#     archivo.write("Esto es una prueba\n")
#     archivo.write("Adios mundo\n")
#     # No es necesario cerrar el archivo, se cierra automáticamente al salir del bloque with
# #     archivo.close()