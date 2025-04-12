def sumar_dos():
    while True:
        a = input("numero 1: ")
        b = input("numero 2: ")
        try:
            resultado = int(a) + int(b)
        except:
            print("ingresa numeros...")
        else:
            break
    return resultado

print(sumar_dos())