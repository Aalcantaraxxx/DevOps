# Crear código que te pregunte tus hobbies, datos personales y los imprima en una cadena junta

nombre = input("¿Cuál es tu nombre? ")
edad = int (input("¿Cuál es tu edad? "))
deporte = str (input("¿Cuál es tu deporte favorito? "))
comida = str (input("¿Cuál es tu comida favorita? "))
pelicula = str (input("¿Cuál es tu película favorita? "))
print("Hola, mi nombre es ", nombre, "tengo ", edad, "años, mi deporte favorito es ", deporte, ", mi comida favorita es ", comida, "y mi película favorita es ", pelicula)

if nombre == "Angel":
    print(nombre)
else:
    print("Si")
   