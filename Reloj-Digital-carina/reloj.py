import tkinter as tk
from tkinter import font
import time

def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
    etiqueta_reloj.config(text=hora_actual)
    etiqueta_reloj.after(1000, actualizar_reloj)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("300x150")
ventana.configure(bg='white')

# Configuración de la fuente
fuente_reloj = font.Font(family='Helvetica', size=30, weight='bold')

# Crear marco redondo para el reloj
marco_reloj = tk.Canvas(ventana, width=200, height=100, bg="white", highlightthickness=0)
marco_reloj.place(relx=0.5, rely=0.5, anchor="center")
marco_reloj.create_oval(10, 10, 190, 90, outline="pink", width=5)
marco_reloj.create_oval(13, 13, 187, 87, outline="light green", width=5)

# Crear etiqueta para mostrar la hora
etiqueta_reloj = tk.Label(ventana, text="", font=fuente_reloj, fg="black", bg="white")
etiqueta_reloj.place(relx=0.5, rely=0.5, anchor="center")

# Actualizar el reloj
actualizar_reloj()

ventana.mainloop()
