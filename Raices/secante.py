import math
import tabulate as tabulate
from tabla import tabla
from tkinter import *

def secante(f, x0, x1, tol, Nmax, root, operaciones, error, atras):
    if error == "Error absoluto":
        secante_absoluto(f, x0, x1, tol, Nmax, root, operaciones, atras)
    else:
        secante_relativo(f, x0, x1, tol, Nmax, root, operaciones, atras)

def secante_absoluto(f, x0, x1, tol, Nmax, root, operaciones, atras):
    resultados = []
    f0 = eval(f, operaciones, {'x': x0})
    resultados.append([0, x0, f0, "N/A"])
    f1 = eval(f, operaciones, {'x': x1})
    E = abs(x1-x0)
    cont = 1
    resultados.append([cont, x1, f1, E])

    while E > tol and cont < Nmax:
        xActual = x1 - (f1 * (x1-x0)) / (f1-f0)
        fActual = eval(f, operaciones, {'x': xActual})
        E = abs(xActual-x1)
        cont = cont + 1
        x0 = x1
        f0 = f1
        x1 = xActual
        f1 = fActual
        resultados.append([cont, x1, f1, E])

    for widget in root.winfo_children():
        if widget != atras:
            widget.destroy()

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=0)
    e.insert(END, "Iteración")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=1)
    e.insert(END, "Valor de x")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=2)
    e.insert(END, "Valor de f(x)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=3)
    e.insert(END, "Error absoluto")

    t = tabla(resultados, root, atras)

def secante_relativo(f, x0, x1, tol, Nmax, root, operaciones, atras):
    resultados = []
    f0 = eval(f, operaciones, {'x': x0})
    resultados.append([0, x0, f0, "N/A"])
    f1 = eval(f, operaciones, {'x': x1})
    E = abs(x1-x0)
    e = E /x1
    cont = 1
    resultados.append([cont, x1, f1, e])

    while abs(e) > tol and cont < Nmax:
        xActual = x1 - (f1 * (x1-x0)) / (f1-f0)
        fActual = eval(f, operaciones, {'x': xActual})
        E = abs(xActual-x1)
        e = E/xActual
        cont = cont + 1
        x0 = x1
        f0 = f1
        x1 = xActual
        f1 = fActual
        resultados.append([cont, x1, f1, e])

    for widget in root.winfo_children():
        if widget != atras:
            widget.destroy()

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=0)
    e.insert(END, "Iteración")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=1)
    e.insert(END, "Valor de x")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=2)
    e.insert(END, "Valor de f(x)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=3)
    e.insert(END, "Error relativo")

    t = tabla(resultados, root, atras)