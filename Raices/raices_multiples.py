import tabulate
from tabla import tabla
from tkinter import *

def raices_multiples(f, primeraDerivada, segundaDerivada, xo, tol, Nmax,  root, operaciones, error, atras):
    if error == "Error absoluto":
        raices_multiples_absoluto(f, primeraDerivada, segundaDerivada, xo, tol, Nmax,  root, operaciones, atras)
    else:
        raices_multiples_relativo(f, primeraDerivada, segundaDerivada, xo, tol, Nmax,  root, operaciones, atras)
 
def raices_multiples_absoluto(f, primeraDerivada, segundaDerivada, xo, tol, Nmax,  root, operaciones, atras):
    resultados = []
    xAnterior = xo
    fAnterior = eval(f, operaciones, {'x': xAnterior})
    E = 1000
    cont = 0
    resultados.append([cont, xAnterior, fAnterior, "N/A"])
    primeraDerivadaAnterior = eval(primeraDerivada, operaciones, {'x': xAnterior})
    segundaDerivadaAnterior = eval(segundaDerivada, operaciones, {'x': xAnterior})

    while E > tol and cont < Nmax:
        xActual = xAnterior-fAnterior*(primeraDerivadaAnterior/(
            (primeraDerivadaAnterior)**2-fAnterior*segundaDerivadaAnterior))
        fActual = eval(f, operaciones, {'x': xActual})
        E = abs(xActual-xAnterior)
        cont += 1
        xAnterior = xActual
        fAnterior = fActual
        resultados.append([cont, xAnterior, fAnterior, E])

    for widget in root.winfo_children():
        if widget != atras:
            widget.destroy()

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=0)
    e.insert(END, "Iteracion")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=1)
    e.insert(END, "Valor de x")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=2)
    e.insert(END, "f(x)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=3)
    e.insert(END, "Error absoluto")

    t = tabla(resultados, root, atras)

def raices_multiples_relativo(f, primeraDerivada, segundaDerivada, xo, tol, Nmax,  root, operaciones, atras):
    resultados = []
    xAnterior = xo
    fAnterior = eval(f, operaciones, {'x': xAnterior})
    E = 1000
    cont = 0
    resultados.append([cont, xAnterior, fAnterior, "N/A"])
    primeraDerivadaAnterior = eval(primeraDerivada, operaciones, {'x': xAnterior})
    segundaDerivadaAnterior = eval(segundaDerivada, operaciones, {'x': xAnterior})

    while E > tol and cont < Nmax:
        xActual = xAnterior-fAnterior*(primeraDerivadaAnterior/(
            (primeraDerivadaAnterior)**2-fAnterior*segundaDerivadaAnterior))
        fActual = eval(f, operaciones, {'x': xActual})
        E = abs(xActual-xAnterior)
        e = E/xActual
        cont += 1
        xAnterior = xActual
        fAnterior = fActual
        resultados.append([cont, xAnterior, fAnterior, E])

    for widget in root.winfo_children():
        if widget != atras:
            widget.destroy()

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=0)
    e.insert(END, "Iteracion")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=1)
    e.insert(END, "Valor de x")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=2)
    e.insert(END, "f(x)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=3)
    e.insert(END, "Error relativo")

    t = tabla(resultados, root, atras)