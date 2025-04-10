from modulo_saludar import saludar, saludar_diferente
import funciones_buenas.modulos2
import sys
sys.path.append(r'C:\Users\640 G5\Desktop\Proyectos\Python\Curso de python\Ejercicios2')
try:
	import Ejercicio_2_3
except ModuleNotFoundError:
	print("Module 'Ejercicio_2_3' not found. Please ensure the file exists in the specified directory.")
	sys.exit(1)
print(funciones_buenas.modulos2.Saludar("Juan"))
print(Ejercicio_2_3.fibonacci(20))
# print(type(saludar))
# print(sys.path)