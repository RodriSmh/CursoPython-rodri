diccionario = dict(nombre="Rodri",apellido="Smith")
# no se puede crear diccionarios vacios de la forma '{}', se tiene que llamar al metodo
# las listas pueden ser clave 
diccionario= {("probando","una"):"Cadena"}
#creando diccionarios con fromkeys
diccionario = dict.fromkeys(["nombre","apellido","mensaje"])
print(diccionario)