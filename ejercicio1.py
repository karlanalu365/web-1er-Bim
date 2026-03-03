import tkinter as tk
from tkinter import messagebox

def calcular_hora():
    try:
        hora = entrada.get()
        h, m = map(int, hora.split(":"))

        if h < 0 or h > 23 or m < 0 or m > 59:
            raise ValueError

        h = h % 12
        min_real = (60 - m) % 60
        hora_real = (11 - h + (1 if m > 0 else 0)) % 12

        if hora_real == 0:
            hora_real = 12

        resultado.config(
            text=f"🕒 Hora real: {hora_real:02d}:{min_real:02d}",
            fg="#D81B60"
        )

    except:
        messagebox.showerror(
            "Error",
            "Por favor ingresa la hora en formato HH:MM"
        )

ventana = tk.Tk()
ventana.title("Reloj en el Espejo ")
ventana.geometry("380x260")
ventana.resizable(False, False)
ventana.configure(bg="#FCE4EC") 


frame = tk.Frame(ventana, bg="#FCE4EC")
frame.pack(expand=True)


titulo = tk.Label(
    frame,
    text=" Hora reflejada en el espejo",
    font=("Comic Sans MS", 15, "bold"),
    bg="#FCE4EC",
    fg="#880E4F"
)
titulo.pack(pady=10)

texto = tk.Label(
    frame,
    text="Ingresa la hora (formato 24 hrs)",
    font=("Arial", 10),
    bg="#FCE4EC",
    fg="#6A1B9A"
)
texto.pack()

entrada = tk.Entry(
    frame,
    font=("Arial", 14),
    justify="center",
    bd=2,
    relief="solid"
)
entrada.pack(pady=8)

boton = tk.Button(
    frame,
    text="💖 Calcular Hora Real 💖",
    font=("Arial", 11, "bold"),
    bg="#EC407A",
    fg="white",
    activebackground="#F06292",
    activeforeground="white",
    bd=0,
    padx=15,
    pady=6,
    command=calcular_hora
)
boton.pack(pady=10)

resultado = tk.Label(
    frame,
    text="",
    font=("Arial", 13, "bold"),
    bg="#FCE4EC",
    fg="#AD1457"
)
resultado.pack(pady=10)

# ---------------- EJECUCIÓN ----------------

ventana.mainloop()
