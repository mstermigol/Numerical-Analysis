import numpy as np
from Matrices.sustregr import sustregrM


def gausstot(A, b):
    n = np.size(A, 1)
    M = np.hstack((A, b.reshape(n, 1)))
    cambi = []
    for i in range(n-1):
        a, b = np.where(abs(M[i:n, i:n]) == np.max(abs(M[i:n, i:n])))
        if b[0]+i != i:
            cambi.append([i, b[0]+i])
            aux2 = M[:, b[0]+i]
            M[:, b[0]+i] = M[:, i]
            M[:, i] = aux2
        if a[0]+i != i:
            aux2 = M[i+a[0], i:n+1]
            M[a[0]+i, i:n+1] = M[i, i:n+1]
            M[i, i:n+1] = aux2
        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] = M[j, i:n+1] - (M[j, i]/M[i, i])*M[i, i:n+1]
    x = sustregrM(M)
    for i in range(len(cambi)-1, -1, -1):
        aux = x[cambi[i][0]]
        x[cambi[i][0]] = x[cambi[i][1]]
        x[cambi[i][1]] = aux
    return x

"""
A = np.array([[1.043, -0.082, -0.088],
              [-0.011, 0.527, -0.104],
              [-0.137, -0.077, 0.362]])

b = np.array([1, 0, 0])

print(gausstot(A, b))
"""