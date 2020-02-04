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

"""
------------- DEFINICJE --------------
"""

global lista
global wybrane_kolumny
global Nowa_lista
global Naglowki


def donothig():
    x = 0


# wybieranie pliku csv

def wczytaj_plik():
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

    # wyswiet_l.config(text=fc)

    # tab1_Wybor.config(state="normal")
    # tab1_Zobacz.config(state="normal")


# Wybieranie kolumn do obliczeń na nich


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


def aktywacja():
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
                    msb.showinfo("Uwaga!", "Wybrana kolumna zawiera dane tekstowe!\nWybierz inną kolumnę!")


"""
    tab1_Wybor.config(state="normal")
    tab1_Wyswietls.config(state="normal")
    tab1_Wyswietls.config(state="normal")
"""


# Zapisz do pliku

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


# INNEEEEEEEEEEEEEEEEEE


def utworz_dataframe(dane, index, columny):
    np_w = np.array(dane)
    return pd.DataFrame(data=np_w, index=index, columns=columny)


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


def donothing():
    x = 0


"""
------------- ZAKLADKI FUNKCJE --------------
"""


# ------------- Funckje TAB 2 --------------

def Tworzenie_tabel_w_petli(dane, okno, poziom):
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

def Wypelanianie_tabeli_w_petli(dlugosc, okno, x):
    for y in range(dlugosc):
        okno.b2 = tkinter.Text(okno, width=10, height=1)
        okno.b2.insert('end', okno.Wyniki[y])
        okno.b2.config(state="disabled")
        okno.b2.grid(row=y + 2, column=x + 2)
        return y


class MiaryPol(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)

        self.funkcje = [
            'Wartość minimalna',
            'Wartość maksymalna',
            'Średnia arytmetyczna',
            # 'Średnia geometryczna',
            'Średnia harmoniczna',
            'Kwartyl dolny',
            'Mediana',
            'Kwartyl górny']
        self.save = []

        for x1 in range(len(Nowa_lista[0])):
            self.Wyniki = []
            self.Wyniki.append(np.nanmin(Nowa_lista[:, x1]))
            self.Wyniki.append(np.nanmax(Nowa_lista[:, x1]))
            self.Wyniki.append(np.nanmean(Nowa_lista[:, x1]))
            # self.Wyniki.append(stat.geometric_mean(Nowa_lista[:, x1]))
            self.Wyniki.append(stats.hmean(Nowa_lista[:, x1], axis=0, dtype=None))
            self.Wyniki.append(np.nanquantile(Nowa_lista[:, x1], q=0.25))
            self.Wyniki.append(np.nanmedian(np.sort(Nowa_lista[:, x1])))
            self.Wyniki.append(np.nanquantile(Nowa_lista[:, x1], q=0.75))
            self.save.append(self.Wyniki)

            Wypelanianie_tabeli_w_petli(len(self.funkcje), self, x1)

        Tworzenie_tabel_w_petli(Naglowki, self, poziom='True')

        Tworzenie_tabel_w_petli(self.funkcje, self, poziom='False')

        self.l1 = Button(self, text='Zapisz wyniki', command=self.zapisz)
        self.l1.grid(row=len(self.funkcje) + 3, column=len(Nowa_lista[0]) + 1, pady=10, sticky=W)

        self.wolny = Label(self, text=' ', padx=10, pady=10)
        self.wolny.grid(row=y + 4, column=x1 + 3)

    def zapisz(self):

        files = [('csv', '*.csv')]
        file_name = asksaveasfilename(filetypes=files, defaultextension=files)

        if file_name:
            utworz_dataframe(self.save, Naglowki, self.funkcje).to_csv(file_name, sep=';', encoding='utf-8-sig')


def miary_polozenia():
    klasa_wyniki = MiaryPol()
    klasa_wyniki.mainloop()


class MiaryZmi(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)

        self.funkcje = (
            'Wariancja',
            'Odchylenie standardowe',
            'Odchylenie przeciętne',
            'Klasyczny współczynnik zmienności',
            'Rozstęp',
            'Rozstęp międzykwartylowy',
            'Odchylenie ćwiartkowe',
            'Pozycyjny współczynnik zmienności')
        self.save = []

        for x1 in range(len(Nowa_lista[0])):
            self.Wyniki = []
            self.Wyniki.append(float(np.nanvar(Nowa_lista[:, x1])))
            self.Wyniki.append(np.nanstd(Nowa_lista[:, x1]))
            suma = 0
            for i in range(len(Nowa_lista)):
                suma = suma + mat.fabs(Nowa_lista[i, x1] - np.nanmean(Nowa_lista[:, x1]))
            self.Wyniki.append(suma / len(Nowa_lista[:, x1]))
            self.Wyniki.append((np.nanstd(Nowa_lista[:, x1]) / np.nanmean(Nowa_lista[:, x1])) * 100)
            self.Wyniki.append(np.ptp(Nowa_lista[:, x1]))
            self.Wyniki.append(stats.iqr(Nowa_lista[:, x1]))
            self.Wyniki.append(stats.iqr(Nowa_lista[:, x1]))
            self.Wyniki.append(((stats.iqr(Nowa_lista[:, x1]) / 2) / np.nanmedian(np.sort(Nowa_lista[:, x1]))) * 100)
            self.save.append(self.Wyniki)

            for y1 in range(len(self.funkcje)):
                self.b2 = tkinter.Text(self, width=10, height=1)
                self.b2.insert('end', self.Wyniki[y1])
                self.b2.config(state="disabled")
                self.b2.grid(row=y1 + 2, column=x1 + 2)

        for x in range(len(Nowa_lista[0])):
            self.pomoc = tkinter.StringVar(self)
            self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
            self.a = Naglowki[x]
            self.pomoc.set(self.a)
            self.pokaz.grid(row=1, column=x + 2)

        for y in range(len(self.funkcje)):
            self.pomoc = tkinter.StringVar(self)
            self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
            self.a = self.funkcje[y]
            self.pomoc.set(self.a)
            self.pokaz.grid(row=y + 2, column=1)

        self.l1 = Button(self, text='Zapisz wyniki', command=self.zapisz)
        self.l1.grid(row=len(self.funkcje) + 3, column=len(Nowa_lista[0]) + 1, pady=10, sticky=W)

        self.wolny = Label(self, text=' ', padx=10, pady=10)
        self.wolny.grid(row=y1 + 4, column=x1 + 3)

    def zapisz(self):
        files = [('csv', '*.csv')]
        file_name = asksaveasfilename(filetypes=files, defaultextension=files)

        if file_name:
            utworz_dataframe(self.save, Naglowki, self.funkcje).to_csv(file_name, sep=';', encoding='utf-8-sig')


def miary_zmiennosci():
    klasa_wyniki = MiaryZmi()
    klasa_wyniki.mainloop()


def kappa():
    x = 0


class MiaryAsy(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)

        self.funkcje = ('Wskaźnik skośności',
                        'Pozycyjny wskaźnik skośności',
                        'Pozycyjny współczynnik asymetrii',
                        'Klasyczny współczynnik asymetrii',
                        'Współczynnik kurtozy',
                        'Współczynnik ekscesu')
        self.save = []

        for x1 in range(len(Nowa_lista[0])):
            sko = stats.skew(Nowa_lista[:, x1])
            y = np.sort(Nowa_lista[:, x1])
            poz_sko = np.nanquantile(y, q=0.75) + np.nanquantile(y, q=0.25) - 2 * (np.nanmedian(y))
            poz_asy = poz_sko / (np.nanquantile(y, q=0.75) - np.nanquantile(y, q=0.25))
            mean = np.nanmean(Nowa_lista[:, x1])
            a = 0
            for i in range(len(Nowa_lista[:, x1])):
                a = a + ((Nowa_lista[i, x1] - mean) ** 3)
                m3 = a / len(Nowa_lista[:, x1])
            kla_asy = m3 / (np.nanstd(Nowa_lista[:, x1]) ** 3)
            kurtoza = stats.kurtosis(Nowa_lista[:, x1], axis=0, fisher=False)
            k1 = (stats.kurtosis(Nowa_lista[:, x1], axis=0, fisher=False)) - 3

            self.Wyniki = []
            self.Wyniki.append(sko)
            self.Wyniki.append(poz_sko)
            self.Wyniki.append(poz_asy)
            self.Wyniki.append(kla_asy)
            self.Wyniki.append(kurtoza)
            self.Wyniki.append(k1)

            self.save.append(self.Wyniki)

            for y1 in range(len(self.funkcje)):
                self.b2 = tkinter.Text(self, width=10, height=1)
                self.b2.insert('end', self.Wyniki[y1])
                self.b2.config(state="disabled")
                self.b2.grid(row=y1 + 2, column=x1 + 2)

        for x in range(len(Nowa_lista[0])):
            self.pomoc = tkinter.StringVar(self)
            self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
            self.a = Naglowki[x]
            self.pomoc.set(self.a)
            self.pokaz.grid(row=1, column=x + 2)

        for y in range(len(self.funkcje)):
            self.pomoc = tkinter.StringVar(self)
            self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
            self.a = self.funkcje[y]
            self.pomoc.set(self.a)
            self.pokaz.grid(row=y + 2, column=1)

        self.l1 = Button(self, text='Zapisz wyniki', command=self.zapisz)
        self.l1.grid(row=len(self.funkcje) + 3, column=len(Nowa_lista[0]) + 1, pady=10, sticky=W)

        self.wolny = Label(self, text=' ', padx=10, pady=10)
        self.wolny.grid(row=y1 + 4, column=x1 + 3)

    def zapisz(self):

        files = [('csv', '*.csv')]
        file_name = asksaveasfilename(filetypes=files, defaultextension=files)

        if file_name:
            utworz_dataframe(self.save, Naglowki, self.funkcje).to_csv(file_name, sep=';', encoding='utf-8-sig')


def miary_asymetrii():
    klasa_wyniki = MiaryAsy()
    klasa_wyniki.mainloop()


def kor_per():
    a = 0


def kow():
    a = 0


def kor_sper():
    a = 0


def reg_lin():
    a = 0


def reg_wyk():
    a = 0


def reg_kwadt():
    a = 0

# ------------- Funckje TAB 5 --------------
