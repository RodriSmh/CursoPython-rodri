import re

texto ="Hola, ¿cómo estas? hola hola Hola 1 2 344 4 "

#resultado=re.findall("Hola",texto,flags=re.IGNORECASE)
# \w busca caracteres alfanumericos
# \d busca digitos, \D busca todo menos digitos
# \n busca todos los saltos de linea
resultado = re.findall(r'\d{3}',texto)
resultado = re.findall(r'\d{1,3}',texto)
resultado = re.findall(r'as{1,3}',texto,flags=re.IGNORECASE)
print(resultado)