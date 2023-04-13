import tabulate as tabulate


def punto_fijo(g, xo, tol, Nmax):
    resultados = []
    xAnterior = xo
    E = 1000
    resultados.append([0, xo, "N/A"])
    cont = 0

    while E >= tol and cont < Nmax:
        xActual = g(xAnterior)
        E = abs(xActual-xAnterior)
        cont += 1
        resultados.append([cont, xActual, E])
        xAnterior = xActual

    print(tabulate.tabulate(resultados, headers=[
        "Iteracion", "Valor de x", "Error"], tablefmt="fancy_grid"))
