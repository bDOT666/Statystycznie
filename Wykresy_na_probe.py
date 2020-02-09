import csv
import statistics as stat
import tkinter as tk
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

try:
    Nowa_lista = Nowa_lista.astype(np.float)
except:
    try:
        Nowa_lista = Nowa_lista[1:len(Nowa_lista), :].astype(np.float)
    except:
        Nowa_lista = np.char.replace(Nowa_lista, ',', '.')
        try:
            Nowa_lista = Nowa_lista.astype(np.float)
        except:
            try:
                Nowa_lista = Nowa_lista[1:len(Nowa_lista), :].astype(np.float)
            except:
                msb.showinfo("Uwaga!", "Wybrane kolumny zawierają dane tekstowe!\nWybierz inne kolumny!")


def kolumny_do_wykresow():

    slownik.clear()

    for cb in lista_boxow:
        cb.destroy()
    lista_boxow.clear()

    for kolumna in Naglowki:
        slownik[kolumna] = tk.IntVar()
        c = tk.Checkbutton(top, text=kolumna, variable=slownik[kolumna])
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
    nazwa_wykres = e1.get()
    nazwa_x = e2.get()
    nazwa_y = e3.get()
    v = do_wkresu[0]
    p = do_wkresu[1]

    fig = Figure()
    ax = fig.add_subplot(111)
    ax.plot(v, color='#4285F4', linewidth=0.51)
    ax.plot(p, color='#DB4437', linewidth=0.51)

    ax.invert_yaxis()

    ax.set_title(nazwa_wykres, fontsize=16)
    ax.set_ylabel(nazwa_x, fontsize=14)
    ax.set_xlabel(nazwa_y, fontsize=14)

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

l1 = tk.Label(top, text="Nazwa Wykresu")
e1 = tk.Entry(top, textvariable='Nazwa Wykresu')
l2 = tk.Label(top, text="Os X")
e2 = tk.Entry(top, textvariable='X')
l3 = tk.Label(top, text="Os Y")
e3 = tk.Entry(top, textvariable='Y')
l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()

top.mainloop()















