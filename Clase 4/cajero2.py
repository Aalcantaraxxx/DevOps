import tkinter as tk
from tkinter import messagebox

# Variables globales
saldo = 1000
pin_correcto = "2705"
nombre = "Angel y Fer"

# --- Funciones de Lógica ---

def verificar_pin():
    """Valida el PIN ingresado y cambia a la pantalla del menú si es correcto."""
    pin = entry_pin.get()
    
    if pin == pin_correcto:
        # Ocultar la pantalla de login
        frame_login.pack_forget()
        # Mostrar la pantalla del menú principal
        frame_menu.pack(pady=20)
        # Actualizar el mensaje de bienvenida
        label_bienvenida.config(text=f"¡Bienvenidos {nombre}!")
    else:
        messagebox.showerror("Error", "PIN incorrecto. Intente de nuevo.")
        entry_pin.delete(0, tk.END) # Limpiar el campo de texto

def consultar_saldo():
    """Muestra una ventana emergente con el saldo."""
    messagebox.showinfo("Saldo Actual", f"Su saldo actual es: ${saldo}")

def retirar_dinero():
    """Valida y resta el monto del saldo si es posible."""
    global saldo # Necesitamos indicarle a Python que modificaremos la variable global
    
    try:
        monto = float(entry_monto.get())
        if monto <= 0:
            messagebox.showwarning("Cuidado", "Ingrese un monto mayor a $0.")
        elif monto > saldo:
            messagebox.showwarning("Fondos insuficientes", "No tienes suficiente dinero en la cuenta.")
        else:
            saldo -= monto
            messagebox.showinfo("Retiro Exitoso", f"Has retirado ${monto}.\nTu nuevo saldo es: ${saldo}")
            entry_monto.delete(0, tk.END) # Limpiar el campo
    except ValueError:
        # Si el usuario escribe letras en lugar de números
        messagebox.showerror("Error de formato", "Por favor, ingrese un número válido.")
        entry_monto.delete(0, tk.END)

def salir():
    """Cierra la aplicación."""
    ventana.destroy()


# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Cajero Automático")
ventana.geometry("350x400") # Ancho x Alto

# --- Pantalla 1: Login ---
frame_login = tk.Frame(ventana)
frame_login.pack(pady=80)

tk.Label(frame_login, text="Bienvenido al cajero automático", font=("Arial", 14)).pack(pady=10)
tk.Label(frame_login, text="Ingrese su PIN:").pack()

# show="*" oculta los números del PIN por seguridad
entry_pin = tk.Entry(frame_login, show="*", font=("Arial", 14), width=10, justify="center")
entry_pin.pack(pady=10)

tk.Button(frame_login, text="Ingresar", command=verificar_pin, width=15).pack()


# --- Pantalla 2: Menú Principal (Inicia oculta) ---
frame_menu = tk.Frame(ventana)

label_bienvenida = tk.Label(frame_menu, text="", font=("Arial", 14, "bold"))
label_bienvenida.pack(pady=10)

tk.Button(frame_menu, text="1. Consultar Saldo", command=consultar_saldo, width=20).pack(pady=10)

tk.Label(frame_menu, text="Monto a retirar ($):").pack(pady=5)
entry_monto = tk.Entry(frame_menu, font=("Arial", 12), width=15, justify="center")
entry_monto.pack(pady=5)

tk.Button(frame_menu, text="2. Retirar Dinero", command=retirar_dinero, width=20).pack(pady=10)

tk.Button(frame_menu, text="3. Salir", command=salir, width=20, fg="red").pack(pady=30)

# Iniciar el bucle de la aplicación
ventana.mainloop()