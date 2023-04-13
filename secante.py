import math
import tabulate as tabulate


def secante(f, x0, x1, tol, Nmax):
    resultados = []
    f0 = f(x0)
    resultados.append([0, x0, f0, "N/A"])
    f1 = f(x1)
    E = abs(x1-x0)
    cont = 1
    resultados.append([cont, x1, f1, E])

    while E > tol and cont < Nmax:
        xActual = x1 - (f(x1) * (x1-x0)) / (f(x1)-f(x0))
        fActual = f(xActual)
        E = abs(xActual-x1)
        cont = cont + 1
        x0 = x1
        f0 = f1
        x1 = xActual
        f1 = fActual
        resultados.append([cont, x1, f1, E])

    print(tabulate.tabulate(resultados, headers=[
        "Iteracion", "Valor de x", "Valor eval f(x)", "Error abs"], tablefmt="fancy_grid"))


def ojo_de_halcon():  # Parcial 2 2019-2
    x = 14.2
    y = 1.8
    g = 6.4
    vo = 25.4
    tol = 10**-5
    def f(teta): return y - (x * math.tan(teta) -
                             ((g*x**2)/(2*vo**2*math.cos(teta)**2)))

    secante(f, 0, 1, tol, 1000)


# ojo_de_halcon()

def Dolan():  # Parcial 2 2021-1
    a = -1
    b = -1.5
    tol = 1e-5
    def f(x): return x**3-x**2-2*x+2+math.sin(x-1)
    secante(f, a, b, tol, 1000)


# Dolan()

def fuerza():  # Parcial 2021-1 grupo 2
    F = 10000
    tol = 1e-4
    def f(d): return d - (3*d/math.sqrt(d**2+9)) - F/1000
    secante(f, 1, 2, tol, 1000)


fuerza()
