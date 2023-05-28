from tkinter import *


def tabla(lst, root):
    total_rows = len(lst)
    total_columns = len(lst[0])

    root.columnconfigure(0, weight=0)

    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(root, width=20, fg='black',
                      font=('Arial', 10))

            e.grid(row=i+1, column=j)
            e.insert(END, lst[i][j])

    scrollx = Scrollbar(root, orient=HORIZONTAL)
    scrollx.grid(sticky=S)
