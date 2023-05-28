import numpy as np


def lagrange(x, y, punto):
    n = np.size(x)
    p = 0
    for i in range(n):
        L = y[i]
        for j in range(n):
            if i != j:
                L = L*(punto-x[j])/(x[i]-x[j])
        p = p+L
    return p


x = [-1, 0, 1, 2]
y = [2.3, -1.2, 4.5, 3.3]

print(lagrange(x, y, 0.5))
