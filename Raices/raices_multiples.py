import tabulate


def raices_multiples(f, primeraDerivada, segundaDerivada, xo, tol, Nmax):

    resultados = []
    xAnterior = xo
    fAnterior = f(xAnterior)
    E = 1000
    cont = 0
    resultados.append([cont, xAnterior, fAnterior, "N/A"])

    while E > tol and cont < Nmax:
        xActual = xAnterior-fAnterior*(primeraDerivada(xAnterior)/(
            (primeraDerivada(xAnterior))**2-fAnterior*segundaDerivada(xAnterior)))
        fActual = f(xActual)
        E = abs(xActual-xAnterior)
        cont += 1
        xAnterior = xActual
        fAnterior = fActual
        resultados.append([cont, xAnterior, fAnterior, E])

    print(tabulate.tabulate(resultados, headers=[
        "Iteracion", "Valor de x", "f(x)", "Error"], tablefmt="fancy_grid"))
