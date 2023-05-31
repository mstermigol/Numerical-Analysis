- [Manual de usuario](#manual-de-usuario)
  - [Anotaciones generales](#anotaciones-generales)
  - [Anotaciones bisección](#anotaciones-bisección)
  - [Anotaciones busquedas incrementales](#anotaciones-busquedas-incrementales)
  - [Anotaciones Newton](#anotaciones-newton)
  - [Anotaciones punto fijo](#anotaciones-punto-fijo)
  - [Anotaciones raices multiples](#anotaciones-raices-multiples)
  - [Anotaciones secante](#anotaciones-secante)
  - [Anotaciones regla falsa](#anotaciones-regla-falsa)
  - [Anotaciones Cholesky](#anotaciones-cholesky)
  - [Anotaciones Crout](#anotaciones-crout)
  - [Anotaciones Doolittle](#anotaciones-doolittle)
  - [Anotaciones Gauss simple](#anotaciones-gauss-simple)
  - [Anotaciones Gauss parcial](#anotaciones-gauss-parcial)
  - [Anotaciones Gauss total](#anotaciones-gauss-total)
  - [Anotaciones Gauss-Seidel](#anotaciones-gauss-seidel)
  - [Anotaciones Jacobi](#anotaciones-jacobi)
  - [Anotaciones LU parcial](#anotaciones-lu-parcial)
  - [Anotaciones LU simple](#anotaciones-lu-simple)
  - [Anotaciones Lagrange](#anotaciones-lagrange)
  - [Anotaciones diferencias divididas](#anotaciones-diferencias-divididas)
  - [Anotaciones Vandermonde](#anotaciones-vandermonde)
- [Seudocódigos](#seudocódigos)
  - [Seudocódigo bisección](#seudocódigo-bisección)
    - [Relativo](#relativo)
    - [Absoluto](#absoluto)
  - [Seudocódigo busquedas incrementales](#seudocódigo-busquedas-incrementales)
  - [Seudocódigo Newton](#seudocódigo-newton)
  - [Seudocódigo punto fijo](#seudocódigo-punto-fijo)
  - [Seudocódigo raíces múltiples](#seudocódigo-raíces-múltiples)
  - [Seudocódigo secante](#seudocódigo-secante)
  - [Seudocódigo regla falsa](#seudocódigo-regla-falsa)
  - [Seudocódigo Cholesky](#seudocódigo-cholesky)
  - [Seudocódigo Crout](#seudocódigo-crout)
  - [Seudocódigo Doolittle](#seudocódigo-doolittle)
  - [Seudocódigo Gauss simple](#seudocódigo-gauss-simple)
  - [Seudocódigo Gauss parcial](#seudocódigo-gauss-parcial)
  - [Seudocódigo Gauss total](#seudocódigo-gauss-total)
  - [Seudocódigo Gauss-Seidel](#seudocódigo-gauss-seidel)
  - [Seudocódigo Jacobi](#seudocódigo-jacobi)
  - [Seudocódigo LU parcial](#seudocódigo-lu-parcial)
  - [Seudocódigo LU simple](#seudocódigo-lu-simple)
  - [Seudocódigo Lagrange](#seudocódigo-lagrange)
  - [Seudocódigo diferencias divididas](#seudocódigo-diferencias-divididas)
  - [Seudocódigo Vandermonde](#seudocódigo-vandermonde)

## Manual de usuario

### Anotaciones generales

Cuando se escriba una función, los equivalentes a estas expresiones son los siguientes:

- $e^x=exp⁡(x)$
- $ln⁡x=ln(x)$
- $√x=sqrt(x)$
- $∛x=thirdroot(x)$
- $log⁡x=log⁡(x)$
- $sin⁡x=sin(x)$
- $cos⁡x=cos(x)$
- $tanx=tan⁡(x)$

Si se van a usar decimales se manejan con el “.” (punto) así _1.5_

En las matrices la manera de ingresar la matriz A es, cada elemento de la fila separado por “,” y cuando se va a pasar a la siguiente fila se pone un “;”. Ejemplo: _2,3;1,2_ (Lo que resulta en una matriz 2X2 donde 2 y 3 son los valores de la fila uno de izquierda a derecha y, 1 y 2 son los elementos de la segunda fila).

Los métodos se distribuyeron de la siguiente manera:

**Miguel Sosa**

- Cholesky
- Crout
- Lagrange
- Diferencias divididas
- Vandermonde
- Doolitle

**Miguel Jaramillo**

- Gauss seidel
- Jacobi
- LU parcial
- LU simple
- Gauss total

**Sergio Córdoba**

- Biseccion
- Búsquedas incrementales
- Newton
- Gauss simple
- Gauss parcial

**Valeria Guerra**

- Punto fijo
- Raíces múltiples
- Regla falsa
- Secante

### Anotaciones bisección

[Seudocódigo](#seudocódigo-bisección)

### Anotaciones busquedas incrementales

[Seudocódigo](#seudocódigo-busquedas-incrementales)

### Anotaciones Newton

[Seudocódigo](#seudocódigo-newton)

### Anotaciones punto fijo

[Seudocódigo](#seudocódigo-punto-fijo)

### Anotaciones raices multiples

[Seudocódigo](#seudocódigo-raíces-múltiples)

### Anotaciones secante

[Seudocódigo](#seudocódigo-secante)

### Anotaciones regla falsa

[Seudocódigo](#seudocódigo-regla-falsa)

### Anotaciones Cholesky

[Seudocódigo](#seudocódigo-cholesky)

### Anotaciones Crout

[Seudocódigo](#seudocódigo-crout)

### Anotaciones Doolittle

[Seudocódigo](#seudocódigo-doolittle)

### Anotaciones Gauss simple

[Seudocódigo](#seudocódigo-gauss-simple)

### Anotaciones Gauss parcial

[Seudocódigo](#seudocódigo-gauss-parcial)

### Anotaciones Gauss total

[Seudocódigo](#seudocódigo-gauss-total)
La matriz ingresada debe ser cuadrada. Y que sus valores sean o enteros o flotantes. Y que la matriz no sea singular.

### Anotaciones Gauss-Seidel

[Seudocódigo](#anotaciones-gauss-seidel)
La matriz ingresada debe ser cuadrada. Y que sus valores sean o enteros o flotantes. La matriz A debe ser invertible para evitar errores o resultados inesperados.

### Anotaciones Jacobi

[Seudocódigo](#seudocódigo-jacobi)
La matriz ingresada debe ser cuadrada. Y que sus valores sean o enteros o flotantes. La matriz A debe ser diagonalmente dominante y que su diagonal no sean ceros.

### Anotaciones LU parcial

[Seudocódigo](#seudocódigo-lu-parcial)
La matriz ingresada debe ser cuadrada. Y que sus valores sean o enteros o flotantes. Y que la matriz no sea singular.

### Anotaciones LU simple

[Seudocódigo](#seudocódigo-lu-simple)
La matriz ingresada debe ser cuadrada. Y que sus valores sean o enteros o flotantes. Y que la matriz no sea singular y sea invertible.

### Anotaciones Lagrange

[Seudocódigo](#seudocódigo-lagrange)
A la hora de ingresar los valores, estos se tienen que ingresar separados por “,” (coma) así _1,2,3,4_ además que todos los valores deben ser enteros o flotantes (nada de caracteres)

Si se quiere extrapolar posiblemente dará un valor muy alejado del real, así que se debe evitar extrapolar con este método

### Anotaciones diferencias divididas

[Seudocódigo](#seudocódigo-diferencias-divididas)
A la hora de ingresar los valores, estos se tienen que ingresar separados por “,” (coma) así _1, 2, 3, 4_ además que todos los valores deben ser enteros o flotantes (nada de caracteres)

Al ingresar los puntos, A la hora de ingresar los valores, estos se tienen que ingresar separados por “,” (coma) así _1, 2.5, 3, 4.5_

Si se quiere extrapolar posiblemente dará un valor muy alejado del real, así que se debe evitar extrapolar con este método

### Anotaciones Vandermonde

[Seudocódigo](#seudocódigo-vandermonde)
Las mismas que [diferencias divididas](#anotaciones-diferencias-divididas)

## Seudocódigos

### Seudocódigo bisección

[Anotaciones](#anotaciones-bisección)

#### Relativo

    Inicio
    funcion biseccionRelativo(f, a, b, tol, Nmax)
        fa = f(a)
        fb = f(b)
        valorMedio = (a + b) / 2
        fValorMedio = f(valorMedio)
        E = V. Absoluto de a - valorMedio
        e = E / valorMedio
        iter = 1
        Mientras V. Absoluto de e > tol y iter < Nmax Hacer
            Si fa * fValorMedio < 0:
                b = valorMedio
            De lo contrario
                a = valorMedio
            FinSi
            fa = f(a)
            fb = f(b)
            p0 = valorMedio
            valorMedio = (a + b) / 2
            fValorMedio = f(valorMedio)
            E = V. Absoluto de valorMedio - p0
            e = E / valorMedio
            iter += 1
        FinMientras
        return iter, a, f(a), p, f(p), b, f(b), e
    FinBiseccionRelativo
    Fin

#### Absoluto

    Inicio
    funcion biseccionAbsoluto(f, a, b, tol, Nmax)
        fa = f(a)
        fb = f(b)
        valorMedio = (a + b) / 2
        fValorMedio = f(valorMedio)
        E = V. Absoluto de a - valorMedio
        iter = 1
        Mientras E > tol y iter < Nmax Hacer
            Si fa * fValorMedio < 0:
                b = valorMedio
            De lo contrario
                a = valorMedio
            FinSi
            fa = f(a)
            fb = f(b)
            p0 = valorMedio
            valorMedio = (a + b) / 2
            fValorMedio = f(valorMedio)
            E = V. Absoluto de valorMedio - p0
            iter += 1
        FinMientras
        return iter, a, f(a), p, f(p), b, f(b), E
    FinBiseccionAbsoluto
    Fin

### Seudocódigo busquedas incrementales

[Anotaciones](#anotaciones-busquedas-incrementales)

    Inicio
    funcion busquedas(f, x0, h, Nmax)
        xAnterior = x0
        fAnterior = f(xAnterior)
        xActual = xActual + h
        fActual = f(xActual)
        iter = 0
        Desde i = 1 Hasta Nmax Hacer
            Si fActual*fAnterior < 0 Entonces
                break
            FinSi
            xAnterior = xActual
            fAnterior = fActual
            xActual = xAnterior + h
            fActual = f(xActual)
            iter += 1
        FinDesde
        return xAnterior, xActual, h
    FinBusquedas
    Fin

### Seudocódigo Newton

[Anotaciones](#anotaciones-newton)

    Inicio
    funcion newton(f, derivada, xo, tol, Nmax)
        xAnterior = xo
        fAnterior = f(xAnterior)
        E = 1000
        iter = 0
        derivadaAnterior = derivada(xAnterior)
        Mientras E > tol y iter < Nmax y derivadaAnterior != 0 Hacer
            xActual = xAnterior - fAnterior/derivadaAnterior
            fActual = f(xActual)
            E = Valor absoluto de xActual -xAnterior
            iter += 1
            xAnterior = xActual
            fAnterior = fActual
            derivadaAnterior = derivada(xAnterior)
        FinMientras
        return iter, x, f(x), error
    FinNewton
    Fin

### Seudocódigo punto fijo

[Anotaciones](#anotaciones-punto-fijo)

### Seudocódigo raíces múltiples

[Anotaciones](#anotaciones-raices-multiples)

### Seudocódigo secante

[Anotaciones](#anotaciones-secante)

### Seudocódigo regla falsa

[Anotaciones](#anotaciones-regla-falsa)

### Seudocódigo Cholesky

[Anotaciones](#anotaciones-cholesky)

    Entradas A, b
    Salidas x []

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

### Seudocódigo Crout

[Anotaciones](#anotaciones-crout)

    Entradas: A, b
    Salidas: x[]

    funcion crout (A, b)
        n = tamaño de A
        L = matriz con diagonal de 1s tamaño n
        U = matriz con diagonal de 1s tamaño n

        para i desde 0 hasta n-1
            para j desde i hasta n
                U[i, j] = A[i, j] - producto punto(L[i, 0:i], U[0:i, j])
            finpara

            para j desde i+1 hasta n
                L[j, i] = (A[j, i] - producto punto(L[j, 0:i], U[0:i, i]))/U[i, i]
            finpara

            L[n-1, n-1] = A[n-1, n-1] - producto punto(L[n-1, 0:n-1], U[0:n-1, n-1])

            z = sustitucion progresiva (L, b)
            x = sustitucion regresiva (U, z)
        finpara

        return x

### Seudocódigo Doolittle

[Anotaciones](#anotaciones-doolittle)

    Entradas: A, b
    Salidas: x[]

    funcion doolittle (A, b)
        n = tamaño de A
        L = matriz con diagonal de 1s tamaño n
        U = matriz con diagonal de 1s tamaño n

        para i desde 0 hasta n-1
            para j desde i hasta n
                U[i, j] = A[i, j] - producto punto(L[i, 0:i], U[0:i, j])
            finpara

            para j desde i+1 hasta n
                L[j, i] = (A[j, i] - producto punto(L[j, 0:i], U[0:i, i]))/U[i, i]
            finpara

            U[n-1, n-1] = A[n-1, n-1] - producto punto(L[n-1, 0:n-1], U[0:n-1, n-1])

            z = sustitucion progresiva (L, b)
            x = sustitucion regresiva (U, z)
        finpara

        return x

### Seudocódigo Gauss simple

[Anotaciones](#anotaciones-gauss-simple)

    Inicio
    funcion gausspl(A, b)
        n = np.size(A, 0)
        m = np.hstack((A, b.reshape(-1, 1)))
        contador = 1
        Desde i = 0 Hasta n - 1 Hacer
            Desde j = i + 1 Hasta n Hacer
                Si M[j, i] != 0 Entonces
                    M[j, i:n+1] = M[j, i:n+1] - (M[j, i]/M[i, i])*M[i, i:n+1]
                FinSi
                Imprimir f"Paso {contador}:"
                Imprimir M
                contador += 1
            FinDesde
        FinDesde
        Imprimir ""
        Imprimir Resultado
        x = sustregrM(M)
        return x
    FinGausspl
    Fin

### Seudocódigo Gauss parcial

[Anotaciones](#anotaciones-gauss-parcial)

    Inicio
    funcion gausspar(A, b):
        n = np.size(A, 0)
        M = np.hstack((A, b.reshape(-1, 1)))
        Imprimir Matriz:
        Imprimir M
        contador = 1
        Desde i = 0 Hasta n Hacer
            p = if
            Desde j = i + 1 Hasta n Hacer
                Si V. Absoluto de M[j, i] > V. Absoluto de M[p, i] Hacer
                    p = j
                FinSi
            FinDesde
            Desde j = i Hasta n + 1 Hcaer
                temp = M[i, j]
                M[i, j] = M[p, j]
                M[p, j] = temp
            FinDesde
            Desde i = 0 Hasta n - 1 Hacer
                Dede j = i + 1 Hasta n Hacer:
                    Si M[j, i] != 0 Entonces
                        M[j, i:n+1] = M[j, i:n+1] - (M[j, i]/M[i, i])*M[i, i:n+1]
                    FinSi
                    Imprimir f"Paso {contador}:"
                    Imprimir M
                    contador += 1
                FinDesde
            FinDesde
        FinDesde
        Imprimir ""
        Imprimir Resultado:
        x = sustregrM(M)
        return x

### Seudocódigo Gauss total

[Anotaciones](#anotaciones-gauss-total)

    Función gausstot(A, b)
        n = tamaño de columnas de A
        M = concatenar A y b en una matriz extendida
        cambi = lista vacía

        Para i desde 0 hasta n-1
            (a, b) = posición del máximo valor en la submatriz M[i:n, i:n]

            Si b[0]+i != i
                intercambiar columnas b[0]+i e i en la matriz M
                agregar [i, b[0]+i] a la lista cambi

            Si a[0]+i != i
                intercambiar filas a[0]+i e i en la matriz M

            Para j desde i+1 hasta n
                Si M[j, i] != 0
                    M[j, i:n+1] = M[j, i:n+1] - (M[j, i]/M[i, i])*M[i, i:n+1]

        x = sustregrM(M)

        Para i desde longitud(cambi)-1 hasta 0, decrementando en 1
            aux = x[cambi[i][0]]
            x[cambi[i][0]] = x[cambi[i][1]]
            x[cambi[i][1]] = aux

        Retornar x

### Seudocódigo Gauss-Seidel

[Anotaciones](#anotaciones-gauss-seidel)

    función gseidel(A, b, x0, tol, Nmax):
        D = obtener diagonal de A
        L = matriz triangular inferior de A con ceros en la diagonal
        U = matriz triangular superior de A con ceros en la diagonal
        T = (D-L)^(-1) * U
        C = (D-L)^(-1) * b
        xant = x0
        E = 1000
        cont = 0

        mientras E > tol y cont < Nmax:
            xact = T * xant + C
            E = norma de xant - xact
            xant = xact
            cont += 1

        x = xact
        iter = cont
        err = E
        retornar x, iter, err

### Seudocódigo Jacobi

[Anotaciones](#anotaciones-jacobi)

    Función jacobi(A, b, x0, tol, Nmax):
        D = matriz diagonal con los elementos diagonales de A
        Imprimir inversa de D
        L = matriz triangular inferior de A - D
        U = matriz triangular superior de A - D
        Imprimir L + U
        T = inversa de D multiplicada por (L + U)
        Imprimir T
        Imprimir valores propios de T
        C = inversa de D multiplicada por b
        xant = x0
        E = 1000
        cont = 0

        Mientras E > tol y cont < Nmax:
            xact = T multiplicada por xant más C
            E = norma euclidiana de la diferencia entre xant y xact
            xant = xact
            cont = cont + 1

        x = xact
        iter = cont
        err = E
        retornar x, iter, err


### Seudocódigo LU parcial

[Anotaciones](#anotaciones-lu-parcial)

    función LUparcial(A, b):
        n = tamaño de A (filas)
        L = matriz identidad de tamaño n x n
        U = matriz de ceros de tamaño n x n
        P = matriz identidad de tamaño n x n
        M = copia de A

        para i en rango(0, n-1):
            aux0 = máximo valor absoluto en M[i:n, i]
            aux = coordenadas del máximo en M[i:n, i]

            si aux0 > valor absoluto de M[i, i]:
                intercambiar filas y columnas en M, P y L para que el máximo quede en M[i, i]

            para j en rango(i+1, n):
                si M[j, i] != 0:
                    L[j, i] = M[j, i] / M[i, i]
                    actualizar filas correspondientes en L y M para realizar eliminación gaussiana

            actualizar filas i y i+1 en U con los valores correspondientes de M

        asignar el último elemento de la diagonal de M a U[n-1, n-1]

        z = sustprgr(L, producto de P por b)
        x = sustregr(U, z)

        retornar x

### Seudocódigo LU simple

[Anotaciones](#anotaciones-lu-simple)

    función LUsimpl(A, b):
        n = tamaño de A en la dimensión 0
        L = matriz identidad de tamaño nxn
        U = matriz de ceros de tamaño nxn
        M = copia de A

        para i desde 0 hasta n-1:
            para j desde i+1 hasta n:
                si M[j, i] != 0:
                    L[j, i] = M[j, i] / M[i, i]
                    M[j, i:n] = M[j, i:n] - (M[j, i] / M[i, i]) * M[i, i:n]

            U[i, i:n] = M[i, i:n]
            U[i+1, i+1:n] = M[i+1, i+1:n]

        U[n-1, n-1] = M[n-1, n-1]

        z = sustprgr(L, b)
        x = sustregr(U, z)

        retornar x

### Seudocódigo Lagrange

[Anotaciones](#anotaciones-lagrange)

    Entradas x, y, punto
    Salidas p

    funcion lagrange (x, y, punto)
        n = size(x)
        p = 0
        para i desde 0 hasta n:
            L = yi
            para j desde 0 hasta n:
                si i != j:
                    L = L*(punto-xj)/(xi-xj)
                finsi
                p = p + L
            finpara
        finpara

        return p

### Seudocódigo diferencias divididas

[Anotaciones](#anotaciones-diferencias-divididas)

    Entradas: x, y, puntos
    Salidas: Polinomio, p(puntos)

    funcion diferencias (x, y, puntos)
        a = []
        para i desde 0 hasta len(x)+1
            aux = []
            para j de 0 hasta len(x)
                aux.append(0)
            finpara
            a.append(aux)
        finpara

        para i desde 0 hasta len(x)
            a[0][i] = x[i]
            a[1][i] = y[i]
        finpara

        b = 1
        c = 1
        d = 1

        para i desde 0 hasta len(a[0])
            para j desde 0 hasta len(a[0])-b
                a[c+1][j]=(a[c][j+1]-a[c][j])/(a[0][j+d]-a[0][j])
            finpara

            b = b + 1
            c = c + 1
            d = d + 1
        finpara

        p = 0
        w = 0

        para i desde 0 hasta len(a[0])
            terminos = 1
            para j desde 0 hasta w
                terminos = terminos * (x-a[0][j])
            finpara

            p = p + a[i+1][0] * terminos
            w = w + 1
        finpara

        para punto en puntos
            print(p(punto))
        finpara

### Seudocódigo Vandermonde

[Anotaciones](#anotaciones-vandermonde)

    Entradas: x, y, puntos
    Salidas: coeficientes, valores

    funcion vandermonde (x, y, punto)
        N = len(x)
        A = matriz de ceros tamaño NxN

        para i desde 0 hasta N
            para j desde 0 hasta N
                si j == 0
                    A[i, j] = 1
                si no
                    A[i, j] = x[i]**j
                finsi
            finpara
        finpara

        coeficientes = producto punto(inversa(A), y)

        para i desde 0 hasta len(puntos)
            resultado = 0
            para j desde 0 hasta N
                resultado = resultado + coeficientes[j] * (puntos[i]**j)
            finpara
            print(p(puntos[i]) = resultado)
