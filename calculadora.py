# Calculadora: Suma, resta, division, multiplicacion, potencia y raiz cuadrada

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
print("6. Raíz cuadrada")

op = input("Elige el número de la operación que quieres hacer: ")

if op in ['1', '2', '3', '4', '5']:
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))

    if op == '1':
        print("Resultado:", n1 + n2)
    
    elif op == '2':
        print("Resultado:", n1 - n2)
    
    elif op == '3':
        print("Resultado:", n1 * n2)
    
    elif op == '4':
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("No se puede dividir entre cero.")
            
    elif op == '5':
        print("Resultado:", n1 ** n2)

elif op == '6':
    n1 = float(input("Ingresa el número para sacarle raíz cuadrada: "))
    
    if n1 >= 0:
        print("Resultado:", n1 ** 0.5)
    else:
        print(" No se puede sacar raíz cuadrada de números negativos.")

else:
    print("Opción incorrecta.")