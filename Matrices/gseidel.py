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
from sustregr import sustregr
from sustprgr import sustprgr


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


A = np.array([[1.043, -0.082, -0.088],
              [-0.011, 0.527, -0.104],
              [-0.137, -0.077, 0.362]])

b = np.array([1, 0, 0])

x0 = np.array([0, 0, 0])

tol = 1e-5

Nmax = 100

print(gseidel(A, b, x0, tol, Nmax))
