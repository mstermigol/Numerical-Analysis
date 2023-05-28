import numpy as np


def vandermonde(x, y):
    N = len(x)
    A = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if j == 0:
                A[i, j] = 1
            else:
                A[i, j] = x[i]**j

    coeficientes = np.dot(np.linalg.inv(A), y)
    print(coeficientes)


x = [-1, 0, 1, 2]
y = [2.3, -1.2, 4.5, 3.3]

vandermonde(x, y)
