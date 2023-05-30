import numpy as np
from Matrices.sustregr import sustregrM


def gausspl(A, b):
    n = np.size(A, 0)
    M = np.hstack((A, b.reshape(-1, 1)))
    contador = 1
    for i in range(n-1):
        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] = M[j, i:n+1] - (M[j, i]/M[i, i])*M[i, i:n+1]
            #print(f"Paso {contador}:")
            #print(M)
            contador += 1
    #print("")
    #print("Resultado:")
    x = sustregrM(M)
    return x

A = np.array([[1.043, -0.082, -0.088],
              [-0.011, 0.527, -0.104],
              [-0.137, -0.077, 0.362]])

b = np.array([1, 0, 0])