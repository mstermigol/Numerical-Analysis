import numpy as np
from Matrices.sustregr import sustregr
from Matrices.sustprgr import sustprgr


def doolitle_matrices(A):
    n = np.size(A, 0)
    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n-1):
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, 0:i], U[0:i, j])
            print("Matriz U: ")
            print(U)
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, 0:i], U[0:i, i]))/U[i, i]
            print("Matriz L: ")
            print(L)
    U[n-1, n-1] = A[n-1, n-1] - np.dot(L[n-1, 0:n-1], U[0:n-1, n-1])

    print("\nMatrices L y U: \n")
    print(f"\n{L}\n")
    print(f"\n{U}\n")


def doolitle_solucion(A, b):
    n = np.size(A, 0)
    L = np.eye(n)
    U = np.eye(n)

    for i in range(n-1):
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, 0:i], U[0:i, j])
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, 0:i], U[0:i, i]))/U[i, i]
    U[n-1, n-1] = A[n-1, n-1] - np.dot(L[n-1, 0:n-1], U[0:n-1, n-1])

    z = sustprgr(L, b)
    print(z)
    x = sustregr(U, z)

    return x
