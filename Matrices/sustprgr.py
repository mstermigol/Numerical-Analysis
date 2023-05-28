import numpy as np


def sustprgr(A, b):
    M = np.hstack((A, b.reshape(-1, 1)))
    n = np.size(M, 0)
    x = np.zeros(n)
    x[0] = M[0, n] / M[0, 0]
    for i in range(1, n):
        aux = np.concatenate(([1], x[0:i]))
        aux1 = np.concatenate(([M[i, n]], -M[i, 0:i]))
        x[i] = np.dot(aux, aux1) / M[i, i]
    return x
