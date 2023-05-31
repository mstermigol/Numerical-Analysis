import numpy as np

def gseidel(A, b, x0, tol, Nmax):
    D = np.diag(np.diag(A))
    L = -np.tril(A) + D
    U = -np.triu(A) + D
    T = np.dot(np.linalg.inv(D-L), U)
    C = np.dot(np.linalg.inv(D-L), b)
    xant = x0
    E = 1000
    cont = 0
    while E > tol and cont < Nmax:
        xact = np.dot(T, xant) + C
        E = np.linalg.norm(xant-xact)
        xant = xact
        cont += 1
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

tol = 0.05

Nmax = 100

print(gseidel(A, b, x0, tol, Nmax))
"""
