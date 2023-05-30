import numpy as np


def jacobi(A, b, x0, tol, Nmax):
    D = np.diag(np.diag(A))
    print(np.linalg.inv(D))
    L = -np.tril(A)+D
    U = -np.triu(A)+D
    print(L+U)
    T = np.dot(np.linalg.inv(D), (L+U))
    print(T)
    print(np.linalg.eigvals(T))
    C = np.dot(np.linalg.inv(D), b)
    xant = x0
    E = 1000
    cont = 0
    while E > tol and cont < Nmax:
        xact = np.dot(T, xant)+C
        E = np.linalg.norm(xant-xact)
        xant = xact
        cont = cont+1
    x = xact
    iter = cont
    err = E
    return x, iter, err

"""
A = np.array([[4, -1, -2],
              [1, -8, 2],
             [-2, 1, 5]])

b = np.array([8, -11, 1])

x0 = np.array([2, 2, 2])

tol = 1e-2

Nmax = 100

print(jacobi(A, b, x0, tol, Nmax))
"""
