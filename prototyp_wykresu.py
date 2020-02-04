import csv
import statistics as stat
import tkinter
from tkinter import messagebox as msb
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.filedialog import *
import scipy.stats as stats
import pandas as pd
import numpy as np
import math as mat
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

"""

with open('pokemon.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    lista = list(reader)
    lista = np.array(lista)

Nowa_lista = lista[1:,6:8]
Nowa_lista = Nowa_lista.astype(np.float)


def rysuj_wykres():

    v = Nowa_lista[:, 0]
    p = Nowa_lista[:, 1]

    fig = Figure()
    ax = fig.add_subplot(111)
    ax.plot(v, color='#4285F4', linewidth=0.51)
    ax.plot(p, color='#DB4437', linewidth=0.51)

    ax.invert_yaxis()

    ax.set_title("Wykres ", fontsize=16)
    ax.set_ylabel("Y", fontsize=14)
    ax.set_xlabel("X", fontsize=14)

    rysuj = Toplevel()
    canvas = FigureCanvasTkAgg(fig, master=rysuj)
    canvas.get_tk_widget().pack()
    canvas.draw()


top= Tk()

b1 = Button(top, text='mama', command=rysuj_wykres)
b1.pack()

top.mainloop()

"""



x = np.array([[1, 2, 3], [4, 5, 6]])


print(x)


def wybierz_do_wypisania(dane, okno, ile_wierszy):
    for x in range(len(dane)):
        for y in range(ile_wierszy):
            wez = tkinter.StringVar(okno)
            pokaz = tkinter.Label(okno, textvariable=wez)
            a = lista[y, x]
            wez.set(a)
            pokaz.grid(row=y, column=x)
