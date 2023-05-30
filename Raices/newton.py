import tabulate
from tkinter import *
from tabla import tabla

def newton_lambda(f, derivada, xo, tol, Nmax, root, operaciones, atras):
    resultados = []
    xAnterior = xo
    fAnterior = eval(f, operaciones, {'x': xAnterior})
    E = 1000
    cont = 0
    resultados.append([cont, xAnterior, fAnterior, "N/A"])
    derivadaAnterior = eval(derivada, operaciones, {'x': xAnterior})
    while E > tol and cont < Nmax and derivadaAnterior != 0:
        xActual = xAnterior - fAnterior/derivadaAnterior
        fActual = eval(f, operaciones, {'x': xActual})
        E = abs(xActual-xAnterior)
        cont += 1
        xAnterior = xActual
        fAnterior = fActual
        derivadaAnterior = eval(derivada, operaciones, {'x': xAnterior})   

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
    e.insert(END, "Error")

    t = tabla(resultados, root, atras)

    #print(tabulate.tabulate(resultados, headers=[
    #    "Iteracion", "Valor de x", "f(x)", "Error"], tablefmt="fancy_grid"))
    
