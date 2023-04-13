import math
import tabulate as tabulate


def biseccion(f, a, b, tol, Nmax):
    resultados = []
    fa = f(a)
    fb = f(b)
    valorMedio = (a+b)/2
    fValorMedio = f(valorMedio)
    E = abs(a-valorMedio)
    e = E/valorMedio
    resultados.append([0, a, fa, valorMedio, fValorMedio, b, fb, E, e])
    cont = 1

    while E > tol and cont < Nmax:
        if fa*fValorMedio < 0:
            b = valorMedio
        else:
            a = valorMedio
        fa = f(a)
        fb = f(b)
        p0 = valorMedio
        valorMedio = (a+b)/2
        fValorMedio = f(valorMedio)
        E = abs(valorMedio-p0)
        e = E/valorMedio
        resultados.append([cont, a, fa, valorMedio, fValorMedio, b, fb, E, e])
        cont += 1

    print(tabulate.tabulate(resultados, headers=[
        "Iteracion", "a", "f(a)", "valor medio", "fValorMedio", "b", "fb", "E", "e"], tablefmt="fancy_grid"))


def numero_de_iteraciones(a, b, E):
    k = (math.log(b-a, 10)-math.log(E, 10))/(math.log(2, 10))
    return math.ceil(k)
