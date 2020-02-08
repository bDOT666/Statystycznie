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



with open('C:\Officjum Inkwizytorskie\pliki\pokemon.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    lista = list(reader)
    lista = np.array(lista)

Nowa_lista = lista[:,6:8]
print(Nowa_lista[0])


def rysuj_wykres():

    Nowa_lista1 = Nowa_lista[1:,:].astype(np.float)

    v = Nowa_lista1[:, 0]
    p = Nowa_lista1[:, 1]

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

b1 = Button(top, text='mama', command=rysuj_wykres)
b1.pack()

e_nazwa1 = Entry(top)
e_nazwa1.pack()

e_nazwa2 = Entry(top)
e_nazwa2.pack()



top.mainloop()





def wybierz_kolumny():

    filez = tkinter.filedialog.askdirectory(parent=window, title='Choose a file')

    ent1.insert(20, filez)

    dirs = os.listdir(filez)

    # remove previous IntVars
    intvar_dict.clear()

    # remove previous Checkboxes
    for cb in checkbutton_list:
        cb.destroy()
    checkbutton_list.clear()

    for filename in dirs:
        # create IntVar for filename and keep in dictionary
        intvar_dict[filename] = tkinter.IntVar()

        # create Checkbutton for filename and keep on list
        c = tkinter.Checkbutton(window, text=filename, variable=intvar_dict[filename])
        c.pack()
        checkbutton_list.append(c)


    for kolumna in Nowa_lista[0]:
        # create IntVar for filename and keep in dictionary
        Nowa_lista[kolumna] = tkinter.IntVar()

        # create Checkbutton for filename and keep on list
        c = tkinter.Checkbutton(window, text=kolumna, variable=Nowa_lista[kolumna])
        c.pack()
        checkbutton_list.append(c)












def browse():

    filez = tkinter.filedialog.askdirectory(parent=window, title='Choose a file')

    ent1.insert(20, filez)

    dirs = os.listdir(filez)

    # remove previous IntVars
    intvar_dict.clear()

    # remove previous Checkboxes
    for cb in checkbutton_list:
        cb.destroy()
    checkbutton_list.clear()

    for filename in dirs:
        # create IntVar for filename and keep in dictionary
        intvar_dict[filename] = tkinter.IntVar()

        # create Checkbutton for filename and keep on list
        c = tkinter.Checkbutton(window, text=filename, variable=intvar_dict[filename])
        c.pack()
        checkbutton_list.append(c)

def test():
    for key, value in intvar_dict.items():
        if value.get() > 0:
            print('selected:', key)

# --- main ---

# to keep all IntVars for all filenames
intvar_dict = {}
 # to keep all Checkbuttons for all filenames
checkbutton_list = []

window = tkinter.Tk()

lbl = tkinter.Label(window, text="Path")
lbl.pack()

ent1 = tkinter.Entry(window)
ent1.pack()

btn1 = tkinter.Button(window, text="Select Path", command=browse)
btn1.pack()

btn1 = tkinter.Button(window, text="Test Checkboxes", command=test)
btn1.pack()

window.mainloop()