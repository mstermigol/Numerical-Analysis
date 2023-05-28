import numpy as np
from sustregr import sustregr
from sustprgr import sustprgr


def cholesky(A, b):
    n = np.size(A, 0)
    L = np.eye(n)
    U = np.eye(n)

    for i in range(n-1):
        L[i, i] = np.sqrt(A[i, i] - np.dot(L[i, 0:i], U[0:i, i]))
        U[i, i] = L[i, i]
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, 0:i], U[0:i, i]))/U[i, i]
        for j in range(i+1, n):
            U[i, j] = (A[i, j] - np.dot(L[i, 0:i], U[0:i, j]))/L[i, i]
    L[n-1, n-1] = np.sqrt(A[n-1, n-1] - np.dot(L[n-1, 0:n-1], U[0:n-1, n-1]))
    U[n-1, n-1] = L[n-1, n-1]

    z = sustprgr(L, b)
    x = sustregr(U, z)

    return x


A = np.array([[1.043, -0.082, -0.088],
              [-0.011, 0.527, -0.104],
              [-0.137, -0.077, 0.362]])

b = np.array([1, 0, 0])

print(cholesky(A, b))
