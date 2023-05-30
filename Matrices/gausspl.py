import numpy as np
from Matrices.sustregr import sustregrM
from tkinter import *
from tabla import tabla

def gausspl(a, b, c, d, root, atras):
    a = a.split(",")
    b = b.split(",")
    c = c.split(",")
    d = d.split(",")
    for i in range(len(a)):
        a[i] = float(a[i])
        b[i] = float(b[i])
        c[i] = float(c[i])
        d[i] = float(d[i])
    A = np.array([a, 
                 b,
                 c])
    b = np.array(d)
    n = np.size(A, 0)
    M = np.hstack((A, b.reshape(-1, 1)))
    contador = 1
    for i in range(n-1):
        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] = M[j, i:n+1] - (M[j, i]/M[i, i])*M[i, i:n+1]
            print(f"Paso {contador}:")
            print(M)
            contador += 1
    print("")
    print("Resultado:")
    x = sustregrM(M)
    lista =  [[x[0], x[1], x[2]]]
    for widget in root.winfo_children():
        if widget != atras:
            widget.destroy()

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=0)
    e.insert(END, "x1")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=1)
    e.insert(END, "x2")

    e = Entry(root, width=20, fg='Blue', font=('Arial', 10))
    e.grid(row=0, column=2)
    e.insert(END, "x3")

    t = tabla(lista, root, atras)



