"""function [x,iter,err]=C17_gseidel(A,b,x0,tol,Nmax)

%Inicializaci�n 
D=diag(diag(A));
L=-tril(A)+D;
U=-triu(A)+D;
T=inv(D-L)*U; 
C=inv(D-L)*b;
xant=x0;
E=1000;
cont=0;

%Ciclo
while E>tol && cont<Nmax       
    xact=T*xant+C;
    E=norm(xant-xact);
    xant=xact;
    cont=cont+1;
end

%Entrega de resultados
x=xact;
iter=cont;
err=E;
end"""

import numpy as np

def gseidel(A, b, x0, tol, Nmax):
    D = np.diag(np.diag(A))
    L = -np.tril(A) + D
    U = -np.triu(A) + D
    T = np.dot(np.linalg.inv(D-L), U)
    C = np.dot(np.linalg.inv(D-L), b)
    xant = x0
    E = 1000
    cont = 0
    while E > tol and cont < Nmax:
        xact = np.dot(T, xant) + C
        E = np.linalg.norm(xant-xact)
        xant = xact
        cont += 1
    x = xact
    iter = cont
    err = E
    return x, iter, err



A = np.array([[4, -1, -2],
              [1, -8, 2],
             [-2, 1, 5]])

b = np.array([8, -11, 1])

x0 = np.array([2, 2, 2])

tol = 0.05

Nmax = 100

print(gseidel(A, b, x0, tol, Nmax))
