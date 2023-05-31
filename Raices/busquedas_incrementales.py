import math
from tkinter import *

from tabla import tabla


def busquedas(f, x0, h, Nmax, root, operaciones, atras):
    xAnterior = x0
    fAnterior = eval(f, operaciones, {'x': xAnterior})
    xActual = xAnterior + h
    fActual = eval(f, operaciones, {'x': xActual})
    cont = 0
    for i in range(1, Nmax):
        if fActual*fAnterior < 0:
            break
        xAnterior = xActual
        fAnterior = fActual
        xActual = xAnterior + h
        fActual = eval(f, operaciones, {'x': xActual})
        cont += 1

    lista = [xAnterior, xActual, h]

    return lista
