
from Kontrola_Danych import *

global lista
global wybrane_kolumny
global Nowa_lista
global Naglowki

"""
------------- Pierwsza Karta --------------
"""


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
    x = 0


class Miary_Asy(tkinter.Tk):
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
    klasa_wyniki = Miary_Asy()
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

