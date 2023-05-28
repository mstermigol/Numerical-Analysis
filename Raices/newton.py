import tabulate


def newton_lambda(f, derivada, xo, tol, Nmax):
    resultados = []
    xAnterior = xo
    fAnterior = f(xAnterior)
    E = 1000
    cont = 0
    resultados.append([cont, xAnterior, fAnterior, "N/A"])
    derivadaAnterior = derivada(xAnterior)
    while E > tol and cont < Nmax and derivadaAnterior != 0:
        xActual = xAnterior - fAnterior/derivadaAnterior
        fActual = f(xActual)
        E = abs(xActual-xAnterior)
        cont += 1
        xAnterior = xActual
        fAnterior = fActual
        derivadaAnterior = derivada(xAnterior)

        resultados.append([cont, xAnterior, fAnterior, E])

    print(tabulate.tabulate(resultados, headers=[
        "Iteracion", "Valor de x", "f(x)", "Error"], tablefmt="fancy_grid"))
