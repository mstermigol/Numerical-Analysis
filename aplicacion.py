import tkinter as tk
from seleccion_metodos import definirMetodo

root = tk.Tk()

root.geometry("1500x700")
root.title("Metodos numéricos")

label = tk.Label(root, text="Metodos numéricos", font=("Arial", 20))
label.grid()


opcionesMetodos = [
    "Bisección",
    "Busqueda incremental",
    "Newton",
    "Punto fijo",
    "Raices multiples",
    "Secante",
    "Regla falsa",
    "Cholesky",
    "Crout",
    "Doolittle",
    "Gauss simple",
    "Gauss con pivoteo parcial",
    "Gauss con pivoteo total",
    "Gauss-Seidel",
    "Jacobi",
    "LU parcial",
    "LU simple",
    "LaGrange",
    "Newton",
    "Spline",
    "Vandermonde"
]


# Se crean los menus desplegables para cada metodo
clickedMetodos = tk.StringVar()
clickedMetodos.set(opcionesMetodos[0])
dropDownMetodos = tk.OptionMenu(root, clickedMetodos, *opcionesMetodos)
dropDownMetodos.grid(sticky="")
root.grid_columnconfigure(0, weight=1)


siguiente = tk.Button(root, text="Siguiente",
                      command=lambda: definirMetodo(root, clickedMetodos.get()))
siguiente.grid()

root.mainloop()
