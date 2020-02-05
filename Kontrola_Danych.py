

import csv
import tkinter
from tkinter import messagebox as msb
from tkinter import scrolledtext
from tkinter.filedialog import *
import scipy.stats as stats
import pandas as pd
import numpy as np
import math as mat

"""
------------- DEFINICJE --------------
"""

global lista
global wybrane_kolumny
global Nowa_lista
global Naglowki


def wczytaj_plik(scierzeka, przycisk_1, przycisk_2):
    global lista
    fc = tkinter.filedialog.askopenfilename(
        initialdir='/',
        title='Wybierz plik csv',
        filetypes=[('text files', '.csv')])
    f = open(fc, 'r')
    dialect = csv.Sniffer().sniff(f.read(1024), delimiters=";, ")
    f.seek(0)
    reader = csv.reader(f, dialect)
    lista = list(reader)
    lista = np.array(lista)

    scierzeka.config(text=fc)
    odpal(przycisk_1)
    odpal(przycisk_2)


class Wybieranie_Kolumn(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)

        # ustawienie

        frame4 = Frame(self)
        frame5 = Frame(self)
        frame6 = Frame(self)
        frame7 = Frame(self)
        frame8 = Frame(self)
        frame9 = Frame(self)
        frame10 = Frame(self)
        frame4.grid(row=1, column=0, rowspan=5, sticky=W + E)
        frame5.grid(row=1, column=2, rowspan=5, sticky=W + E)
        frame6.grid(row=6, column=2, sticky=W + E)
        frame7.grid(row=1, column=1, sticky=W + E)
        frame8.grid(row=2, column=1, sticky=W + E)
        frame9.grid(row=4, column=1, sticky=W + E)
        frame10.grid(row=5, column=1, sticky=W + E)

        #   lista z tego pobieram

        self.Rama1 = tkinter.Frame(frame4)
        self.Pasek = tkinter.Scrollbar(self.Rama1)
        self.ListaBox = tkinter.Listbox(self.Rama1)
        self.ListaBox.delete(0, tkinter.END)
        for i in range(len(lista[0])):
            self.ListaBox.insert(tkinter.END, lista[0, i])
        self.Pasek['command'] = self.ListaBox.yview
        self.ListaBox['yscrollcommand'] = self.Pasek.set
        self.ListaBox.bind('<<ListboxSelect>>')

        #   Lista do tego pobieram i przyciski

        self.Rama2 = tkinter.Frame(frame5)
        self.Pasek2 = tkinter.Scrollbar(self.Rama2)
        self.ListaBox2 = tkinter.Listbox(self.Rama2)
        self.Pasek2['command'] = self.ListaBox2.yview
        self.ListaBox2['yscrollcommand'] = self.Pasek2.set
        self.ListaBox2.bind('<<ListboxSelect>>')

        self.B_wybor = tkinter.Button(frame6, text='OK', command=self.wyjmij_z_listy)
        self.B_jedna_plus = tkinter.Button(frame7, text='>', command=self.daj_jedno)
        self.B_wszystkie_plus = tkinter.Button(frame8, text='>>', command=self.dodaj_wszystki)
        self.B_jedna_minus = tkinter.Button(frame9, text='< ', command=self.usun_jedno)
        self.B_wszystkie_minus = tkinter.Button(frame10, text='<< ', command=self.usun_wszystki)

        # packi

        self.Rama1.pack()
        self.Pasek.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.ListaBox.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.Rama2.pack()
        self.Pasek2.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.ListaBox2.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.B_wybor.pack()
        self.B_jedna_plus.pack()
        self.B_wszystkie_plus.pack()
        self.B_jedna_minus.pack()
        self.B_wszystkie_minus.pack()

    def daj_jedno(self):
        a = str((self.ListaBox.get(self.ListaBox.curselection())))
        self.ListaBox2.insert(tkinter.END, a)

    def dodaj_wszystki(self):
        self.ListaBox2.delete(0, tkinter.END)
        for i in range(len(lista[0])):
            self.ListaBox2.insert(tkinter.END, lista[0, i])

    def usun_jedno(self):
        self.ListaBox2.delete(tkinter.ANCHOR)

    def usun_wszystki(self):
        self.ListaBox2.delete(0, tkinter.END)

    def wyjmij_z_listy(self):
        global wybrane_kolumny
        wybrane_kolumny = list(self.ListaBox2.get(0, tkinter.END))
        # Aktywoj.config(state="normal")
        self.destroy()


def wybierz_kolumny():
    klasa_kolumny = Wybieranie_Kolumn()
    klasa_kolumny.mainloop()


def zatwierdz_kolumny(przycisk_1, przycisk_2):
    global Nowa_lista
    global Naglowki
    Nowa_lista = np.empty([len(lista), 0])

    ii = 0
    while ii < len(wybrane_kolumny):
        a = wybrane_kolumny[ii]
        for i, j in enumerate(lista[0]):
            if j == a:
                Nowa_lista = np.append(Nowa_lista, lista[:, i:i + 1], axis=1)
        ii = ii + 1
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

    odpal(przycisk_1)
    odpal(przycisk_2)


def wybierz_do_wypisania(dane, okno, ile_wierszy):
    for x in range(len(dane[0])):
        for y in range(ile_wierszy):
            wez = tkinter.StringVar(okno)
            pokaz = tkinter.Label(okno, textvariable=wez)
            a = dane[y, x]
            wez.set(a)
            pokaz.grid(row=y, column=x)


class Podglad_Wybrane(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)

        if len(Nowa_lista[:, 0]) > 20:
            wybierz_do_wypisania(Nowa_lista, self, 20)
        else:
            wybierz_do_wypisania(Nowa_lista, self, len(Nowa_lista[:, 0]))


def podglad_kolumn():
    klasa_wyniki = Podglad_Wybrane()
    klasa_wyniki.mainloop()


class Podglad_Wszystko(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)

        if len(Nowa_lista[:, 0]) > 20:
            wybierz_do_wypisania(lista, self, 20)
        else:
            wybierz_do_wypisania(lista, self, len(lista[:, 0]))


def podglad_wszystko():
    wyswietl_wszystko = Podglad_Wszystko()
    wyswietl_wszystko.mainloop()


def zapis_pliku():
    save = pd.DataFrame(data=Nowa_lista)

    files = [('csv', '*.csv')]
    file_name = asksaveasfilename(filetypes=files, defaultextension=files)

    if file_name:
        save.to_csv(file_name, sep=';', encoding='utf-8-sig')


def notatnik():
    okno = Tk()
    okno.title("Notatki")
    okno.geometry('350x810')
    notatki = scrolledtext.ScrolledText(okno, width=40, height=50)
    notatki.grid(column=0, row=0)
    okno.mainloop()


"""
------------- WSPEIRAJĄCE --------------
"""


def odpal(tabela):
    tabela.config(state="normal")


def utworz_dataframe(dane, index, columny):
    np_w = np.array(dane)
    return pd.DataFrame(data=np_w, index=index, columns=columny)


def tworzenie_tabel_w_petli(dane, okno, poziom):
    if poziom == 'True':
        for x in range(len(dane)):
            wez = tkinter.StringVar(okno)
            pokaz = tkinter.Label(okno, textvariable=wez)
            a = dane[x]
            wez.set(a)
            pokaz.grid(row=1, column=x + 2)
    else:
        for y in range(len(dane)):
            wez = tkinter.StringVar(okno)
            pokaz = tkinter.Label(okno, textvariable=wez)
            a = dane[y]
            wez.set(a)
            pokaz.grid(row=y + 2, column=1)


def wypelanianie_tabeli_w_petli(dlugosc, okno, x):
    for y in range(dlugosc):
        okno.b2 = tkinter.Text(okno, width=10, height=1)
        okno.b2.insert('end', okno.Wyniki[y])
        okno.b2.config(state="disabled")
        okno.b2.grid(row=y + 2, column=x + 2)



def donothig():
    x = 0


def donothing():
    x = 0

