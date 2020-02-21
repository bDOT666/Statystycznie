

import csv
import tkinter
from tkinter import messagebox as msb
from tkinter import scrolledtext
from tkinter.filedialog import *
import scipy.stats as stats
import pandas as pd
import numpy as np
import math as mat
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('TkAgg')


#


#

"""
#  ------------- KONTROLA DANYCH --------------
"""

#


#

"""
global lista
global wybrane_kolumny
global Nowa_lista
global Naglowki
"""

slownik = {}
lista_boxow =[]


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


class WybieranieKolumn(tkinter.Tk):
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
    klasa_kolumny = WybieranieKolumn()
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
    print(Naglowki)


def wybierz_do_wypisania(dane, okno, ile_wierszy):
    for x in range(len(dane[0])):
        for y in range(ile_wierszy):
            wez = tkinter.StringVar(okno)
            pokaz = tkinter.Label(okno, textvariable=wez)
            a = dane[y, x]
            wez.set(a)
            pokaz.grid(row=y, column=x)


class PodgladWybrane(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)

        if len(Nowa_lista[:, 0]) > 20:
            wybierz_do_wypisania(Nowa_lista, self, 20)
        else:
            wybierz_do_wypisania(Nowa_lista, self, len(Nowa_lista[:, 0]))


def podglad_kolumn():
    klasa_wyniki = PodgladWybrane()
    klasa_wyniki.mainloop()


class PodgladWszystko(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)

        if len(Nowa_lista[:, 0]) > 20:
            wybierz_do_wypisania(lista, self, 20)
        else:
            wybierz_do_wypisania(lista, self, len(lista[:, 0]))


def podglad_wszystko():
    wyswietl_wszystko = PodgladWszystko()
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


#


#

"""
#  ------------- WSPEIRAJĄCE --------------
"""

#


#


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
    pass


def donothing():
    pass


#


#

"""
#                       Miary Położenia
"""

#


#


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

            mini = np.nanmin(Nowa_lista[:, x1])
            maxi = np.nanmax(Nowa_lista[:, x1])
            sr_a = np.nanmean(Nowa_lista[:, x1])
            # sr_g = stat.geometric_mean(Nowa_lista[:, x1])
            sr_h = stats.hmean(Nowa_lista[:, x1], axis=0, dtype=None)
            kw_d = np.nanquantile(Nowa_lista[:, x1], q=0.25)
            med = np.nanmedian(np.sort(Nowa_lista[:, x1]))
            kw_g = np.nanquantile(Nowa_lista[:, x1], q=0.75)

            self.Wyniki.append(mini)
            self.Wyniki.append(maxi)
            self.Wyniki.append(sr_a)
            # self.Wyniki.append(sr_g)
            self.Wyniki.append(sr_h)
            self.Wyniki.append(kw_d)
            self.Wyniki.append(med)
            self.Wyniki.append(kw_g)

            self.save.append(self.Wyniki)

            wypelanianie_tabeli_w_petli(len(self.funkcje), self, x1)

        tworzenie_tabel_w_petli(Naglowki, self, poziom='True')

        tworzenie_tabel_w_petli(self.funkcje, self, poziom='False')

        self.l1 = Button(self, text='Zapisz wyniki', command=self.zapisz)
        self.l1.grid(row=len(self.funkcje) + 3, column=len(Nowa_lista[0]) + 1, pady=10, sticky=W)

        self.wolny = Label(self, text=' ', padx=10, pady=10)
        self.wolny.grid(row=len(self.funkcje) + 3, column=len(Nowa_lista[0]) + 3)

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

            war = float(np.nanvar(Nowa_lista[:, x1]))
            odch_s = np.nanstd(Nowa_lista[:, x1])
            suma = 0
            for i in range(len(Nowa_lista)):
                suma = suma + mat.fabs(Nowa_lista[i, x1] - np.nanmean(Nowa_lista[:, x1]))
            odch_p = suma / len(Nowa_lista[:, x1])
            klas_wsp_z = (np.nanstd(Nowa_lista[:, x1]) / np.nanmean(Nowa_lista[:, x1])) * 100
            roz = np.ptp(Nowa_lista[:, x1])
            roz_m = stats.iqr(Nowa_lista[:, x1])
            odch_c = stats.iqr(Nowa_lista[:, x1])
            poz_wsp_z = ((stats.iqr(Nowa_lista[:, x1]) / 2) / np.nanmedian(np.sort(Nowa_lista[:, x1]))) * 100

            self.Wyniki.append(war)
            self.Wyniki.append(odch_s)
            self.Wyniki.append(odch_p)
            self.Wyniki.append(klas_wsp_z)
            self.Wyniki.append(roz)
            self.Wyniki.append(roz_m)
            self.Wyniki.append(odch_c)
            self.Wyniki.append(poz_wsp_z)

            self.save.append(self.Wyniki)

            wypelanianie_tabeli_w_petli(len(self.funkcje), self, x1)

        tworzenie_tabel_w_petli(Naglowki, self, poziom='True')

        tworzenie_tabel_w_petli(self.funkcje, self, poziom='False')

        self.l1 = Button(self, text='Zapisz wyniki', command=self.zapisz)
        self.l1.grid(row=len(self.funkcje) + 3, column=len(Nowa_lista[0]) + 1, pady=10, sticky=W)

        self.wolny = Label(self, text=' ', padx=10, pady=10)
        self.wolny.grid(row=len(self.funkcje) + 3, column=len(Nowa_lista[0]) + 3)

    def zapisz(self):
        files = [('csv', '*.csv')]
        file_name = asksaveasfilename(filetypes=files, defaultextension=files)

        if file_name:
            utworz_dataframe(self.save, Naglowki, self.funkcje).to_csv(file_name, sep=';', encoding='utf-8-sig')


def miary_zmiennosci():
    klasa_wyniki = MiaryZmi()
    klasa_wyniki.mainloop()


def kappa():
    pass


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

            wypelanianie_tabeli_w_petli(len(self.funkcje), self, x1)

        tworzenie_tabel_w_petli(Naglowki, self, poziom='True')

        tworzenie_tabel_w_petli(self.funkcje, self, poziom='False')

        self.l1 = Button(self, text='Zapisz wyniki', command=self.zapisz)
        self.l1.grid(row=len(self.funkcje) + 3, column=len(Nowa_lista[0]) + 1, pady=10, sticky=W)

        self.wolny = Label(self, text=' ', padx=10, pady=10)
        self.wolny.grid(row=len(self.funkcje) + 3, column=len(Nowa_lista[0]) + 3)

    def zapisz(self):

        files = [('csv', '*.csv')]
        file_name = asksaveasfilename(filetypes=files, defaultextension=files)

        if file_name:
            utworz_dataframe(self.save, Naglowki, self.funkcje).to_csv(file_name, sep=';', encoding='utf-8-sig')


def miary_asymetrii():
    klasa_wyniki = MiaryAsy()
    klasa_wyniki.mainloop()


def kor_per():
    pass


def kow():
    pass


def kor_sper():
    pass


def reg_lin():
    pass


def reg_wyk():
    pass


def reg_kwadt():
    pass


#


#

"""
#                       Wykresy
"""

#


#


def kolumny_do_wykresow(ram2):
    slownik.clear()

    for cb in lista_boxow:
        cb.destroy()
    lista_boxow.clear()

    for kolumna in Naglowki:
        slownik[kolumna] = tkinter.IntVar()
        c = tkinter.Checkbutton(ram2, text=kolumna, variable=slownik[kolumna])
        c.pack()
        lista_boxow.append(c)


def wyjmij_kolumny_wykresy():
    do_wykresu = []
    zmienne = []

    for key, value in slownik.items():
        if value.get() > 0:
            i = Naglowki.tolist().index(key)
            zmienne.append(i)
            print(i)
            print(key)
    for i in zmienne:
        do_wykresu.append(Nowa_lista[:, i])
    return do_wykresu


def konwertuj_przed_wykresem():
    do_wykresu = wyjmij_kolumny_wykresy()
    do_wykresu = np.array(do_wykresu)
    do_wykresu = do_wykresu.astype(np.float)
    return do_wykresu


def rysuj_wykres(e1, e2, e3):
    do_wykresu = konwertuj_przed_wykresem()
    # W tym miejscu masz wyjęte wybrane wcześniej kolumny
    # 'do_wykresu' to array z tymi wybranymi kolumnami
    # ich liczba nie musi sięzgadzać, ale jak zrobisz samo wywolywanie  wykresow to dodadm obostrzenie, żeby błąd
    # wyskakiwał i podawał zakres ile możesz kolumn wybrać do danego wykresu
    nazwa_wykres = e1.get()
    nazwa_x = e2.get()
    nazwa_y = e3.get()
    v = do_wykresu[0]
    p = do_wykresu[1]

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
