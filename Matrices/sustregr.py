import numpy as np


def sustregr(A, b):
    M = np.hstack((A, b.reshape(-1, 1)))
    n = np.size(M, 0)

    x = np.zeros(n)

    x[n-1] = M[n-1, n]/M[n-1, n-1]
    for i in range(n-1, -1, -1):
        aux = np.concatenate((np.array([1]), x[i+1:n]))
        aux1 = np.concatenate((np.array([M[i, n]]), -M[i, i+1:n]))
        x[i] = np.dot(aux, aux1)/M[i, i]
    return x


def sustregrM(M):
    n = np.size(M, 0)

    x = np.zeros(n)

    x[n-1] = M[n-1, n]/M[n-1, n-1]
    for i in range(n-1, -1, -1):
        aux = np.concatenate((np.array([1]), x[i+1:n]))
        aux1 = np.concatenate((np.array([M[i, n]]), -M[i, i+1:n]))
        x[i] = np.dot(aux, aux1)/M[i, i]
    return x
