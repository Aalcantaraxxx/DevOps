# Sistema de Calificaciones de Materias Reprobatorias o Aprobatorias 
# Materias: Full Stack, DevOps, Inglés y Gestión de Redes


print("Sistema para calcular promedio de un alumno")

nombre = input("Ingrese el nombre del alumno: ")

fullstack = int(input("Ingrese la calificación de Full Stack: "))
devops = int(input("Ingrese la calificación de DevOps: "))
ingles = int(input("Ingrese la calificación de Inglés: "))
gestion_redes = int(input("Ingrese la calificación de Gestión de Redes: "))

promedio = (fullstack + devops + ingles + gestion_redes) / 4

if promedio >= 60:
    print(f"{nombre} ha aprobado con un promedio de {promedio:}")
else:
    print(f"{nombre} ha reprobado con un promedio de {promedio:}")

if promedio == 10:
    print("Excelente")
elif promedio >= 9:
    print("Muy bien")
elif promedio >= 8:
    print("Bien")
elif promedio >= 7:
    print("Regular")
elif promedio >= 6:
    print("Insuficiente")
elif promedio >= 5:
    print("Deficiente")
else:    
    print("Reprobado")

