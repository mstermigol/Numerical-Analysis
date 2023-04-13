import math


def busquedas(f, x0, h, Nmax):
    xAnterior = x0
    fAnterior = f(xAnterior)
    xActual = xAnterior + h
    fActual = f(xActual)
    cont = 0
    for i in range(1, Nmax):
        if fActual*fAnterior < 0:
            break
        xAnterior = xActual
        fAnterior = fActual
        xActual = xAnterior + h
        fActual = f(xActual)
        cont += 1

    return ([xAnterior, xActual], cont)
