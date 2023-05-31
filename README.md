- [Manual de usuario](#manual-de-usuario)
  - [Anotaciones generales](#anotaciones-generales)
  - [Anotaciones Lagrange](#anotaciones-lagrange)
- [Seudocodigos](#seudocodigos)
  - [Seudocódigo bisección](#seudocódigo-bisección)
    - [Relativo](#relativo)
    - [Absoluto](#absoluto)
  - [Seudocódigo busquedas incrementales](#seudocódigo-busquedas-incrementales)
  - [Seudocodigo Newton](#seudocodigo-newton)
  - [Seudocódigo Gauss simple](#seudocódigo-gauss-simple)
  - [Seudocódigo Gauss parcial](#seudocódigo-gauss-parcial)
  - [Seudocódigo Cholesky](#seudocódigo-cholesky)
  - [Seudocódigo Lagrange](#seudocódigo-lagrange)

## Manual de usuario

### Anotaciones generales

Cuando se escriba una función, los equivalentes a estas expresiones son los siguientes:

- $ e^x=exp⁡(x) $
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

### Anotaciones Lagrange

A la hora de ingresar los valores, estos se tienen que ingresar separados por “,” (coma) así _1,2,3,4_ además que todos los valores deben ser enteros o flotantes (nada de caracteres)

Si se quiere extrapolar seguramente dará un valor muy alejado
del real, así que se debe evitar extrapolar con este método

## Seudocodigos

### Seudocódigo bisección

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

### Seudocodigo Newton

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

### Seudocódigo Gauss simple

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

### Seudocódigo Cholesky

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

### Seudocódigo Lagrange

    Entradas x, y, punto
    Salidas p

    n = size(x)
    p = 0
    for i in range(n):
        L = yi
        for j in range(n):
            if i != j:
                L = L*(punto-xj)/(xi-xj)
            p = p + L
    return p
