import tkinter as tk
from Raices.biseccion import biseccion
from Raices.busquedas_incrementales import busquedas
from Interpolacion.Lagrange import lagrange
from Raices.newton import newton_lambda
from Interpolacion.Newton import newtonInterpolacion
from Interpolacion.Vandermonde import vandermonde
from Matrices.gausspl import gausspl
from Matrices.Jacobi import jacobi
from Matrices.gseidel import gseidel
from Matrices.LUpar import LUparcial
import numpy as np
from math import *

root = tk.Tk()

root.geometry("800x600")
root.title("Metodos numéricos")

opcionesMetodos = [
    "Bisección",
    "Busqueda incremental",
    "Newton",
    "Punto fijo",
    "Raices multiples",
    "Secante",
    "Regla falsa",
    "Cholesky",
    "Crout",
    "Doolittle",
    "Gauss simple",
    "Gauss con pivoteo parcial",
    "Gauss con pivoteo total",
    "Gauss-Seidel",
    "Jacobi",
    "LU parcial",
    "LU simple",
    "LaGrange",
    "Diferencias divididas",
    "Vandermonde"
]


def inicio(root):
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text="Metodos numéricos", font=("Arial", 20))
    label.grid()

    clickedMetodos = tk.StringVar()
    clickedMetodos.set(opcionesMetodos[0])
    dropDownMetodos = tk.OptionMenu(root, clickedMetodos, *opcionesMetodos)
    dropDownMetodos.grid(sticky="")
    root.grid_columnconfigure(0, weight=1)

    siguiente = tk.Button(root, text="Siguiente",
                          command=lambda: definirMetodo(root, clickedMetodos.get()))
    siguiente.grid()


inicio(root)

operaciones = {"exp": exp, "ln(x)": log, "log(x)": log10,
               "sin(x)": sin, "cos(x)": cos, "tan(x)": tan,
               "sqrt(x)": sqrt, "thirdroot(x)": lambda x: x**(1/3),}

error = ["Error absoluto", "Error relativo"]


def definirMetodo(root, metodo):
    errorSeleccionado = tk.StringVar()
    errorSeleccionado.set(error[0])

    for widget in root.winfo_children():
        widget.destroy()

    if metodo == "Bisección":
        label = tk.Label(root, text="Biseccion", font=("Arial", 20))
        label.grid()

        funcion = tk.Label(root, text="Ingrese la función")
        funcion.grid()
        funcionEntry = tk.Entry(root)
        funcionEntry.grid()

        a = tk.Label(root, text="Ingrese el valor de a")
        a.grid()
        aEntry = tk.Entry(root)
        aEntry.grid()

        b = tk.Label(root, text="Ingrese el valor de b")
        b.grid()
        bEntry = tk.Entry(root)
        bEntry.grid()

        tol = tk.Label(root, text="Ingrese el valor de la tolerancia")
        tol.grid()
        tolEntry = tk.Entry(root)
        tolEntry.grid()

        Nmax = tk.Label(root, text="Ingrese el valor de Nmax")
        Nmax.grid()
        NmaxEntry = tk.Entry(root)
        NmaxEntry.grid()

        dropdown = tk.OptionMenu(root, errorSeleccionado, *error)
        dropdown.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: biseccion(
            funcionEntry.get(), float(aEntry.get()), float(
                bEntry.get()), float(tolEntry.get()),
            int(NmaxEntry.get()), root, operaciones, errorSeleccionado.get(), atras))
        calcular.grid()

    elif metodo == "Busqueda incremental":
        label = tk.Label(root, text="Busqueda incremental", font=("Arial", 20))
        label.grid()

        funcion = tk.Label(root, text="Ingrese la función")
        funcion.grid()
        funcionEntry = tk.Entry(root)
        funcionEntry.grid()

        x0 = tk.Label(root, text="Ingrese el valor de x0")
        x0.grid()
        x0Entry = tk.Entry(root)
        x0Entry.grid()

        h = tk.Label(root, text="Ingrese el valor de h")
        h.grid()
        hEntry = tk.Entry(root)
        hEntry.grid()

        Nmax = tk.Label(root, text="Ingrese el valor de Nmax")
        Nmax.grid()
        NmaxEntry = tk.Entry(root)
        NmaxEntry.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: busquedas(
            funcionEntry.get(), float(x0Entry.get()), float(hEntry.get()), int(NmaxEntry.get()), root, operaciones, atras))
        calcular.grid()

        print("Busqueda incremental")
    elif metodo == "Newton":
        label = tk.Label(root, text="Newton", font=("Arial", 20))
        label.grid()

        f = tk.Label(root, text="Ingrese la función")
        f.grid()
        fEntry = tk.Entry(root)
        fEntry.grid()

        derivada = tk.Label(root, text="Ingrese la derivada")
        derivada.grid()
        derivadaEntry = tk.Entry(root)
        derivadaEntry.grid()

        x0 = tk.Label(root, text="Ingrese el valor de x0")
        x0.grid()
        x0Entry = tk.Entry(root)
        x0Entry.grid()

        tol = tk.Label(root, text="Ingrese el valor de la tolerancia")
        tol.grid()
        tolEntry = tk.Entry(root)
        tolEntry.grid()

        Nmax = tk.Label(root, text="Ingrese el valor de Nmax")
        Nmax.grid()
        NmaxEntry = tk.Entry(root)
        NmaxEntry.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: newton_lambda(
            fEntry.get(), derivadaEntry.get(), float(x0Entry.get()), float(tolEntry.get()), int(NmaxEntry.get()), root, operaciones, atras))
        calcular.grid()

        print("Newton")
    elif metodo == "Punto fijo":
        print("Punto fijo")
    elif metodo == "Raices multiples":
        print("Raices multiples")
    elif metodo == "Secante":
        print("Secante")
    elif metodo == "Regla falsa":
        print("Regla falsa")
    elif metodo == "Cholesky":
        print("Cholesky")
    elif metodo == "Crout":
        print("Crout")
    elif metodo == "Doolittle":
        print("Doolittle")
    elif metodo == "Gauss simple":
        def calcularGauss(A_str, b_str):
            A_rows = A_str.split(';')
            A_values = [list(map(float, row.split(','))) for row in A_rows]
            A = np.array(A_values)
            b = np.array(list(map(float, b_str.split(','))))

            # Llamar a la función de eliminación gaussiana con las entradas proporcionadas
            x = gausspl(A, b)

            # Mostrar los resultados en la interfaz de Tkinter
            x_result.config(text="Valores de x: " + str(x))

        label = tk.Label(root, text="Eliminación Gaussiana", font=("Arial", 20))
        label.grid()

        A_label = tk.Label(root, text="Ingrese la matriz A (separada por comas, filas por punto y coma):")
        A_label.grid()
        A_entry = tk.Entry(root)
        A_entry.grid()

        b_label = tk.Label(root, text="Ingrese el vector b (separado por comas):")
        b_label.grid()
        b_entry = tk.Entry(root)
        b_entry.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: calcularGauss(
            A_entry.get(), b_entry.get()))
        calcular.grid()

        result_label = tk.Label(root, text="Resultados:")
        result_label.grid()

        x_result = tk.Label(root, text="Valores de x:")
        x_result.grid()
    elif metodo == "Gauss con pivoteo parcial":
        print("Gauss con pivoteo parcial")
    elif metodo == "Gauss con pivoteo total":
        print("Gauss con pivoteo total")
    elif metodo == "Gauss-Seidel":
        def calculargseidel(A_str, b_str, X0_str, tol_str, Nmax_str):
            A_rows = A_str.split(';')
            A_values = [list(map(float, row.split(','))) for row in A_rows]
            A = np.array(A_values)
            b = np.array(list(map(float, b_str.split(','))))
            X0 = np.array(list(map(float, X0_str.split(','))))
            tol = float(tol_str)
            Nmax = int(Nmax_str)

            result = gseidel(A, b, X0, tol, Nmax)

            x_result.config(text="Valores de x: " + str(result[0]))
            iter_result.config(text="Número de iteraciones: " + str(result[1]))
            error_result.config(text="Error: " + str(result[2]))

        label = tk.Label(root, text="Gauss-Seidel", font=("Arial", 20))
        label.grid()

        A_label = tk.Label(root, text="Ingrese la matriz A (separada por comas, filas por punto y coma):")
        A_label.grid()
        A_entry = tk.Entry(root)
        A_entry.grid()

        b_label = tk.Label(root, text="Ingrese el vector b (separado por comas):")
        b_label.grid()
        b_entry = tk.Entry(root)
        b_entry.grid()

        X0_label = tk.Label(root, text="Ingrese la aproximación inicial X0 (separado por comas):")
        X0_label.grid()
        X0_entry = tk.Entry(root)
        X0_entry.grid()

        tol_label = tk.Label(root, text="Ingrese la tolerancia:")
        tol_label.grid()
        tol_entry = tk.Entry(root)
        tol_entry.grid()

        Nmax_label = tk.Label(root, text="Ingrese el número máximo de iteraciones (Nmax):")
        Nmax_label.grid()
        Nmax_entry = tk.Entry(root)
        Nmax_entry.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: calculargseidel(
            A_entry.get(), b_entry.get(), X0_entry.get(), tol_entry.get(), Nmax_entry.get()))
        calcular.grid()

        result_label = tk.Label(root, text="Resultados")
        result_label.grid()

        x_result = tk.Label(root, text="Valores de x:")
        x_result.grid()

        iter_result = tk.Label(root, text="Número de iteraciones:")
        iter_result.grid()

        error_result = tk.Label(root, text="Error:")
        error_result.grid()
        print("Gauss-Seidel")
    elif metodo == "Jacobi":
        def calcularJacobi(A_str, b_str, X0_str, tol_str, Nmax_str):
            A_rows = A_str.split(';')
            A_values = [list(map(float, row.split(','))) for row in A_rows]
            A = np.array(A_values)
            b = np.array(list(map(float, b_str.split(','))))
            X0 = np.array(list(map(float, X0_str.split(','))))
            tol = float(tol_str)
            Nmax = int(Nmax_str)

            result = jacobi(A, b, X0, tol, Nmax)

            x_result.config(text="Valores de x: " + str(result[0]))
            iter_result.config(text="Número de iteraciones: " + str(result[1]))
            error_result.config(text="Error: " + str(result[2]))

        label = tk.Label(root, text="Jacobi", font=("Arial", 20))
        label.grid()

        A_label = tk.Label(root, text="Ingrese la matriz A (separada por comas, filas por punto y coma):")
        A_label.grid()
        A_entry = tk.Entry(root)
        A_entry.grid()

        b_label = tk.Label(root, text="Ingrese el vector b (separado por comas):")
        b_label.grid()
        b_entry = tk.Entry(root)
        b_entry.grid()

        X0_label = tk.Label(root, text="Ingrese la aproximación inicial X0 (separado por comas):")
        X0_label.grid()
        X0_entry = tk.Entry(root)
        X0_entry.grid()

        tol_label = tk.Label(root, text="Ingrese la tolerancia:")
        tol_label.grid()
        tol_entry = tk.Entry(root)
        tol_entry.grid()

        Nmax_label = tk.Label(root, text="Ingrese el número máximo de iteraciones (Nmax):")
        Nmax_label.grid()
        Nmax_entry = tk.Entry(root)
        Nmax_entry.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: calcularJacobi(
            A_entry.get(), b_entry.get(), X0_entry.get(), tol_entry.get(), Nmax_entry.get()))
        calcular.grid()

        result_label = tk.Label(root, text="Resultados")
        result_label.grid()

        x_result = tk.Label(root, text="Valores de x:")
        x_result.grid()

        iter_result = tk.Label(root, text="Número de iteraciones:")
        iter_result.grid()

        error_result = tk.Label(root, text="Error:")
        error_result.grid()
    elif metodo == "LU parcial":
        def calcularLuPar(A_str, b_str):
            A_rows = A_str.split(';')
            A_values = [list(map(float, row.split(','))) for row in A_rows]
            A = np.array(A_values)
            b = np.array(list(map(float, b_str.split(','))))

            # Llamar a la función de eliminación gaussiana con las entradas proporcionadas
            x = LUparcial(A, b)

            # Mostrar los resultados en la interfaz de Tkinter
            x_result.config(text="Valores de x: " + str(x))

        label = tk.Label(root, text="Eliminación Gaussiana", font=("Arial", 20))
        label.grid()

        A_label = tk.Label(root, text="Ingrese la matriz A (separada por comas, filas por punto y coma):")
        A_label.grid()
        A_entry = tk.Entry(root)
        A_entry.grid()

        b_label = tk.Label(root, text="Ingrese el vector b (separado por comas):")
        b_label.grid()
        b_entry = tk.Entry(root)
        b_entry.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: calcularLuPar(
            A_entry.get(), b_entry.get()))
        calcular.grid()

        result_label = tk.Label(root, text="Resultados:")
        result_label.grid()

        x_result = tk.Label(root, text="Valores de x:")
        x_result.grid()
        print("LU parcial")
    elif metodo == "LU simple":
        print("LU simple")
    elif metodo == "LaGrange":
        label = tk.Label(root, text="LaGrange", font=("Arial", 20))
        label.grid()

        x = tk.Label(root, text="Ingrese los valores de x separados por comas")
        x.grid()
        xEntry = tk.Entry(root)
        xEntry.grid()

        y = tk.Label(root, text="Ingrese los valores de y separados por comas")
        y.grid()
        yEntry = tk.Entry(root)
        yEntry.grid()

        punto = tk.Label(root, text="Ingrese el valor del punto")
        punto.grid()
        puntoEntry = tk.Entry(root)
        puntoEntry.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: lagrange(
            xEntry.get(), yEntry.get(), float(puntoEntry.get()), root, atras))
        calcular.grid()
    elif metodo == "Spline":
        print("Spline")
    elif metodo == "Diferencias divididas":
        label = tk.Label(root, text="Diferencias divididas",
                         font=("Arial", 20))
        label.grid()

        x = tk.Label(root, text="Ingrese los valores de x separados por comas")
        x.grid()
        xEntry = tk.Entry(root)
        xEntry.grid()

        y = tk.Label(root, text="Ingrese los valores de y separados por comas")
        y.grid()
        yEntry = tk.Entry(root)
        yEntry.grid()

        punto = tk.Label(
            root, text="Ingrese los puntos a evaluar separados por comas")
        punto.grid()
        puntoEntry = tk.Entry(root)
        puntoEntry.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: newtonInterpolacion(
            xEntry.get(), yEntry.get(), str(puntoEntry.get()), root, atras))
        calcular.grid()

    elif metodo == "Vandermonde":
        label = tk.Label(root, text="Vandermonde", font=("Arial", 20))
        label.grid()

        x = tk.Label(root, text="Ingrese los valores de x separados por comas")
        x.grid()
        xEntry = tk.Entry(root)
        xEntry.grid()

        y = tk.Label(root, text="Ingrese los valores de y separados por comas")
        y.grid()
        yEntry = tk.Entry(root)
        yEntry.grid()

        puntos = tk.Label(
            root, text="Ingrese los puntos a evaluar separados por comas")
        puntos.grid()
        puntosEntry = tk.Entry(root)
        puntosEntry.grid()

        calcular = tk.Button(root, text="Calcular", command=lambda: vandermonde(
            xEntry.get(), yEntry.get(), str(puntosEntry.get()), root, atras))
        calcular.grid()

    atras = tk.Button(root, text="Atras", command=lambda: inicio(root))
    atras.grid()


root.mainloop()
