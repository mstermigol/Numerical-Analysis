import numpy as np
from sustprgr import sustprgr
from sustregr import sustregr


def LUparcial(A, b):
    n = np.size(A, 0)
    L = np.eye(n)
    U = np.zeros((n, n))
    P = np.eye(n)
    M = A

    for i in range(n-1):
        aux0 = np.max(abs(M[i:n, i]))
        aux = np.where(abs(M[i:n, i]) == aux0)[0][0]
        if aux0 > abs(M[i, i]):
            aux2 = M[i+aux, i:n]
            aux3 = P[i+aux, :]
            M[aux+i, i:n] = M[i, i:n]
            P[aux+i, :] = P[i, :]
            M[i, i:n] = aux2
            P[i, :] = aux3
            if i > 1:
                aux4 = L[i+aux, 0:i]
                L[i+aux, 0:i] = L[i, 0:i]
                L[i, 0:i] = aux4
        for j in range(i+1, n):
            if M[j, i] != 0:
                L[j, i] = M[j, i]/M[i, i]
                M[j, i:n] = M[j, i:n] - (M[j, i]/M[i, i])*M[i, i:n]
        U[i, i:n] = M[i, i:n]
        U[i+1, i+1:n] = M[i+1, i+1:n]
    U[n-1, n-1] = M[n-1, n-1]

    z = sustprgr(L, np.dot(P, b))
    x = sustregr(U, z)

    #print("L: ")
    #print(L)
    #print("\nU: ")
    #print(U)
    #print("\nP: ")
    #print(P)

    #print("\nValores de x: ")
    return x


A = np.array([[4, -1, -2],
              [1, -8, 2],
             [-2, 1, 5]])

b = np.array([1, 0, 0])


print(LUparcial(A, b))

