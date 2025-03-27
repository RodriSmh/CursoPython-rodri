otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_optimo=1.5

# duracion de crudo
crudo_promedio=5
crudo_optimo=3.5

# diferencias de duracion
diferencias_min = 100- curso_optimo /otros_cursos_min*100
print(diferencias_min)

# calculando tiempo vacio
tiempo_vacio_promido=100- otros_cursos_promedio * 1000 // crudo_promedio /10
print(f'el curso promedio elimina un {tiempo_vacio_promido}% de tiempo vacio')

#mostrando las diferecias si los cursos duraran 10 horas
print(f'ver 10 horas del curso optimo equivale a ver {otros_cursos_promedio*100/curso_optimo /10} horas de otros cursos')