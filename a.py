import math
from seleccion_metodos import definirMetodo
import tkinter as tk
fx = input("Enter a polynomial: ")


root = tk.Tk()

root.geometry("500x500")

function = tk.Label(root, text="Ingrese la función")
function.pack()
functionEntry = tk.Entry(root)
functionEntry.pack()
def f(x): return eval(functionEntry.get())


a = math.exp(1)

root.mainloop()
