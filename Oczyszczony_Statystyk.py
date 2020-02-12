
from tkinter import ttk

from Kontrola_Danych import *


statystyka = tkinter.Tk()


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
filemenu.add_command(label="Otwórz", command=lambda: wczytaj_plik(wyswiet_l, tab1_Wybor, tab1_Zobacz))
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

tab1_Wybor = Button(ram1, text='Wybierz kolumny', state=DISABLED, command=wybierz_kolumny)
Aktywoj = Button(ram1, text='Zatwierdz', state=NORMAL, command=lambda: zatwierdz_kolumny(tab1_Wybor, tab1_Wyswietls))

tab1_Wyswietls = Button(tab1, text='Podgląd  kolumn', state=DISABLED, command=podglad_kolumn)
tab1_Zobacz = Button(tab1, text='Podgląd dokumentu', state=NORMAL, command=podglad_wszystko)

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


ram1 = LabelFrame(tab5, text='Podpisy')

l1 = tkinter.Label(ram1, text="Nazwa Wykresu")
e1 = tkinter.Entry(ram1, text='Nazwa Wykresu')
l2 = tkinter.Label(ram1, text="Os X")
e2 = tkinter.Entry(ram1, text='X')
l3 = tkinter.Label(ram1, text="Os Y")
e3 = tkinter.Entry(ram1, text='Y')
b1 = Button(ram1, text='Wypisz kolumny', command=lambda: kolumny_do_wykresow(ram2))
b2 = Button(ram1, text='Rysuj Wykres', command=lambda: rysuj_wykres(e1, e2, e3))

ram2 = LabelFrame(tab5, text='Kolumny')

ram3 = LabelFrame(tab5, text='Wykresy')


# Pack


ram1.grid(column=1, row=1, columnspan=4, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)

l1.grid(column=1, row=1, padx=5, pady=2, sticky=W)
e1.grid(column=2, row=1, padx=5, pady=2, sticky=W)
l2.grid(column=3, row=1, padx=5, pady=2, sticky=W)
e2.grid(column=4, row=1, padx=5, pady=2, sticky=W)
l3.grid(column=3, row=2, padx=5, pady=2, sticky=W)
e3.grid(column=4, row=2, padx=5, pady=2, sticky=W)
b1.grid(column=1, row=2,  padx=5, pady=2, sticky=W)
b2.grid(column=2, row=2,  padx=5, pady=2, sticky=W)

ram2.grid(column=1, row=3, rowspan=15, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)

ram3.grid(column=3, row=3, rowspan=15, padx=5, pady=2, ipadx=5, ipady=5, sticky=NW)


# Pack zakłądek


zakladki.pack(expand=1, fill='both', padx=5, pady=5)


"""
------------- Koniec --------------
"""

statystyka.mainloop()












