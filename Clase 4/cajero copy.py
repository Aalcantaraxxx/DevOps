# CAJERO ATM usando While, agregando datos del usuario, validacion del pin y un menu de opciones para consultar saldo, retirar dinero o salir del cajero 
saldo = 1000
pin_correcto = "2705"
nombre = "Angel y Fer"

while True:
    print("Bienvenido al cajero automático")
    pin = input("Ingrese su PIN: ")
    
    if pin == pin_correcto:
        print(f"PIN correcto. Bienvenidos {nombre}")
        while True:
            print("\n--- Menú ---")
            print("1. Consultar saldo")
            print("2. Retirar dinero")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(f"Su saldo actual es: ${saldo}")
            elif opcion == "2":
                monto = float(input("Ingrese el monto a retirar: "))
                if monto > saldo:
                    print("Fondos insuficientes.")
                else:
                    saldo -= monto
                    print(f"Has retirado ${monto}. Tu nuevo saldo es: ${saldo}")
            elif opcion == "3":
                print("Gracias por usar el cajero automático. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        break
    else:
        print("PIN incorrecto. Intente de nuevo.\n")