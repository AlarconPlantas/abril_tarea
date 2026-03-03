import tkinter as tk
from tkinter import messagebox

def calcular_hora_invertida():
    try:
        # Leer la hora desde el Entry
        hora = entrada.get()
        h, m = map(int, hora.split(":"))
        
        # Calcular minutos totales e invertidos
        total = h*60 + m
        invertido = 720 - total
        horas_inv = invertido // 60
        minutos_inv = invertido % 60
        
        # Mostrar resultado en la etiqueta
        resultado.config(text=f"Hora invertida: {int(horas_inv)}:{int(minutos_inv):02d}")
    except:
        # Mensaje de error si el formato es incorrecto
        messagebox.showerror("Error", "Ingrese la hora en formato HH:MM")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Hora Invertida")
ventana.geometry("300x150")

# Etiqueta instrucción
tk.Label(ventana, text="Ingrese la hora (HH:MM):").pack(pady=5)

# Campo de entrada
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botón para calcular
tk.Button(ventana, text="Calcular hora invertida", command=calcular_hora_invertida).pack(pady=5)

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=5)

# Iniciar la ventana
ventana.mainloop()
