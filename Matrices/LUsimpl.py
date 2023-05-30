import numpy as np
from sustregr import sustregr
from sustprgr import sustprgr


def LUsimpl(A, b):
    n = np.size(A, 0)
    L = np.eye(n)
    U = np.zeros((n, n))
    M = A

    for i in range(n-1):
        for j in range(i+1, n):
            if M[j, i] != 0:
                L[j, i] = M[j, i]/M[i, i]
                M[j, i:n] = M[j, i:n] - (M[j, i]/M[i, i])*M[i, i:n]
        U[i, i:n] = M[i, i:n]
        U[i+1, i+1:n] = M[i+1, i+1:n]
    U[n-1, n-1] = M[n-1, n-1]

    z = sustprgr(L, b)
    x = sustregr(U, z)

    return x


A = np.array([[1.043, -0.082, -0.088],
              [-0.011, 0.527, -0.104],
              [-0.137, -0.077, 0.362]])

b = np.array([1, 0, 0])

print(LUsimpl(A, b))

