# Pseudocodigos

### Cholesky

        funcion Cholesky (A, b)
            n = tamaño de a
            L = matriz con diagonal de 1s tamaño n
            U = matriz con diagonal de 1s tamaño n

        para i desde 0 hasta n-1
            L[i,i]=raiz(A[i,i]-producto punto(L[i, 0:i], U[0:i, i]))
            U[i, i] = L[i, i]

            para j desde i+1 hasta n
                L[j, i] = (A[j, i] - producto punto(L[j, 0:i], U[0:i, i]))/U[i, i]
            finpara
            para j desde i+1 hasta n
                U[i, j] = (A[i, j] - producto punto(L[i, 0:i], U[0:i, j]))/L[i, i]
            finpara

            L[n-1, n-1] = raiz(A[n-1, n-1] - producto punto(L[n-1, 0:n-1], U[0:n-1, n-1]))
            U[n-1, n-1] = L[n-1, n-1]

        finpara

        z = sustitucion progresiva (L, b)
        x = sustitucion regresiva (U, z)

        retorno x

###
