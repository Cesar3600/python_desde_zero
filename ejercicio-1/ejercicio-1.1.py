
# 

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
mi_curso = 1.5

diferencia_con_min       =  100 - (mi_curso / otros_cursos_min * 100) 
diferencia_con_max       =  100 - (mi_curso / otros_cursos_max * 100) 
diferencia_con_promedio  =  100 - (mi_curso / otros_cursos_promedio * 100) 


print("el curso dura un {diferencia_con_min}% menos que el mas rapido")
print("el curso dura un {diferencia_con_max}% menos que el mas lento")
print("el curso dura un {diferencia_con_promedio}% menos que el promedio")







