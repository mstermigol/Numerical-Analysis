import tkinter as tk
from Raices.biseccion import biseccion
from Raices.busquedas_incrementales import busquedas
from math import *

root = tk.Tk()

root.geometry("800x600")
root.title("Metodos numéricos")

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


def inicio(root):
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text="Metodos numéricos", font=("Arial", 20))
    label.grid()

    clickedMetodos = tk.StringVar()
    clickedMetodos.set(opcionesMetodos[0])
    dropDownMetodos = tk.OptionMenu(root, clickedMetodos, *opcionesMetodos)
    dropDownMetodos.grid(sticky="")
    root.grid_columnconfigure(0, weight=1)

    siguiente = tk.Button(root, text="Siguiente",
                          command=lambda: definirMetodo(root, clickedMetodos.get()))
    siguiente.grid()


inicio(root)

operaciones = {"exp": exp, "ln(x)": log, "log(x)": log10,
               "sin(x)": sin, "cos(x)": cos, "tan(x)": tan}

error = ["Error absoluto", "Error relativo"]


def definirMetodo(root, metodo):
    errorSeleccionado = tk.StringVar()
    errorSeleccionado.set(error[0])

    for widget in root.winfo_children():
        widget.destroy()

    if metodo == "Bisección":
        label = tk.Label(root, text="Biseccion", font=("Arial", 20))
        label.grid()

        funcion = tk.Label(root, text="Ingrese la función")
        funcion.grid()
        funcionEntry = tk.Entry(root)
        funcionEntry.grid()

        a = tk.Label(root, text="Ingrese el valor de a")
        a.grid()
        aEntry = tk.Entry(root)
        aEntry.grid()

        b = tk.Label(root, text="Ingrese el valor de b")
        b.grid()
        bEntry = tk.Entry(root)
        bEntry.grid()

        tol = tk.Label(root, text="Ingrese el valor de la tolerancia")
        tol.grid()
        tolEntry = tk.Entry(root)
        tolEntry.grid()

        Nmax = tk.Label(root, text="Ingrese el valor de Nmax")
        Nmax.grid()
        NmaxEntry = tk.Entry(root)
        NmaxEntry.grid()

        dropdown = tk.OptionMenu(root, errorSeleccionado, *error)
        dropdown.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: biseccion(
            funcionEntry.get(), float(aEntry.get()), float(
                bEntry.get()), float(tolEntry.get()),
            int(NmaxEntry.get()), root, operaciones, errorSeleccionado.get(), atras))
        calcular.grid()

    elif metodo == "Busqueda incremental":
        label = tk.Label(root, text="Busqueda incremental", font=("Arial", 20))
        label.grid()

        funcion = tk.Label(root, text="Ingrese la función")
        funcion.grid()
        funcionEntry = tk.Entry(root)
        funcionEntry.grid()

        x0 = tk.Label(root, text="Ingrese el valor de x0")
        x0.grid()
        x0Entry = tk.Entry(root)
        x0Entry.grid()

        h = tk.Label(root, text="Ingrese el valor de h")
        h.grid()
        hEntry = tk.Entry(root)
        hEntry.grid()

        Nmax = tk.Label(root, text="Ingrese el valor de Nmax")
        Nmax.grid()
        NmaxEntry = tk.Entry(root)
        NmaxEntry.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: busquedas(
            funcionEntry.get(), float(x0Entry.get()), float(hEntry.get()), int(NmaxEntry.get()), root, operaciones, atras))
        calcular.grid()

        print("Busqueda incremental")
    elif metodo == "Newton":
        print("Newton")
    elif metodo == "Punto fijo":
        print("Punto fijo")
    elif metodo == "Raices multiples":
        print("Raices multiples")
    elif metodo == "Secante":
        print("Secante")
    elif metodo == "Regla falsa":
        print("Regla falsa")
    elif metodo == "Cholesky":
        print("Cholesky")
    elif metodo == "Crout":
        print("Crout")
    elif metodo == "Doolittle":
        print("Doolittle")
    elif metodo == "Gauss simple":
        print("Gauss simple")
    elif metodo == "Gauss con pivoteo parcial":
        print("Gauss con pivoteo parcial")
    elif metodo == "Gauss con pivoteo total":
        print("Gauss con pivoteo total")
    elif metodo == "Gauss-Seidel":
        print("Gauss-Seidel")
    elif metodo == "Jacobi":
        print("Jacobi")
    elif metodo == "LU parcial":
        print("LU parcial")
    elif metodo == "LU simple":
        print("LU simple")
    elif metodo == "LaGrange":
        print("LaGrange")
    elif metodo == "Newton":
        print("Newton")
    elif metodo == "Spline":
        print("Spline")
    elif metodo == "Vandermonde":
        print("Vandermonde")

    atras = tk.Button(root, text="Atras", command=lambda: inicio(root))
    atras.grid()


root.mainloop()
