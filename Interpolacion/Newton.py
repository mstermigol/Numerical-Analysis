import sympy as sp
import numpy as np
from tkinter import *
#from PIL import ImageTk, Image


def newtonInterpolacion(x, y, puntos, root, atras):
    for widget in root.winfo_children():
        if widget != atras:
            widget.destroy()
    atras.grid_forget()

    label = Label(root, text="Interpolación de Newton", font=("Arial", 20))

    xs = sp.symbols('x')
    x = x.split(",")
    y = y.split(",")
    puntos = puntos.split(",")
    for i in range(len(x)):
        x[i] = float(x[i])
        y[i] = float(y[i])
    for i in range(len(puntos)):
        puntos[i] = float(puntos[i])

    a = []
    for i in range(len(x)+1):
        aux = []
        for j in range(len(x)):
            aux.append(0)
        a.append(aux)

    for i in range(len(x)):
        a[0][i] = (x[i])
        a[1][i] = (y[i])

    b = 1
    c = 1
    d = 1

    for i in range(len(a[0])):
        for j in range(len(a[0])-b):
            a[c+1][j] = (a[c][j+1]-a[c][j])/(a[0][j+d]-a[0][j])
        b += 1
        c += 1
        d += 1

    p = 0
    w = 0
    for i in range(len(a[0])):
        terminos = 1
        for j in range(w):
            terminos *= (xs-a[0][j])
        p += a[i+1][0]*terminos
        w += 1
        pol = sp.simplify(p)

    polinomio = Label(root, text="Polinomio: " + str(pol))
    polinomio.grid()

    for punto in puntos:
        label = Label(root, text="P(" + str(punto) + ") = " +
                      str(pol.subs(xs, punto)))
        label.grid()

    atras.grid()


x = [-1, 0, 1, 2]
y = [1, 2, -1, 10]
