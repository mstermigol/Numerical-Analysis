import tabulate as tabulate
from tabla import tabla
from tkinter import *


def punto_fijo(g, xo, tol, Nmax,  root, operaciones, error, atras):
    if error == "Error absoluto":
        punto_fijo_absoluto(g, xo, tol, Nmax, root, operaciones, atras)
    else:
        punto_fijo_relativo(g, xo, tol, Nmax, root, operaciones, atras)


def punto_fijo_absoluto(g, xo, tol, Nmax, root, operaciones, atras):
    resultados = []
    xAnterior = xo
    gxAnterior = eval(g, operaciones, {'x': xAnterior})
    E = 1000
    resultados.append([0, xo, "N/A"])
    cont = 0

    while E >= tol and cont < Nmax:
        xActual = gxAnterior
        E = abs(xActual-xAnterior)
        cont += 1
        resultados.append([cont, xActual, E])
        xAnterior = xActual
        gxAnterior = eval(g, operaciones, {'x': xAnterior})

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
    e.insert(END, "Error absoluto")

    t = tabla(resultados, root, atras)


def punto_fijo_relativo(g, xo, tol, Nmax, root, operaciones, atras):
    resultados = []
    xAnterior = xo
    gxAnterior = eval(g, operaciones, {'x': xAnterior})
    e = 1000
    resultados.append([0, xo, "N/A"])
    cont = 0

    while abs(e) >= tol and cont < Nmax:
        xActual = gxAnterior
        E = abs(xActual-xAnterior)
        e = E / xActual
        cont += 1
        resultados.append([cont, xActual, e])
        xAnterior = xActual
        gxAnterior = eval(g, operaciones, {'x': xAnterior})

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
    e.insert(END, "Error relativo")

    t = tabla(resultados, root, atras)
