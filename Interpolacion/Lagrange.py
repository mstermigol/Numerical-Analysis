import numpy as np
from tkinter import *


def lagrange(x, y, punto, root, atras):
    x = x.split(",")
    y = y.split(",")
    for i in range(len(x)):
        x[i] = float(x[i])
        y[i] = float(y[i])
    punto = float(punto)

    for widget in root.winfo_children():
        if widget != atras:
            widget.destroy()
    atras.grid_forget()
    n = np.size(x)
    p = 0
    for i in range(n):
        L = y[i]
        for j in range(n):
            if i != j:
                L = L*(punto-x[j])/(x[i]-x[j])
        p = p+L

    titulo = Label(root, text="Interpolación de Lagrange", font=("Arial", 20))

    label = Label(root, text="El valor de la interpolación es: " + str(p))
    label.grid()

    atras.grid()


x = [-1, 0, 1, 2]
y = [2.3, -1.2, 4.5, 3.3]

# print(lagrange(x, y, 0.5))
