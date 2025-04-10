#funcion que muestre la serie fibonacci hasta n
import sys
def fibonacci(n):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(n):
        if a+b > n: return fibonacci_lista
        else:
            fibonacci_lista.append(b) 
            a,b = b,a+b
    return fibonacci_lista