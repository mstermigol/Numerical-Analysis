from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from matplotlib.figure import Figure
import math
import tabulate as tabulate
from tabla import tabla
from tkinter import *
import matplotlib

matplotlib.use('TkAgg')


def biseccion(f, a, b, tol, Nmax, root, operaciones, error, atras):
    if error == "Error absoluto":
        biseccionAbsoluto(f, a, b, tol, Nmax, root, operaciones, atras)
    else:
        biseccionRelativo(f, a, b, tol, Nmax, root, operaciones, atras)


def biseccionRelativo(f, a, b, tol, Nmax, root, operaciones, atras):
    resultados = []
    fa = eval(f, operaciones, {'x': a})
    fb = eval(f, operaciones, {'x': b})
    valorMedio = (a + b) / 2
    fValorMedio = eval(f, operaciones, {'x': valorMedio})
    E = abs(a - valorMedio)
    e = E / valorMedio
    resultados.append([0, a, fa, valorMedio, fValorMedio, b, fb, e])
    cont = 1

    while abs(e) > tol and cont < Nmax:
        if fa * fValorMedio < 0:
            b = valorMedio
        else:
            a = valorMedio
        fa = eval(f, operaciones, {'x': a})
        fb = eval(f, operaciones, {'x': b})
        p0 = valorMedio
        valorMedio = (a + b) / 2
        fValorMedio = eval(f, operaciones, {'x': valorMedio})
        E = abs(valorMedio - p0)
        e = E / valorMedio
        resultados.append([cont, a, fa, valorMedio, fValorMedio, b, fb, e])
        cont += 1

    for widget in root.winfo_children():
        if widget != atras:
            widget.destroy()

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=0)
    e.insert(END, "Iteración")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=1)
    e.insert(END, "a")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=2)
    e.insert(END, "f(a)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=3)
    e.insert(END, "p")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=4)
    e.insert(END, "f(p)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=5)
    e.insert(END, "b")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=6)
    e.insert(END, "f(b)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=7)
    e.insert(END, "e")

    t = tabla(resultados, root, atras)

    graficoError = Figure(figsize=(5, 4), dpi=100)

    canva_error = FigureCanvasTkAgg(graficoError, master=root)
    canva_error.draw()

    axes = graficoError.add_subplot()

    axes.bar(range(len(resultados)), [row[7]
             for row in resultados], color='red')
    axes.set_title("Error relativo")
    axes.set_xlabel("Iteraciones")
    axes.set_ylabel("Error relativo")

    canva_error.get_tk_widget().grid()


def biseccionAbsoluto(f, a, b, tol, Nmax, root, operaciones, atras):
    resultados = []
    fa = eval(f, operaciones, {'x': a})
    fb = eval(f, operaciones, {'x': b})
    valorMedio = (a + b) / 2
    fValorMedio = eval(f, operaciones, {'x': valorMedio})
    E = abs(a - valorMedio)
    resultados.append([0, a, fa, valorMedio, fValorMedio, b, fb, E])
    cont = 1

    while E > tol and cont < Nmax:
        if fa * fValorMedio < 0:
            b = valorMedio
        else:
            a = valorMedio
        fa = eval(f, operaciones, {'x': a})
        fb = eval(f, operaciones, {'x': b})
        p0 = valorMedio
        valorMedio = (a + b) / 2
        fValorMedio = eval(f, operaciones, {'x': valorMedio})
        E = abs(valorMedio - p0)
        resultados.append([cont, a, fa, valorMedio, fValorMedio, b, fb, E])
        cont += 1

    for widget in root.winfo_children():
        if widget != atras:
            widget.destroy()

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=0)
    e.insert(END, "Iteración")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=1)
    e.insert(END, "a")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=2)
    e.insert(END, "f(a)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=3)
    e.insert(END, "p")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=4)
    e.insert(END, "f(p)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=5)
    e.insert(END, "b")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=6)
    e.insert(END, "f(b)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=7)
    e.insert(END, "E")

    t = tabla(resultados, root, atras)

    graficoError = Figure(figsize=(5, 4), dpi=100)

    canva_error = FigureCanvasTkAgg(graficoError, master=root)
    canva_error.draw()

    axes = graficoError.add_subplot()

    axes.bar(range(len(resultados)), [row[7]
             for row in resultados], color='red')
    axes.set_title("Error absoluto")
    axes.set_xlabel("Iteraciones")
    axes.set_ylabel("Error absoluto")

    canva_error.get_tk_widget().grid()


def numero_de_iteraciones(a, b, E):
    k = (math.log(b-a, 10)-math.log(E, 10))/(math.log(2, 10))
    return math.ceil(k)
