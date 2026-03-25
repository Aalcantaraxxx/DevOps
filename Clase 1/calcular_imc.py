#Calculador IMC
#IMC = peso / estatura^2

peso = float(input("Dame tu peso en kg: "))
estatura = float(input("Dame tu estatura en metros: "))
imc = peso / estatura**2
imc = round(imc, 2)
print("Tu IMC es: ", imc)


