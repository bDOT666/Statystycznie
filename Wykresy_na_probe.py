import csv
import statistics as stat
import tkinter
import numpy as np
import pandas as pd
import math as mat
from tkinter import messagebox as msb
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.filedialog import *
import scipy.stats as stats
import matplotlib
matplotlib.use('TkAgg')
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *




with open('C:\Officjum Inkwizytorskie\pliki\pokemon.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    lista = list(reader)
    lista = np.array(lista)

Nowa_lista = lista[:, 6:8]
Naglowki = Nowa_lista[0]
Nowa_lista = lista[1:, 6:8]

print(Naglowki)

def kolumny_do_wykresow():

    slownik.clear()

    for cb in lista_boxow:
        cb.destroy()
    lista_boxow.clear()

    for kolumna in Naglowki:
        slownik[kolumna] = tkinter.IntVar()
        c = tkinter.Checkbutton(top, text=kolumna, variable=slownik[kolumna])
        c.pack()
        lista_boxow.append(c)


def wyjmij_kolumny_wykresy():

    do_wykresu = []
    zmienne = []

    for key, value in slownik.items():
        if value.get() > 0:
            i = Naglowki.tolist().index(key)
            zmienne.append(i)

    for i in zmienne:
        do_wykresu.append(Nowa_lista[:, i])
    return do_wykresu


def rysuj_wykres():
    do_wkresu = wyjmij_kolumny_wykresy()
    do_wkresu = np.array(do_wkresu)

    do_wkresu = do_wkresu.astype(np.float)
    # W tym miejscu masz wyjęte wybrane wcześniej kolumny
    # 'do_wykresu' to array z tymi wybranymi kolumnami
    # ich liczba nie musi sięzgadzać, ale jak zrobisz samo wywolywanie  wykresow to dodadm obostrzenie, żeby błąd
    # wyskakiwał i podawał zakres ile możesz kolumn wybrać do danego wykresu


    kolumny = do_wkresu.astype(np.float)

    v = kolumny[0]
    p = kolumny[1]

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


top = Tk()

slownik = {}
lista_boxow =[]

b1 = Button(top, text='pokaż kolumny', command=kolumny_do_wykresow)
b1.pack()

b2 = Button(top, text='wyswietl zaznaczone kolumny i stworz wykres', command=rysuj_wykres)
b2.pack()

top.mainloop()















