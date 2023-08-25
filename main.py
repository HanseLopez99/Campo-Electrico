import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Functions as f

# Variables globales
canvas = None

# Ventana principal
root = tk.Tk()
root.title("Campo Eléctrico")

# Crear un frame para los controles
control_frame = ttk.LabelFrame(root, text="Configuración")
control_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Dropdown para elegir la distribución
distribution_label = ttk.Label(control_frame, text="Distribución:")
distribution_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
distributions = ["Anillo", "Linea finíta", "Disco"]
distribution_var = tk.StringVar()
distribution_dropdown = ttk.Combobox(control_frame, textvariable=distribution_var, values=distributions)
distribution_dropdown.grid(row=0, column=1, padx=5, pady=5)
distribution_dropdown.current(0)

# Función para actualizar la etiqueta de un deslizador
def update_label(label, slider):
    label.config(text=f"{slider.get():.2f}")

# Etiqueta para mostrar el valor del radio
radio_value_label = ttk.Label(control_frame, text="")
radio_value_label.grid(row=1, column=2, padx=5)

# Etiqueta para mostrar la distancia en X
x_distance_value_label = ttk.Label(control_frame, text="")
x_distance_value_label.grid(row=2, column=2, padx=5)

# Slider para configurar el radio
radio_label = ttk.Label(control_frame, text="Radio (m):")
radio_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
radio_slider = ttk.Scale(control_frame, from_=0.1, to=10.0, orient=tk.HORIZONTAL, command=lambda e: update_label(radio_value_label, radio_slider))
radio_slider.grid(row=1, column=1, padx=5, pady=5)
radio_slider.set(1)

# Slider para configurar la distancia en X
x_distance_label = ttk.Label(control_frame, text="Distancia en X (m):")
x_distance_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
x_distance_slider = ttk.Scale(control_frame, from_=0.1, to=10.0, orient=tk.HORIZONTAL, command=lambda e: update_label(x_distance_value_label, x_distance_slider))
x_distance_slider.grid(row=2, column=1, padx=5, pady=5)
x_distance_slider.set(2)

# Ahora que ambos deslizadores están definidos, podemos actualizar las etiquetas.
update_label(radio_value_label, radio_slider)
update_label(x_distance_value_label, x_distance_slider)


# Función para generar el gráfico
def plot_graph():
    global canvas  # Hacer referencia al canvas global
    
    # Destruir el canvas anterior si existe
    if canvas:
        canvas.get_tk_widget().destroy()

    distribution = distribution_var.get()
    radio = radio_slider.get()
    x_distance = x_distance_slider.get()
    
    if distribution == "Anillo":
        E = float(f.electric_field_ring(radio, x_distance))
    elif distribution == "Linea finíta":
        E = float(f.electric_field_line(radio, x_distance))
    else:  # "Disco"
        E = float(f.electric_field_disk(radio, x_distance))
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Dibujar la distribución de carga
    if distribution == "Anillo":
        circle = plt.Circle((0, 0), radio, color='r', fill=False)
        ax.add_artist(circle)
    elif distribution == "Linea finíta":
        ax.plot([0, 0], [-radio / 2, radio / 2], 'r-')
    else:  # "Disco":
        circle = plt.Circle((0, 0), radio, color='r', fill=True)
        ax.add_artist(circle)
    
    # Dibujar el punto P
    ax.plot(x_distance, 0, 'bo')  # Punto azul en la distancia x_distance y y=0
    
    # Dibujar la flecha indicando el campo eléctrico
    direction = 1 if x_distance > 0 else -1  # Si el punto P está a la derecha de la distribución, la dirección es hacia la derecha. De lo contrario, es hacia la izquierda.
    ax.arrow(x_distance, 0, direction * 0.5, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
    
    # Configurar el gráfico
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Campo Eléctrico (N/C)")
    ax.set_title(f"Campo Eléctrico: {E:.3f} N/C")
    
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
    canvas.draw()

# Botón para generar el gráfico
plot_button = ttk.Button(root, text="Generar Gráfico", command=plot_graph)
plot_button.pack(pady=20)

root.mainloop()
