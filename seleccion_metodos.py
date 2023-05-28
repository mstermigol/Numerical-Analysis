import tkinter as tk
from Raices.biseccion import biseccion
from math import *

operaciones = {"exp": exp, "ln(x)": log, "log(x)": log10,
               "sin(x)": sin, "cos(x)": cos, "tan(x)": tan}


def definirMetodo(root, metodo):
    if metodo == "Bisección":
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
        """
        calcular = tk.Button(root, text="Calcular", command=lambda: biseccion("funcionEntry.get()", float(
            aEntry.get()), float(bEntry.get()), float(tolEntry.get()), int(NmaxEntry.get()), root,
            operaciones))"""
        calcular = tk.Button(root, text="Calcular", command=lambda: biseccion(
            "exp(x)-2", 0, 2, 0.0001, 100, root, operaciones))
        calcular.grid()
