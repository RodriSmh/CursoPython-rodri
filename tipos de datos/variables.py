##variables
nombre="rodrigo"

edad=27
# F strings, sirve para poder poner formato y así poder concatenar las variables de manera mas sencilla 
# se coloca f antes del string y se coloca llaves donde iran variables que se pondran en la cadena 
#bienvenida= f"hola {nombre}, bienvenido"
# las comillas triples sirven para poder colocar saltos de linea
bienvenida= f"""Hola {nombre}, bienvenido
tu edad es {edad}"""
# la palabra reservada del sirve para eliminar las variables 
del nombre
print(bienvenida)
#la palabra reservada in busca una sub cadena proporcionada en una cadena, regresa un valor booleano
print("ad"in bienvenida)