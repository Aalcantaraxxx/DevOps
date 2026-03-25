import tkinter as tk
from tkinter import messagebox
# from PIL import Image, ImageTk

# --- Variables Globales y Datos Simulados ---
SALDO = 100000.0
PIN_CORRECTO = "2705"
NOMBRE_USUARIO = "Angel y Fer"
TARJETA_TERMINACION = "1234"

# --- Configuración de Colores BBVA y Diseño MEJORADA ---
COLOR_FONDO_CORTINA = "#072146"  # Azul oscuro principal
COLOR_PANEL_AZUL = "#00477E"     # Azul para paneles de saldo y retiro
COLOR_CYAN_ACCION = "#00D2D3"    # Cian solo para acciones importantes (como confirmar retiro)
COLOR_TEXTO_PRIMARIO = "white"
COLOR_TEXTO_SECUNDARIO = "#A6A6A6"
COLOR_FONDO_APP = "#1E1E1E"      # Gris muy oscuro/casi negro en lugar de morado
COLOR_BOTON_SECUNDARIO = "#E0E0E0" # Gris claro para botones de salir/movimientos

FONT_ENCABEZADO = ("Arial", 14, "bold")
FONT_TITULO_GRANDE = ("Arial", 28, "bold")
FONT_MENSAJE_ALERTA = ("Arial", 16)
FONT_BOTON = ("Arial", 12, "bold")
FONT_TEXTO_MENUDO = ("Arial", 12)

# --- Funciones de Lógica ---
def verificar_pin():
    pin = entry_pin.get()
    if pin == PIN_CORRECTO:
        frame_login.pack_forget()
        CargarPantallaMenuPrincipal()
    else:
        messagebox.showerror("PIN Incorrecto", "El PIN ingresado no es válido.", parent=ventana)
        entry_pin.delete(0, tk.END)

def realizar_retiro(monto_entry):
    global SALDO
    try:
        monto = float(monto_entry.get())
        if monto <= 0:
            messagebox.showwarning("Cuidado", "Ingrese un monto mayor a $0.", parent=ventana)
        elif monto > SALDO:
            messagebox.showwarning("Fondos Insuficientes", "Su saldo es insuficiente.", parent=ventana)
        else:
            SALDO -= monto
            messagebox.showinfo("Retiro Exitoso", f"Has retirado ${monto:.2f}.\nTu nuevo saldo es: ${SALDO:.2f}", parent=ventana)
            monto_entry.delete(0, tk.END)
            # Refrescar pantalla
            frame_actual.pack_forget()
            CargarPantallaMenuPrincipal()
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.", parent=ventana)
        monto_entry.delete(0, tk.END)

def salir():
    frame_actual.pack_forget()
    CargarPantallaInicio()

# --- Funciones para Cargar Pantallas ---
def CargarPantallaInicio():
    global frame_login, entry_pin, frame_actual
    frame_login = tk.Frame(area_contenido, bg=COLOR_FONDO_CORTINA)
    frame_login.pack(expand=True, fill="both")
    frame_actual = frame_login
    
    panel_seguridad = tk.Frame(frame_login, bg=COLOR_FONDO_CORTINA)
    panel_seguridad.pack(pady=40, fill="x")
    
    tk.Label(panel_seguridad, text="Que no te distraigan,\nnunca pierdas de vista\ntu tarjeta", 
             font=FONT_TITULO_GRANDE, fg=COLOR_TEXTO_PRIMARIO, bg=COLOR_FONDO_CORTINA, justify="left").pack(anchor="w", padx=40, pady=(10, 0))
    tk.Label(panel_seguridad, text="Protégete, que no te engañen.", 
             font=FONT_MENSAJE_ALERTA, fg=COLOR_CYAN_ACCION, bg=COLOR_FONDO_CORTINA, justify="left").pack(anchor="w", padx=40, pady=10)
    
    tk.Frame(panel_seguridad, height=1, width=400, bg=COLOR_TEXTO_SECUNDARIO).pack(anchor="w", padx=40, pady=10)

    frame_input = tk.Frame(frame_login, bg=COLOR_FONDO_CORTINA)
    frame_input.pack(pady=20)
    
    tk.Label(frame_input, text="Ingresa tu PIN de 4 dígitos:", font=FONT_TEXTO_MENUDO, fg=COLOR_TEXTO_PRIMARIO, bg=COLOR_FONDO_CORTINA).pack(pady=5)
    entry_pin = tk.Entry(frame_input, show="*", font=("Arial", 32, "bold"), width=6, justify="center")
    entry_pin.pack(pady=10)
    entry_pin.focus_set()
    
    tk.Button(frame_login, text="CONFIRMAR", command=verificar_pin, font=FONT_BOTON, fg="black", bg=COLOR_CYAN_ACCION, width=20, pady=10).pack(pady=20)

    # Footer de Inicio
    footer_inicio = tk.Frame(frame_login, bg=COLOR_FONDO_CORTINA, height=80)
    footer_inicio.pack(side="bottom", fill="x", pady=20, padx=20)
    
    # Botón Salir gris claro a la derecha
    btn_salir_marco = tk.Frame(footer_inicio, bg=COLOR_FONDO_CORTINA)
    btn_salir_marco.pack(side="right", padx=10)
    tk.Button(btn_salir_marco, text="SALIR", command=ventana.destroy, font=FONT_BOTON, bg=COLOR_BOTON_SECUNDARIO, fg="black", width=15, height=2).pack()

def CargarPantallaMenuPrincipal():
    global frame_menu, frame_actual
    frame_menu = tk.Frame(area_contenido, bg=COLOR_FONDO_CORTINA)
    frame_menu.pack(expand=True, fill="both")
    frame_actual = frame_menu
    
    tk.Label(frame_menu, text=f"¡Bienvenido, {NOMBRE_USUARIO}!", font=("Arial", 20, "bold"), fg=COLOR_TEXTO_PRIMARIO, bg=COLOR_FONDO_CORTINA).pack(anchor="w", padx=40, pady=(30, 5))
    tk.Label(frame_menu, text=f"Tarjeta terminación {TARJETA_TERMINACION}", font=FONT_TEXTO_MENUDO, fg=COLOR_TEXTO_SECUNDARIO, bg=COLOR_FONDO_CORTINA).pack(anchor="w", padx=40)

    panel_info = tk.Frame(frame_menu, bg=COLOR_FONDO_CORTINA)
    panel_info.pack(pady=30, fill="x", padx=40)
    
    panel_info.columnconfigure(0, weight=1)
    panel_info.columnconfigure(1, weight=1)

    # Mosaico Izquierdo (Saldo) - Ahora es azul igual que el fondo general pero más claro
    tile_saldo = tk.Frame(panel_info, bg=COLOR_PANEL_AZUL, pady=30, padx=20)
    tile_saldo.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
    tk.Label(tile_saldo, text="Saldo Disponible", font=FONT_TEXTO_MENUDO, fg=COLOR_TEXTO_SECUNDARIO, bg=COLOR_PANEL_AZUL).pack(anchor="w")
    tk.Label(tile_saldo, text=f"${SALDO:.2f}", font=FONT_TITULO_GRANDE, fg=COLOR_TEXTO_PRIMARIO, bg=COLOR_PANEL_AZUL).pack(anchor="w", pady=10)
    
    # Mosaico Derecho (Retiro) - Ya no es celeste, es azul igual que el de saldo
    tile_retiro = tk.Frame(panel_info, bg=COLOR_PANEL_AZUL, pady=20, padx=20)
    tile_retiro.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
    tk.Label(tile_retiro, text="Retiro Rápido ($)", font=FONT_TEXTO_MENUDO, fg=COLOR_TEXTO_PRIMARIO, bg=COLOR_PANEL_AZUL).pack(anchor="w")
    entry_monto_retiro = tk.Entry(tile_retiro, font=("Arial", 24, "bold"), width=10, justify="center")
    entry_monto_retiro.pack(pady=10)
    
    # El botón de retirar sí se queda cyan para resaltar
    tk.Button(tile_retiro, text="RETIRAR", command=lambda: realizar_retiro(entry_monto_retiro), font=FONT_BOTON, fg="black", bg=COLOR_CYAN_ACCION).pack(fill="x", pady=(5, 0))

    # Footer del Menú (Botones grises a la derecha)
    footer = tk.Frame(frame_menu, bg=COLOR_FONDO_CORTINA, height=80)
    footer.pack(side="bottom", fill="x", pady=20, padx=20)
    
    # Botones en orden inverso para que "Movimientos" quede más a la derecha y "Salir" a su izquierda
    btn_mov_marco = tk.Frame(footer, bg=COLOR_FONDO_CORTINA)
    btn_mov_marco.pack(side="right", padx=10)
    tk.Button(btn_mov_marco, text="Movimientos", font=FONT_BOTON, bg=COLOR_BOTON_SECUNDARIO, fg="black", width=15, height=2).pack()
    
    btn_salir_marco = tk.Frame(footer, bg=COLOR_FONDO_CORTINA)
    btn_salir_marco.pack(side="right", padx=10)
    tk.Button(btn_salir_marco, text="SALIR", command=salir, font=FONT_BOTON, bg=COLOR_BOTON_SECUNDARIO, fg="black", width=15, height=2).pack()


# --- Configuración Principal ---
ventana = tk.Tk()
ventana.title("Cajero BBVA")
ventana.geometry("1000x750")
# ADIÓS MORADO: Cambiado a un gris muy oscuro simulando el hardware
ventana.configure(bg=COLOR_FONDO_APP) 
ventana.resizable(False, False)

# --- Contenedor Principal (El cajero entero) ---
display_cajero = tk.Frame(ventana, bg=COLOR_FONDO_CORTINA, width=850, height=650)
display_cajero.place(relx=0.5, rely=0.5, anchor="center") 
display_cajero.pack_propagate(False)

# --- Encabezado ---
header = tk.Frame(display_cajero, bg=COLOR_FONDO_CORTINA, height=80)
header.pack(fill="x", pady=(20,0), padx=40)

tk.Label(header, text="Bienvenido a", font=FONT_ENCABEZADO, fg=COLOR_TEXTO_PRIMARIO, bg=COLOR_FONDO_CORTINA).pack(side="left")
tk.Label(header, text="BBVA", font=("Arial", 24, "bold"), fg=COLOR_TEXTO_PRIMARIO, bg=COLOR_FONDO_CORTINA).pack(side="left", padx=10)

info_frame = tk.Frame(header, bg=COLOR_FONDO_CORTINA)
info_frame.pack(side="right")
tk.Label(info_frame, text="Línea BBVA: (55) 5226 2663", font=FONT_TEXTO_MENUDO, fg=COLOR_TEXTO_SECUNDARIO, bg=COLOR_FONDO_CORTINA).pack(anchor="e")
tk.Label(info_frame, text="Cajero: 1234", font=FONT_TEXTO_MENUDO, fg=COLOR_TEXTO_SECUNDARIO, bg=COLOR_FONDO_CORTINA).pack(anchor="e")

tk.Frame(display_cajero, height=2, bg=COLOR_TEXTO_SECUNDARIO).pack(fill="x", padx=40, pady=10)

# --- Área de Contenido Dinámico ---
area_contenido = tk.Frame(display_cajero, bg=COLOR_FONDO_CORTINA)
area_contenido.pack(expand=True, fill="both")

CargarPantallaInicio()

ventana.mainloop()