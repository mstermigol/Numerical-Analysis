import tabulate
from tabla import tabla
from tkinter import *


def regla_falsa(f, a, b, tol, Nmax, root, operaciones, error, atras):
    if error == "Error absoluto":
        regla_falsa_absoluto(f, a, b, tol, Nmax, root, operaciones, atras)
    else:
        regla_falsa_relativo(f, a, b, tol, Nmax, root, operaciones, atras)
    
    #resultados = []
    #fa = f(a)
    #fb = f(b)
    #puntoMedio = (fb*a-fa*b)/(fb-fa)
    #fPuntoMedio = f(puntoMedio)
    #E = 1000
    #cont = 1
    #resultados.append([0, a, fa, puntoMedio, fPuntoMedio, b, fb, "N/A"])

    #while E > tol and cont < Nmax:
        #if fa*fPuntoMedio < 0:
            #b = puntoMedio
        #else:
            #a = puntoMedio
        #p0 = puntoMedio
        #puntoMedio = (f(b)*a-f(a)*b)/(f(b)-f(a))
        #fPuntoMedio = f(puntoMedio)
        #E = abs(puntoMedio-p0)
        #resultados.append([cont, a, fa, b, fb, puntoMedio, fPuntoMedio, cont])
        #cont = cont+1

    #print(tabulate.tabulate(resultados, headers=[
        #"Iteracion", "a", "f(a)", "pm", "f(pm)", "b", "f(b)", "Error"], tablefmt="fancy_grid"))

def regla_falsa_absoluto(f, x0, x1, tol, Nmax, root, operaciones, atras):
    resultados = []
    fa = eval(f, operaciones, {'x': a})
    fb = eval(f, operaciones, {'x': b})
    puntoMedio = (fb*a-fa*b)/(fb-fa)
    fPuntoMedio = eval(f, operaciones, {'x': puntoMedio})
    E = 1000
    cont = 1
    resultados.append([0, a, fa, puntoMedio, fPuntoMedio, b, fb, "N/A"])

    while E > tol and cont < Nmax:
        if fa*fPuntoMedio < 0:
            b = puntoMedio
        else:
            a = puntoMedio
        fa = eval(f, operaciones, {'x': a})
        fb = eval(f, operaciones, {'x': b})
        p0 = puntoMedio
        puntoMedio = (fb*a-fa*b)/(fb-fa)
        fPuntoMedio = eval(f, operaciones, {'x': puntoMedio})
        E = abs(puntoMedio-p0)
        resultados.append([cont, a, fa, puntoMedio, fPuntoMedio, b, fb, E])
        cont = cont+1
    
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
    e.insert(END, "pm")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=4)
    e.insert(END, "f(pm)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=5)
    e.insert(END, "b")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=6)
    e.insert(END, "f(b)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=7)
    e.insert(END, "Error absoluto")

    t = tabla(resultados, root, atras)

def regla_falsa_relativo(f, x0, x1, tol, Nmax, root, operaciones, atras):
    resultados = []
    fa = eval(f, operaciones, {'x': a})
    fb = eval(f, operaciones, {'x': b})
    puntoMedio = (fb*a-fa*b)/(fb-fa)
    fPuntoMedio = eval(f, operaciones, {'x': puntoMedio})
    E = 1000
    e = E/puntoMedio
    cont = 1
    resultados.append([0, a, fa, puntoMedio, fPuntoMedio, b, fb, "N/A"])

    while abs(e) > tol and cont < Nmax:
        if fa*fPuntoMedio < 0:
            b = puntoMedio
        else:
            a = puntoMedio
        fa = eval(f, operaciones, {'x': a})
        fb = eval(f, operaciones, {'x': b})
        p0 = puntoMedio
        puntoMedio = (fb*a-fa*b)/(fb-fa)
        fPuntoMedio = eval(f, operaciones, {'x': puntoMedio})
        E = abs(puntoMedio-p0)
        e = E/puntoMedio
        resultados.append([cont, a, fa, puntoMedio, fPuntoMedio, b, fb, e])
        cont = cont+1
    
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
    e.insert(END, "pm")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=4)
    e.insert(END, "f(pm)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=5)
    e.insert(END, "b")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=6)
    e.insert(END, "f(b)")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=7)
    e.insert(END, "Error relativo")

    t = tabla(resultados, root, atras)