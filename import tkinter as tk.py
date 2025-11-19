import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Ventana de Tkinter")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Agregar un label (etiqueta) dentro de la ventana
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!", font=("Arial", 14))
etiqueta.pack(pady=20)

# Agregar un botón que cierre la ventana
boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.quit)
boton_cerrar.pack(pady=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
