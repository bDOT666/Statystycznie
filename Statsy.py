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

statystyka = tkinter.Tk()

"""
------------- DEFINICJE --------------
"""

# wybieranie pliku csv


def wczytaj_plik():
    global lista
    fc = tkinter.filedialog.askopenfilename(
        parent=statystyka, initialdir='/',
        title='Wybierz plik csv',
        filetypes=[('text files', '.csv')]
    )
    f = open(fc, 'r')
    dialect = csv.Sniffer().sniff(f.read(1024), delimiters=";, ")
    f.seek(0)
    reader = csv.reader(f, dialect)
    lista = list(reader)
    lista = np.array(lista)

    wyswiet_l.config(text=fc)

    tab1_Wybor.config(state="normal")
    tab1_Zobacz.config(state="normal")


# Wybieranie kolumn do obliczeń na nich


class Kolumny(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)
        self.naglowki = lista[0]

        # ustawienie

        frame1 = Frame(self)
        frame2 = Frame(self)
        frame4 = Frame(self)
        frame3 = Frame(self)
        frame5 = Frame(self)
        frame6 = Frame(self)
        frame7 = Frame(self)
        frame8 = Frame(self)
        frame9 = Frame(self)
        frame10 = Frame(self)
        frame1.grid(row=0, column=0, sticky=W + E)
        frame2.grid(row=0, column=2, sticky=W + E)
        frame3.grid(row=0, column=1, sticky=W + E)
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
        for i in range(len(self.naglowki)):
            self.ListaBox.insert(tkinter.END, self.naglowki[i])
        self.Pasek['command'] = self.ListaBox.yview
        self.ListaBox['yscrollcommand'] = self.Pasek.set
        self.ListaBox.bind('<<ListboxSelect>>')

        #   Lista do tego pobieram

        self.Rama2 = tkinter.Frame(frame5)
        self.Pasek2 = tkinter.Scrollbar(self.Rama2)
        self.ListaBox2 = tkinter.Listbox(self.Rama2)
        self.Pasek2['command'] = self.ListaBox2.yview
        self.ListaBox2['yscrollcommand'] = self.Pasek2.set
        self.ListaBox2.bind('<<ListboxSelect>>')

        # przyciski

        self.B_jedna_plus = tkinter.Button(frame7, text='>', command=self.daj_jedno)
        self.B_wszystkie_plus = tkinter.Button(frame8, text='>>', command=self.dodaj_wszystki)
        self.B_jedna_minus = tkinter.Button(frame9, text='< ', command=self.usun_jedno)
        self.B_wszystkie_minus = tkinter.Button(frame10, text='<< ', command=self.usun_wszystki)
        self.B_wybor = tkinter.Button(frame6, text='OK', command=self.wyjmij_z_listy)

        # packi

        self.Pasek.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.ListaBox.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.Rama1.pack()

        self.Pasek2.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.ListaBox2.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.Rama2.pack()

        self.B_jedna_plus.pack()
        self.B_jedna_minus.pack()
        self.B_wszystkie_plus.pack()
        self.B_wszystkie_minus.pack()
        self.B_wybor.pack()

    def nagluwek_jest(self):
        self.ListaBox.delete(0, tkinter.END)
        for i in range(len(self.naglowki)):
            self.ListaBox.insert(tkinter.END, self.naglowki[i])

    def dodaj_wszystki(self):
        self.ListaBox2.delete(0, tkinter.END)
        for i in range(len(self.naglowki)):
            self.ListaBox2.insert(tkinter.END, self.naglowki[i])

    def daj_jedno(self):
        a = str((self.ListaBox.get(self.ListaBox.curselection())))
        self.ListaBox2.insert(tkinter.END, a)

    def usun_wszystki(self):
        self.ListaBox2.delete(0, tkinter.END)

    def usun_jedno(self):
        self.ListaBox2.delete(tkinter.ANCHOR)

    def wyjmij_z_listy(self):
        global Wybrane_kolumny
        Wybrane_kolumny = list(self.ListaBox2.get(0, tkinter.END))
        global Nowe_naglu
        Nowe_naglu = self.naglowki
        Aktywoj.config(state="normal")
        self.destroy()


def klasa_definicja():
    klasa_kolumny = Kolumny()
    klasa_kolumny.mainloop()


def aktywacja():
    global Nowe_naglu
    global Nowa_lista
    global Naglowki
    Nowa_lista = np.empty([len(lista), 0])

    ii = 0
    while ii < len(Wybrane_kolumny):
        a = Wybrane_kolumny[ii]
        for i, j in enumerate(Nowe_naglu):
            if j == a:
                Nowa_lista = np.append(Nowa_lista, lista[:, i:i + 1], axis=1)
        ii = ii + 1
    Naglowki = Nowa_lista

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

    tab1_Wybor.config(state="normal")
    tab1_Wyswietls.config(state="normal")
    tab1_Wyswietls.config(state="normal")


    """
    a = len(Nowa_lista[0])
    if a == 1:
    # jEDNA
        t2_r1_b1.config(state="normal")
        t2_r1_b2.config(state="normal")
        t2_r1_b3.config(state="normal")
        t3_r1_b1.config(state="normal")
        t3_r1_b2.config(state="normal")
        t3_r1_b3.config(state="normal")
        t3_r2_b1.config(state="normal")
        t3_r3_b1.config(state="normal")
        t3_r3_b2.config(state="normal")
        t4_r1_b1.config(state="normal")
        t4_r2_b1.config(state="normal")
        t4_r3_b1.config(state="normal")
        t4_r4_b1.config(state="normal")
    #   DWIE
        t2_r2_b1.config(state="disabled")
        t2_r2_b2.config(state="disabled")
        t2_r2_b3.config(state="disabled")
        t2_r3_b1.config(state="disabled")
        t2_r3_b2.config(state="disabled")
        t2_r3_b3.config(state="disabled")
        t3_r4_b1.config(state="disabled")
        t3_r4_b2.config(state="disabled")
        t3_r4_b3.config(state="disabled")
        t3_r5_b1.config(state="disabled")
        t3_r5_b2.config(state="disabled")
        t3_r6_b1.config(state="disabled")
        t3_r6_b2.config(state="disabled")
        t4_r5_b1.config(state="disabled")
        t4_r6_b1.config(state="disabled")
        t4_r7_b1.config(state="disabled")
        t4_r8_b1.config(state="disabled")
        t4_r9_b1.config(state="disabled")
    elif a == 2:
    # jEDNA
        t2_r1_b1.config(state="disabled")
        t2_r1_b2.config(state="disabled")
        t2_r1_b3.config(state="disabled")
        t3_r1_b1.config(state="disabled")
        t3_r1_b2.config(state="disabled")
        t3_r1_b3.config(state="disabled")
        t3_r2_b1.config(state="disabled")
        t3_r3_b1.config(state="disabled")
        t3_r3_b2.config(state="disabled")
        t4_r1_b1.config(state="disabled")
        t4_r2_b1.config(state="disabled")
        t4_r3_b1.config(state="disabled")
        t4_r4_b1.config(state="disabled")
    #   DWIE
        t2_r2_b1.config(state="normal")
        t2_r2_b2.config(state="normal")
        t2_r2_b3.config(state="normal")
        t2_r3_b1.config(state="normal")
        t2_r3_b2.config(state="normal")
        t2_r3_b3.config(state="normal")
        t3_r4_b1.config(state="normal")
        t3_r4_b2.config(state="normal")
        t3_r4_b3.config(state="normal")
        t3_r5_b1.config(state="normal")
        t3_r5_b2.config(state="normal")
        t3_r6_b1.config(state="normal")
        t3_r6_b2.config(state="normal")
        t4_r5_b1.config(state="normal")
        t4_r6_b1.config(state="normal")
        t4_r7_b1.config(state="normal")
        t4_r8_b1.config(state="normal")
        t4_r9_b1.config(state="normal")
    else:
    # jEDNA
        t2_r1_b1.config(state="disabled")
        t2_r1_b2.config(state="disabled")
        t2_r1_b3.config(state="disabled")
        t3_r1_b1.config(state="disabled")
        t3_r1_b2.config(state="disabled")
        t3_r1_b3.config(state="disabled")
        t3_r2_b1.config(state="disabled")
        t3_r3_b1.config(state="disabled")
        t3_r3_b2.config(state="disabled")
        t4_r1_b1.config(state="disabled")
        t4_r2_b1.config(state="disabled")
        t4_r3_b1.config(state="disabled")
        t4_r4_b1.config(state="disabled")
    #   DWIE
        t2_r2_b1.config(state="disabled")
        t2_r2_b2.config(state="disabled")
        t2_r2_b3.config(state="disabled")
        t2_r3_b1.config(state="disabled")
        t2_r3_b2.config(state="disabled")
        t2_r3_b3.config(state="disabled")
        t3_r4_b1.config(state="disabled")
        t3_r4_b2.config(state="disabled")
        t3_r4_b3.config(state="disabled")
        t3_r5_b1.config(state="disabled")
        t3_r5_b2.config(state="disabled")
        t3_r6_b1.config(state="disabled")
        t3_r6_b2.config(state="disabled")
        t4_r5_b1.config(state="disabled")
        t4_r6_b1.config(state="disabled")
        t4_r7_b1.config(state="disabled")
        t4_r8_b1.config(state="disabled")
        t4_r9_b1.config(state="disabled")
"""


# Zapisz do pliku


class KlasaPodglad(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)
        if len(Naglowki[:, 0]) > 20:
            for x1 in range(len(Naglowki[0])):
                for y1 in range(20):
                    self.pomoc = tkinter.StringVar(self)
                    self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
                    a = Naglowki[y1, x1]
                    self.pomoc.set(a)
                    self.pokaz.grid(row=y1, column=x1)
        else:

            for x1 in range(len(Naglowki[0])):
                for y1 in range(len(Naglowki[:, 0])):
                    self.pomoc = tkinter.StringVar(self)
                    self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
                    a = Naglowki[y1, x1]
                    self.pomoc.set(a)
                    self.pokaz.grid(row=y1, column=x1)


def podglad_kolumn():
    klasa_wyniki = KlasaPodglad()
    klasa_wyniki.mainloop()


class ShowEverything(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)
        if len(lista[:, 0]) > 20:
            for x1 in range(len(lista[0])):
                for y1 in range(20):
                    self.pomoc = tkinter.StringVar(self)
                    self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
                    a = lista[y1, x1]
                    self.pomoc.set(a)
                    self.pokaz.grid(row=y1, column=x1)
        else:

            for x1 in range(len(lista[0])):
                for y1 in range(len(lista[:, 0])):
                    self.pomoc = tkinter.StringVar(self)
                    self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
                    a = lista[y1, x1]
                    self.pomoc.set(a)
                    self.pokaz.grid(row=y1, column=x1)


def wyswietlanie_duze():
    wyswietl_wszystko = ShowEverything()
    wyswietl_wszystko.mainloop()

# INNEEEEEEEEEEEEEEEEEE


def zapis_pliku():
    DoDruku = pd.DataFrame(data=Nowa_lista)

    files = [('csv', '*.csv')]
    file_name = asksaveasfilename(filetypes=files, defaultextension=files)

    if file_name:
        DoDruku.to_csv(file_name, sep=';', encoding='utf-8-sig')



def notatnik():
    okno = Tk()
    okno.title("Notatki")
    okno.geometry('350x810')
    notatki = scrolledtext.ScrolledText(okno, width=40, height=50)
    notatki.grid(column=0, row=0)
    okno.mainloop()


def donothing():
    x = 0
    print(Nowa_lista)


"""
------------- ZAKLADKI FUNKCJE --------------
"""
# ------------- Funckje TAB 2 --------------

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
        self.DoDruku = []

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
            self.DoDruku.append(self.Wyniki)

            for y1 in range(len(self.funkcje)):
                self.b2 = tkinter.Text(self, width=10, height=1)
                self.b2.insert('end', self.Wyniki[y1])
                self.b2.config(state="disabled")
                self.b2.grid(row=y1 + 2, column=x1 + 2)

        for x in range(len(Nowa_lista[0])):
            self.pomoc = tkinter.StringVar(self)
            self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
            self.a = Naglowki[0, x]
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

        self.DoDruku = np.array(self.DoDruku)
        """
        self.DoDruku = pd.DataFrame(data=self.DoDruku, index=Naglowki[0], columns=self.funkcje)
        """
        self.DoDruku = pd.DataFrame({self.funkcje[0]: self.DoDruku[:, 0],
                                     self.funkcje[1]: self.DoDruku[:, 1],
                                     self.funkcje[2]: self.DoDruku[:, 2],
                                     self.funkcje[3]: self.DoDruku[:, 3],
                                     self.funkcje[4]: self.DoDruku[:, 4],
                                     self.funkcje[5]: self.DoDruku[:, 5],
                                     self.funkcje[6]: self.DoDruku[:, 6],
                                     # self.funkcje[7]: self.DoDruku[:, 7]
                                      },
                                    index=Naglowki[0])


    def zapisz(self):


        files = [('csv', '*.csv')]
        file_name = asksaveasfilename(filetypes=files, defaultextension=files)

        if file_name:
            self.DoDruku.to_csv(file_name, sep=';', encoding='utf-8-sig')


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
        self.DoDruku = []

        for x1 in range(len(Nowa_lista[0])):
            self.Wyniki = []
            self.Wyniki.append(float(np.nanvar(Nowa_lista[:, x1])))
            self.Wyniki.append(np.nanstd(Nowa_lista[:, x1]))
            suma = 0
            for i in range(len(Nowa_lista)):
                suma = suma + mat.fabs(Nowa_lista[i, x1]-np.nanmean(Nowa_lista[:, x1]))
            self.Wyniki.append(suma/len(Nowa_lista[:, x1]))
            self.Wyniki.append((np.nanstd(Nowa_lista[:, x1])/np.nanmean(Nowa_lista[:, x1]))*100)
            self.Wyniki.append(np.ptp(Nowa_lista[:, x1]))
            self.Wyniki.append(stats.iqr(Nowa_lista[:, x1]))
            self.Wyniki.append(stats.iqr(Nowa_lista[:, x1]))
            self.Wyniki.append(((stats.iqr(Nowa_lista[:, x1])/2)/np.nanmedian(np.sort(Nowa_lista[:, x1])))*100)
            self.DoDruku.append(self.Wyniki)

            for y1 in range(len(self.funkcje)):
                self.b2 = tkinter.Text(self, width=10, height=1)
                self.b2.insert('end', self.Wyniki[y1])
                self.b2.config(state="disabled")
                self.b2.grid(row=y1 + 2, column=x1 + 2)

        for x in range(len(Nowa_lista[0])):
            self.pomoc = tkinter.StringVar(self)
            self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
            self.a = Naglowki[0, x]
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

        self.DoDruku = np.array(self.DoDruku)
        self.DoDruku = pd.DataFrame({self.funkcje[0]: self.DoDruku[:, 0],
                                     self.funkcje[1]: self.DoDruku[:, 1],
                                     self.funkcje[2]: self.DoDruku[:, 2],
                                     self.funkcje[3]: self.DoDruku[:, 3],
                                     self.funkcje[4]: self.DoDruku[:, 4],
                                     self.funkcje[5]: self.DoDruku[:, 5],
                                     self.funkcje[6]: self.DoDruku[:, 6],
                                     self.funkcje[7]: self.DoDruku[:, 7]
                                     },
                                    index=Naglowki[0])

    def zapisz(self):
        files = [('csv', '*.csv')]
        file_name = asksaveasfilename(filetypes=files, defaultextension=files)

        if file_name:
            self.DoDruku.to_csv(file_name, sep=';', encoding="utf-8-sig")


def miary_zmiennosci():
    klasa_wyniki = MiaryZmi()
    klasa_wyniki.mainloop()


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
        self.DoDruku = []

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

            self.DoDruku.append(self.Wyniki)

            for y1 in range(len(self.funkcje)):
                self.b2 = tkinter.Text(self, width=10, height=1)
                self.b2.insert('end', self.Wyniki[y1])
                self.b2.config(state="disabled")
                self.b2.grid(row=y1 + 2, column=x1 + 2)

        for x in range(len(Nowa_lista[0])):
            self.pomoc = tkinter.StringVar(self)
            self.pokaz = tkinter.Label(self, textvariable=self.pomoc)
            self.a = Naglowki[0, x]
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

        self.DoDruku = np.array(self.DoDruku)
        self.DoDruku = pd.DataFrame({self.funkcje[0]: self.DoDruku[:, 0],
                                     self.funkcje[1]: self.DoDruku[:, 1],
                                     self.funkcje[2]: self.DoDruku[:, 2],
                                     self.funkcje[3]: self.DoDruku[:, 3],
                                     self.funkcje[4]: self.DoDruku[:, 4],
                                     self.funkcje[5]: self.DoDruku[:, 5]
                                     },
                                    index=Naglowki[0])

    def zapisz(self):
        files = [('csv', '*.csv')]
        file_name = asksaveasfilename(filetypes=files, defaultextension=files)

        if file_name:
            self.DoDruku.to_csv(file_name, sep=';', encoding="utf-8-sig")


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


"""

statystyka.resizable(width='false', height='false')

statystyka.maxsize(width=600, height=600)
statystyka.minsize(width=600, height=600)
"""

"""
------------- MENUE --------------
"""
#       PLIK

menubar = Menu(statystyka)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nowy", command=donothing)
filemenu.add_command(label="Otwórz", command=wczytaj_plik)
filemenu.add_command(label="Zapisz", state=NORMAL, command=donothing)
filemenu.add_separator()
filemenu.add_command(label="WYjście", command=statystyka.quit)
menubar.add_cascade(label="Plik", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)


#       POMOC

helpmenu.add_command(label="Znajdź pomoc", command=donothing)
helpmenu.add_command(label="O nas", command=donothing)
menubar.add_cascade(label="Pomoc", menu=helpmenu)
editmenu = Menu(menubar, tearoff=0)

#       EDYCJA

editmenu.add_command(label="Notatnik", command=notatnik)
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Past", command=donothing)
editmenu.add_command(label="Duplicate Line", command=donothing)
editmenu.add_command(label="Toggle Case", command=donothing)
menubar.add_cascade(label="Edycja", menu=editmenu)
statystyka.config(menu=menubar)

"""
------------- ZAKLADKI --------------
"""
#       Tworzenie

zakladki = ttk.Notebook(statystyka)
tab1 = ttk.Frame(zakladki)
tab2 = ttk.Frame(zakladki)
tab3 = ttk.Frame(zakladki)
tab4 = ttk.Frame(zakladki)
tab5 = ttk.Frame(zakladki)
tab6 = ttk.Frame(zakladki)
tab7 = ttk.Frame(zakladki)
zakladki.add(tab1, text='Kolumny')
zakladki.add(tab2, text='Podstawowe badanai', state=NORMAL)
zakladki.add(tab3, text='Testy parametryczne', state=NORMAL)
zakladki.add(tab4, text='Testy nieparametryczne', state=NORMAL)
zakladki.add(tab5, text='5', state=NORMAL)
zakladki.add(tab6, text='6', state=NORMAL)
zakladki.add(tab7, text='7', state=NORMAL)

#       Zakładka 1

wyswiet_2 = Label(tab1, text='Ścieżka wczytanego pliku:')
wyswiet_l = Label(tab1, text='')

ttk.Separator(tab1).grid(row=2, columnspan=15, pady=7, sticky="ew")

ram1 = LabelFrame(tab1, text="Wybieranie kolumn")

tab1_Wybor = Button(ram1, text='Wybierz kolumny', state=DISABLED, command=klasa_definicja)
Aktywoj = Button(ram1, text='Zatwierdz', state=DISABLED, command=aktywacja)

tab1_Wyswietls = Button(tab1, text='Podgląd  kolumn', state=DISABLED, command=podglad_kolumn)
tab1_Zobacz = Button(tab1, text='Podgląd dokumentu', state=DISABLED, command=wyswietlanie_duze)

#       packi

wyswiet_l.grid(column=0, row=1, columnspan=10, stick='W', padx=5, pady=2)
wyswiet_2.grid(column=0, row=0, columnspan=10, stick='W', padx=5, pady=2)

ram1.grid(column=0, row=3, padx=5, pady=5, ipadx=10, ipady=5)

tab1_Wybor.grid(column=0, row=1, sticky="W", padx=5, pady=2)
Aktywoj.grid(column=0, row=2, sticky="W", padx=5, pady=2)
tab1_Wyswietls.grid(column=0, row=4, sticky="W", padx=5, pady=2)
tab1_Zobacz .grid(column=2, row=3, sticky="W", padx=5, pady=2)

#       Zakładka 2

ttk.Separator(tab2).grid(row=0, columnspan=15, pady=7, sticky="ew")

ram2_jedna = LabelFrame(tab2, text='Wymaga jednej kolumny!!!')
# JEDNA
ram2_1 = LabelFrame(ram2_jedna, text='Statystyki opisowe')
t2_r1_b1 = Button(ram2_1, text='Miary położenia', state=NORMAL, command=miary_polozenia)
t2_r1_b2 = Button(ram2_1, text='Miary zmienności', state=NORMAL, command=miary_zmiennosci)
t2_r1_b3 = Button(ram2_1, text='Miary asymetriii koncentracji', state=NORMAL, command=miary_asymetrii)
# DWIE
ram2_dwa = LabelFrame(tab2, text='Wymaga dwóch kolumn!!!')

ram2_2 = LabelFrame(ram2_dwa, text="Zależności serii danych")
t2_r2_b1 = Button(ram2_2, text='Korelacja liniwa Pearsona', state=DISABLED, command=kor_per)
t2_r2_b2 = Button(ram2_2, text='Kowariancja', state=DISABLED, command=kow)
t2_r2_b3 = Button(ram2_2, text='Korelacja liniwa Spermana', state=DISABLED, command=kor_sper)

ram2_3 = LabelFrame(ram2_dwa, text="Wykresy")
t2_r3_b1 = Button(ram2_3, text='Prosta regresji', state=DISABLED, command=reg_lin)
t2_r3_b2 = Button(ram2_3, text='Regresja wykładnicza', state=DISABLED, command=reg_wyk)
t2_r3_b3 = Button(ram2_3, text='Regresja Kwadratowa', state=DISABLED, command=reg_kwadt)

# tab2_n = tkinter.Text(tab2, width=70,  state=DISABLED)

# packi
ram2_jedna.grid(column=0, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)
ram2_dwa.grid(column=1, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)

ram2_1.grid(column=0, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t2_r1_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)
t2_r1_b2.grid(column=0, row=1, padx=5, pady=2, sticky=W)
t2_r1_b3.grid(column=0, row=2, padx=5, pady=2, sticky=W)

ram2_2.grid(column=0, row=2, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t2_r2_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)
t2_r2_b2.grid(column=0, row=1, padx=5, pady=2, sticky=W)
t2_r2_b3.grid(column=0, row=2, padx=5, pady=2, sticky=W)

ram2_3.grid(column=0, row=3, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t2_r3_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)
t2_r3_b2.grid(column=0, row=1, padx=5, pady=2, sticky=W)
t2_r3_b3.grid(column=0, row=2, padx=5, pady=2, sticky=W)

# tab2_n.grid(column=0, row=3, columnspan=5, rowspan=13, padx=5, pady=5, sticky=SW)

#       Zakładka 3

ttk.Separator(tab3).grid(row=0, columnspan=15, pady=7, sticky="ew")

ram3_jedna = LabelFrame(tab3, text='Wymaga jednej kolumny!!!')

ram3_1 = LabelFrame(ram3_jedna, text='Statystyki opisowe')
t3_r1_b1 = Button(ram3_1, text='Znane ochylenie', state=DISABLED, command=donothing)
t3_r1_b2 = Button(ram3_1, text='Nieznne odcylenie, mała', state=DISABLED, command=donothing)
t3_r1_b3 = Button(ram3_1, text='Nieznne odcylenie, duża', state=DISABLED, command=donothing)

ram3_2 = LabelFrame(ram3_jedna, text="Zależności serii danych")
t3_r2_b1 = Button(ram3_2, text='Duza próba', state=DISABLED, command=donothing)

ram3_3 = LabelFrame(ram3_jedna, text="Wykresy")
t3_r3_b1 = Button(ram3_3, text='Małą próba', state=DISABLED, command=donothing)
t3_r3_b2 = Button(ram3_3, text='Duża próba', state=DISABLED, command=donothing)

ram3_dwa = LabelFrame(tab3, text='Wymaga dwóch kolumn!!!')

ram3_4 = LabelFrame(ram3_dwa, text="Testy dla średniej")
t3_r4_b1 = Button(ram3_4, text='Znane ochyleniq', state=DISABLED, command=donothing)
t3_r4_b2 = Button(ram3_4, text='Nieznne, równe odcylenia', state=DISABLED, command=donothing)
t3_r4_b3 = Button(ram3_4, text='Nieznne odcylenia', state=DISABLED, command=donothing)

ram3_5 = LabelFrame(ram3_dwa, text="Testy dla proporcji")
t3_r5_b1 = Button(ram3_5, text='Próby niezależne', state=DISABLED, command=donothing)
t3_r5_b2 = Button(ram3_5, text='Próby zależne', state=DISABLED, command=donothing)

ram3_6 = LabelFrame(ram3_dwa, text='Testy dla wariancji')
t3_r6_b1 = Button(ram3_6, text='Próby niezależne', state=DISABLED, command=donothing)
t3_r6_b2 = Button(ram3_6, text='Próby zależne', state=DISABLED, command=donothing)

# tab3_n = tkinter.Text(tab3, width=70,  state=DISABLED)

# packi
ram3_jedna.grid(column=0, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)
ram3_dwa.grid(column=1, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)

ram3_1.grid(column=0, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t3_r1_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)
t3_r1_b2.grid(column=0, row=0, padx=5, pady=2, sticky=W)
t3_r1_b3.grid(column=0, row=0, padx=5, pady=2, sticky=W)

ram3_2.grid(column=0, row=2, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t3_r2_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)

ram3_3.grid(column=0, row=3, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t3_r3_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)
t3_r3_b2.grid(column=0, row=1, padx=5, pady=2, sticky=W)

#   2 kolumny
ram3_4.grid(column=0, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t3_r4_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)
t3_r4_b2.grid(column=0, row=2, padx=5, pady=2, sticky=W)
t3_r4_b3.grid(column=0, row=3, padx=5, pady=2, sticky=W)

ram3_5.grid(column=0, row=2, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t3_r5_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)
t3_r5_b2.grid(column=0, row=2, padx=5, pady=2, sticky=W)

ram3_6.grid(column=0, row=3, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t3_r6_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)
t3_r6_b2.grid(column=0, row=1, padx=5, pady=2, sticky=W)

# tab3_n.grid(column=0, row=3, columnspan=5, rowspan=13, padx=5, pady=5, sticky=SW)

#       Zakładka 4

ttk.Separator(tab4).grid(row=0, columnspan=15, pady=7, sticky="ew")

ram4_jedna = LabelFrame(tab4, text='Wymaga jednej kolumny!!!')

ram4_1 = LabelFrame(ram4_jedna, text='Test zgodności chi-kwadrat')
t4_r1_b1 = Button(ram4_1, text='Wykonaj test', state=DISABLED, command=donothing)

ram4_2 = LabelFrame(ram4_jedna, text="Test zgodności λ Kołmogorowa")
t4_r2_b1 = Button(ram4_2, text='Wykonaj test', state=DISABLED, command=donothing)

ram4_3 = LabelFrame(ram4_jedna, text="Test normalności Shapiro-Wilka")
t4_r3_b1 = Button(ram4_3, text='Wykonaj test', state=DISABLED, command=donothing)

ram4_4 = LabelFrame(ram4_jedna, text="Test serii")
t4_r4_b1 = Button(ram4_4, text='Wykonaj test', state=DISABLED, command=donothing)

ram4_dwa = LabelFrame(tab4, text='Wybierz dwie kolumny!!!')

ram4_5 = LabelFrame(ram4_dwa, text="Test Kołmogorowa-Smirnowa")
t4_r5_b1 = Button(ram4_5, text='Wykonaj test', state=DISABLED, command=donothing)

ram4_6 = LabelFrame(ram4_dwa, text='Test jednorodności chi-kwadrat')
t4_r6_b1 = Button(ram4_6, text='Wykonaj test', state=DISABLED, command=donothing)

ram4_7 = LabelFrame(ram4_dwa, text="Test mediany")
t4_r7_b1 = Button(ram4_7, text='Wykonaj test', state=DISABLED, command=donothing)

ram4_8 = LabelFrame(ram4_dwa, text='Test serii')
t4_r8_b1 = Button(ram4_8, text='Wykonaj test', state=DISABLED, command=donothing)

ram4_9 = LabelFrame(ram4_dwa, text='Test znaków')
t4_r9_b1 = Button(ram4_9, text='Wykonaj test', state=DISABLED, command=donothing)

# packi
ram4_jedna.grid(column=0, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)

ram4_1.grid(column=0, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t4_r1_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)

ram4_2.grid(column=0, row=2, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t4_r2_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)

ram4_3.grid(column=0, row=3, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t4_r3_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)

ram4_4.grid(column=0, row=4, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t4_r4_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)

#   2 kolumny
ram4_dwa.grid(column=2, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)

ram4_5.grid(column=0, row=1, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t4_r5_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)

ram4_6.grid(column=0, row=2, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t4_r6_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)

ram4_7.grid(column=0, row=3, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t4_r7_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)

ram4_8.grid(column=0, row=4, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t4_r8_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)

ram4_9.grid(column=0, row=5, padx=5, pady=2, ipadx=5, ipady=5, sticky=W)
t4_r9_b1.grid(column=0, row=0, padx=5, pady=2, sticky=W)

#       Zakładka 5

# Pack zakłądek

zakladki.pack(expand=1, fill='both', padx=5, pady=5)

"""
------------- Koniec --------------
"""

statystyka.mainloop()

