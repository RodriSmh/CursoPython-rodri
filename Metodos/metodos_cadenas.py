#### lista de metodos
'''
dir - devuele la lista de atributos validos para un objeto

UPPER - MAYUSCULAS
LOWER - MINUSCULAS
CAPITALIZA - MAYUSCULA LA PRIMERA LETRA

FIND - ENCUENTRA LA PRIMERA APARICION DEL VALOR ESPECIFICADO 
INDEX - AL PRIMERA APARECION DEL VALOR, DEVUELVE EXCEPCION

ISNUMERIC - DEVUELVE TRUE
ISALPHA - DEVUELVE TRUE

COUNT - DEVUELVE EL NUMERO DE OCURRENCIAS DE UNA SUBCADENA
LEN - CUENTA LOS CARACTERES

ENDSWITH - VERIFICA SI UNA CADENA COMIENZA CON
STARTSWTH - VERIFICA SI UNA CADENA TERMINA CON

REPLACE - REPLAZA UN VALOR POR OTRO
SPLIT - SEPARA POR UN PARAMETRO DADO si se coloca como parametro un espacion en blanco, regresa un arreglo de las palabras separadas por espacios
'''

###
cadena1= "Ejemplo de cadena"
cadena2= " Esta es una extencion de la segunda cadena"
cadena3= "Alfanumerico"
# print(cadena1.lower())
# print(cadena1.find("plo"))
# print(cadena3.isalpha())]
# print(cadena3.count("a"))
# print(len(cadena2))
# print(cadena2.replace("Esta es","Es" ))
print(cadena1.split(" "))