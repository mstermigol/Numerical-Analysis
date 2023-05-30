import numpy as np
from tkinter import *


def vandermonde(x, y, puntos, root, atras):
    for widget in root.winfo_children():
        if widget != atras:
            widget.destroy()
    atras.grid_forget()

    x = x.split(",")
    y = y.split(",")
    puntos = puntos.split(",")
    for i in range(len(x)):
        x[i] = float(x[i])
        y[i] = float(y[i])
    for i in range(len(puntos)):
        puntos[i] = float(puntos[i])

    puntos = puntos.split(", ")
    puntos = [float(i) for i in puntos]

    N = len(x)
    A = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if j == 0:
                A[i, j] = 1
            else:
                A[i, j] = x[i]**j

    coeficientes = np.dot(np.linalg.inv(A), y)

    polinomio = ""
    for i in range(N):
        if i == 0:
            polinomio += str(coeficientes[i])
        else:
            polinomio += " + " + str(coeficientes[i]) + "x^" + str(i)

    label = Label(root, text="Polinomio: " + polinomio)
    label.grid()

    for i in range(len(puntos)):
        resultado = 0
        for j in range(N):
            resultado += coeficientes[j] * (puntos[i]**j)
        label = Label(
            root, text="f(" + str(puntos[i]) + ") = " + str(resultado))
        label.grid()

    atras.grid()


x = [-1, 0, 1, 2]
y = [2.3, -1.2, 4.5, 3.3]
