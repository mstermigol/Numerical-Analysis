import sympy as sp
import numpy as np


def newton(x, y, puntos):
    xs = sp.symbols('x')

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

    print("\n Tabla de diferencias divididas: ")
    matriz = np.array(a)
    matriz_t = np.transpose(matriz)
    print(matriz_t)

    p = 0
    w = 0
    for i in range(len(a[0])):
        terminos = 1
        for j in range(w):
            terminos *= (xs-a[0][j])
        p += a[i+1][0]*terminos
        w += 1
        pol = sp.simplify(p)

    print("\nPolinomio de Newton: ")
    print(pol)

    for punto in puntos:
        print(f"\nValor de x = {punto}: {pol.subs(xs, punto)}")


x = [-1, 0, 1, 2]
y = [1, 2, -1, 10]

newton(x, y, [1.5])
