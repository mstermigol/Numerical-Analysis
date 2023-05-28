import tabulate


def regla_falsa(f, a, b, tol, Nmax):
    resultados = []
    fa = f(a)
    fb = f(b)
    puntoMedio = (fb*a-fa*b)/(fb-fa)
    fPuntoMedio = f(puntoMedio)
    E = 1000
    cont = 1
    resultados.append([0, a, fa, puntoMedio, fPuntoMedio, b, fb, "N/A"])

    while E > tol and cont < Nmax:
        if fa*fPuntoMedio < 0:
            b = puntoMedio
        else:
            a = puntoMedio
        p0 = puntoMedio
        puntoMedio = (f(b)*a-f(a)*b)/(f(b)-f(a))
        fPuntoMedio = f(puntoMedio)
        E = abs(puntoMedio-p0)
        resultados.append([cont, a, fa, b, fb, puntoMedio, fPuntoMedio, cont])
        cont = cont+1

    print(tabulate.tabulate(resultados, headers=[
        "Iteracion", "a", "f(a)", "pm", "f(pm)", "b", "f(b)", "Error"], tablefmt="fancy_grid"))
