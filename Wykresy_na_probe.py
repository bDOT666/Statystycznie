import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

from Kontrola_Danych import *

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






class Wybieranie_Kolumn(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)

        # ustawienie

        ram1 = LabelFrame(self, text='Podpisy')

        l1 = tkinter.Label(ram1, text="Nazwa Wykresu")
        e1 = tkinter.Entry(ram1, text='Nazwa Wykresu')
        l2 = tkinter.Label(ram1, text="Os X")
        e2 = tkinter.Entry(ram1, text='X')
        l3 = tkinter.Label(ram1, text="Os Y")
        e3 = tkinter.Entry(ram1, text='Y')

        ram2 = LabelFrame(self, text='Kolumny')

        # Pack zakłądek

        ram1.grid(column=1, row=1, columnspan=2, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)

        l1.grid(column=1, row=1, padx=5, pady=2, sticky=W)
        e1.grid(column=2, row=1, padx=5, pady=2, sticky=W)
        l2.grid(column=3, row=1, padx=5, pady=2, sticky=W)
        e2.grid(column=4, row=1, padx=5, pady=2, sticky=W)
        l3.grid(column=3, row=2, padx=5, pady=2, sticky=W)
        e3.grid(column=4, row=2, padx=5, pady=2, sticky=W)

        ram2.grid(column=1, row=3, rowspan=15, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)

    def kolumny_do_wykresow(self, ram2):

        slownik.clear()

        for cb in lista_boxow:
            cb.destroy()
        lista_boxow.clear()

        for kolumna in Naglowki:
            slownik[kolumna] = tkinter.IntVar()
            c = tkinter.Checkbutton(ram2, text=kolumna, variable=slownik[kolumna])
            c.pack()
            lista_boxow.append(c)

    def wyjmij_kolumny_wykresy(self):

        self.do_wykresu = []
        self.zmienne = []

        for key, value in slownik.items():
            if value.get() > 0:
                i = Naglowki.tolist().index(key)
                self.zmienne.append(i)

        for i in self.zmienne:
            self.do_wykresu.append(Nowa_lista[:, i])
        return self.do_wykresu









