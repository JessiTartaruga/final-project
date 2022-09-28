# import all essential modules and libraries
import csv
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.offline as py
import tkinter.ttk as ttk
# from tkinter import filedialog, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg    # backend, um matplotlib in tkinter auszuführen
from matplotlib.figure import Figure

fw = pd.read_csv('world_population.csv')    # lesen der Datei mit pandas
fw.columns = fw.columns.str.replace(' Population', '') # Verändern der Spaltennamen, ohne Population

def data_overview():
    '''Einblck in den Datensatz, um einen Überblick zu erhalten'''
    print(f'Derzeit leben {fw["2022"].sum():,} Menschen auf der Welt.')  # addiert Werte der Spalte 2022 Population
#############################
# Hinzufügen: Liste der Länder, Spaltenüberschriften, Anzahl der Länder
############################

def group_by_countries():
    '''Gruppiert die Daten nach Ländern'''
    fw_country = fw.groupby(by='Country').sum().reset_index()   # Gruppieren nach der Spalte 'Country', neuer Index
    print(fw_country)    # Kontrolle, gibt Tabelle strukturiert nach Ländern
    print(fw_country[10:50])    # Gibt Zeilen 10-49 heraus nach Ländern strukturiert, Index auslesen
    print(fw_country[100:200])    # S.o. für Zeile 100-199

years = []    # leere Liste für spätere x-Achse
total_pops = []    # leere Liste für spätere y-Achse
col_list = fw.columns    # Zuweisen der Spalten aus der Datei zu col_list

for col in range(12,4,-1):    # Spalten 5-12 durchgehen: Population Data per year; reverse Reihenfolge
    sum = fw[col_list[col]].sum()    # Summe der einzelnen Spalten errechnen (ergibt world population)
    years.append(col_list[col])    # Liste years befüllen mit Spaltentiteln
    total_pops.append(sum)    # Liste total_pops befüllen mit Summen also Weltpopulation
years = pd.to_datetime(years)    # Ändert Spaltenüberschriften von string zu in datetimeobjekten

def tk_pop_year():
    '''Plottet Entwicklung der Weltbevökerung nach Jahren, mit matplotlib über tkinter'''
    fig = Figure(figsize=(9,6), facecolor="white")    # aus matplotlib.figure - Figure
    fig.suptitle("Die Weltpopulation von 1970-2022")    # Titel der Figure
    axis = fig.add_subplot(111)

    axis.plot(years, total_pops)    # plot-Befehl: "years" und "total_pops" s.o.
    axis.set_xlabel('Jahr')    # Titel oder Label der x-Achse
    axis.grid()    # Aktiviert Gitternetz von Matplotlib

    root = tk.Tk()    # Startet das root-Fenster, ist Basis für alles Weitere in tkinter
    root.title("Die Weltpopulation")    # Titel root-Fenster
    canvas = FigureCanvasTkAgg(fig, master=root)    # öfnet tk-drawingarea für matplotlib plot, Basis: root-Fenster
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)    # tkinter pack-Geometriemanager
    button = tk.Button(master=root, text="Quit", command=quit)    # tkinter Widget: Button, im root-Fenster
    button.pack()    # tkinter pack-Geometriemanager
    root.mainloop()

def plot_pop_year():
    '''Plottet Entwicklung der Weltbevökerung nach Jahren, mit matplotlib'''
    plt.plot(years, total_pops, 'o-g')    # Plot x=years, y=total_pops, als Punkte markiert, in Grün
    plt.title("Die Weltpopulation 1970 bis 2022", fontsize=16)    # Definiert den Titel der Figure
    plt.xlabel("Jahr", fontsize=11)    # Definiert Benennung der x-Achse
    plt.ylabel("Weltpopulation", fontsize=11)    # Definiert Benennung der y-Achse
    plt.grid()    # Gitternetz im Hintergrund der Figure
    plt.tight_layout()    # Verändert Layout, Figure erhält mehr Platz
    plt.show()    # Gibt die Figure aus

def tk_pop_countries():
    '''Plottet Entwicklung der Bevölkerung in Algerien, Brasilien, Spanien,
    Zimbabwe nach Jahren, matplotlib und tkinter'''
    fig, axes = plt.subplots(figsize=(9, 6), facecolor="white")  # Größe und Farbe definieren
    axes.grid(visible=True)  # Boolsche Ausdrucksweise, zeigt Grid an

    algeria = fw.iloc[[2], [12, 11, 10, 9, 8, 7, 6, 5]]  # Gibt Dataframe aus für Zeile 2, Spalten 12-5, Algerien
    algeria = algeria.iloc[0]  # Listen-Inhalt der Zeile 0 aus, "algeria" hat nur Zeile 0
    algeria.index = pd.to_datetime(algeria.index)  # Ändert Spaltenüberschriften in datetimeobj. um

    brazil = fw.iloc[[27], [12, 11, 10, 9, 8, 7, 6, 5]]  # Dataframe für Zeile 27 (Brazil), Spalten 12-5 (1970-2022)
    brazil = brazil.iloc[0]  # Listen-Inhalt der Zeile 0 aus, "brazil" hat nur Zeile 0
    brazil.index = pd.to_datetime(algeria.index)  # Ändert Spaltenüberschriften (1970.2022) in datetimeobj. um

    spain = fw.iloc[[196], [12, 11, 10, 9, 8, 7, 6, 5]]    # Zeile 196 (Spain)
    spain = spain.iloc[0]
    spain.index = pd.to_datetime(spain.index)

    zimbabwe = fw.iloc[[233], [12, 11, 10, 9, 8, 7, 6, 5]]    # Zeile 233 (Zimbabwe)
    zimbabwe = zimbabwe.iloc[0]
    zimbabwe.index = pd.to_datetime(zimbabwe.index)

    root = tk.Tk()  # root-Fenster, essentiell
    root.title("Weltpopulation")  # Titel des root-Fensters

    f1 = tk.Frame(root)    # Startet Frame im root-Fenster
    f1.grid(row=0, column=0, sticky="nw")    # grid Geometriemanager
    f2 = tk.Frame(root)    # Startet Frame im root-Fenster
    f2.grid(row=0, column=1)    # grid Geometriemanager

    c1 = FigureCanvasTkAgg(fig, master=f2)  # matplotlib Zeichenfläche, wird in Frame f2 angezeigt
    c1.get_tk_widget().grid(row=0, column=0)  # grid Geometriemanager

    def plot1():
        axes.set_xlabel("Jahre")    # Titel der x-Achse
        axes.plot(algeria, 'o-r', label="Algerien")  # plot-Befehl, Label, verbundene Punkte in Rot
        axes.legend()  # Zeigt Label an
        axes.grid(visible=True)  # Boolsche Ausdrucksweise, dass grid angezeigt wird
        c1.draw()  # Plot anzeigen, wie plt.show()

    def plot2():
        axes.plot(brazil, "o-g", label="Brasilien")    # s.o., verbundenen Punkte in Grün
        axes.legend()
        c1.draw()

    def plot3():
        axes.plot(spain, "x-m", label="Spanien")    # verbundene x in Magenta
        axes.legend()
        c1.draw()

    def plot4():
        axes.plot(zimbabwe, "x-b", label="Zimbabwe")    # s.o., verbundene x in Blau
        axes.legend()
        c1.draw()

    def clear():
        axes.cla()  # löscht Plot(s), cla() = clear axes
        axes.grid(visible=True)
        c1.draw()

    b1 = tk.Button(f1, text="Algerien", command=plot1)  # Plot 1, im Frame f1, Text auf Button, führt "def plot1()" aus
    b1.grid(row=0, column=0, sticky="nsew")  # grid Geometriemanager, lokalisiert und dehnt Button
    b2 = tk.Button(f1, text="Brasilien", command=plot2)
    b2.grid(row=1, column=0, sticky="nsew")
    b3 = tk.Button(f1, text="Spanien", command=plot3)
    b3.grid(row=2, column=0, sticky="nsew")
    b4 = tk.Button(f1, text="Zimbabwe", command=plot4)
    b4.grid(row=3, column=0, sticky="nsew")
    b5 = tk.Button(f1, text="Clear", command=clear) # Clear: löscht gezeichnete Plots
    b5.grid(row=4, column=0, sticky="nsew")
    b6 = tk.Button(f1, text="Quit", command=root.quit)  # Button zum Schließen des gesamten Fensters (root)
    b6.grid(row=5, column=0, sticky="nsew")  # grid Geometriemanager, Buttons unter einander in einer Spalte

    root.mainloop()

def plot_pop_algeria():
    '''Plottet Entwicklung der Population von Algerien nach Jahren, mit matplotlib'''
    algeria = fw.iloc[[2], [12, 11, 10, 9, 8, 7, 6, 5]]    # Gibt Dataframe aus für Zeile 2, Spalten 12-5, Algerien
    algeria = algeria.iloc[0]    # Listen-Inhalt der Zeile 0 aus, "algeria" hat nur Zeile 0
    algeria.index = pd.to_datetime(algeria.index)    # Ändert Spaltenüberschriften in datetimeobj. um
    # print(algeria.index)    # Optional: zur Kontrolle

    plt.plot(algeria, "o-m")    # x-Achse: Jahreszahlen, y-Achse: Population in Algerien, Punkte und Linie in "magenta"
    plt.title("Population von Algerien 1970 bis 2022", fontsize=16)  # Definiert den Titel der Figure
    plt.xlabel("Jahr", fontsize=11)  # Definiert Benennung der x-Achse
    plt.ylabel("Population", fontsize=11)  # Definiert Benennung der y-Achse
    plt.grid()  # Gitternetz im Hintergrund der Figure
    plt.tight_layout()  # Verändert Layout, Figure erhält mehr Platz
    plt.show()

def plot_pop_brazil():
    '''Plottet Entwicklung der Population von Brasilien nach Jahren, mit matplotlib'''
    brazil = fw.iloc[[27], [12, 11, 10, 9, 8, 7, 6, 5]]    # Dataframe für Zeile 27 (Brazil), Spalten 12-5 (1970-2022)
    brazil = brazil.iloc[0]    # Listen-Inhalt der Zeile 0 aus, "brazil" hat nur Zeile 0
    brazil.index = pd.to_datetime(algeria.index)    # Ändert Spaltenüberschriften (1970.2022) in datetimeobj. um
    # print(brazil.index)    # Optional: zur Kontrolle

    plt.plot(brazil, "o-y")    # x-Achse: Jahreszahlen, y-Achse: Population in Brasilien, Punkte und Linie in "yellow"
    plt.title("Population von Brasilien 1970 bis 2022", fontsize=16)  # Definiert den Titel der Figure
    plt.xlabel("Jahr", fontsize=11)  # Definiert Benennung der x-Achse
    plt.ylabel("Population", fontsize=11)  # Definiert Benennung der y-Achse
    plt.grid()  # Gitternetz im Hintergrund der Figure
    plt.tight_layout()  # Verändert Layout, Figure erhält mehr Platz
    plt.show()

def plot_pop_spain():
    '''Plottet Entwicklung der Population von Spanien nach Jahren, mit matplotlib'''
    spain = fw.iloc[[196], [12, 11, 10, 9, 8, 7, 6, 5]]
    spain = spain.iloc[0]
    spain.index = pd.to_datetime(spain.index)
    # print(spain.index)

    plt.plot(spain, "o-r")    # x-Achse: Jahreszahlen, y-Achse: Population in Spanien, Punkte und Linie in "red"
    plt.title("Population von Spanien 1970 bis 2022", fontsize=16)  # Definiert den Titel der Figure
    plt.xlabel("Jahr", fontsize=11)  # Definiert Benennung der x-Achse
    plt.ylabel("Population", fontsize=11)  # Definiert Benennung der y-Achse
    plt.grid()  # Gitternetz im Hintergrund der Figure
    plt.tight_layout()  # Verändert Layout, Figure erhält mehr Platz
    plt.show()

def plot_pop_zimbabwe():
    '''Plottet Entwicklung der Population von Zimbabwe nach Jahren, mit matplotlib'''
    zimbabwe = fw.iloc[[233], [12, 11, 10, 9, 8, 7, 6, 5]]
    zimbabwe = zimbabwe.iloc[0]
    zimbabwe.index = pd.to_datetime(zimbabwe.index)
    # print(zimbabwe.index)

    plt.plot(zimbabwe, "o-b")    # x-Achse: Jahreszahlen, y-Achse: Population in Zimbabwe, Punkte und Linie in "red"
    plt.title("Population von Zimbabwe 1970 bis 2022", fontsize=16)  # Definiert den Titel der Figure
    plt.xlabel("Jahr", fontsize=11)  # Definiert Benennung der x-Achse
    plt.ylabel("Population", fontsize=11)  # Definiert Benennung der y-Achse
    plt.grid()  # Gitternetz im Hintergrund der Figure
    plt.tight_layout()  # Verändert Layout, Figure erhält mehr Platz
    plt.show()

def plot_continents22():
    '''Pie-Chart: Daten für Weltbevölkerung 2022 gruppiert nach Kontinenten, mit plotly.express'''
    population2022 = fw.groupby(by='Continent')['2022'].sum()    # Gruppiert Daten nach Kontinenten für Spalte '2022'
    fig = px.pie(values=population2022.values,    # Erzeugt Figure mit plotly.express, Werte kommen aus Kontinent-Daten
              names=population2022.index,    # Labels kommen aus Spaltenüberschriften der Daten
              # color_discrete_sequence=px.colors.sequential.RdBu,
              title= 'Weltbevölkerung nach Kontinenten in 2022'    # Titel der Figure
              )
    fig.update_traces(textinfo='label+percent+value', textfont_size=13) # Gibt neben Label(Continent) auch Percent&Value
    fig.show()

def plot_worldpopulation22():
    '''Plottet Population auf Weltkarte nach Einwohnern, mit plotly.express'''
    fig1 = px.choropleth(fw,                             # Erstellt eine Choropleth Map (besteht aus bunten Polygonen)
                         locations='Country',            # locations nimmt Werte aus Spalte 'Country'
                         locationmode='country names',   # ???
                         color='2022',                   # Farbe unterscheidet sich nach Zahlen in Spalte '2022'
                         color_continuous_scale=px.colors.sequential.Peach,    # Farbscale
                         # template='plotly_dark',
                         title = 'Weltbevökerung im Jahr 2022')    # Titel der Figure
    fig1.update_layout(font=dict(size=17, family="Franklin Gothic"))    # Anpassen des Layouts
    fig1.show()    # Anzeigen der Figure

    
# data_overview()
# tk_pop_year()
# plot_pop_year()
# plot_pop_algeria()
# plot_pop_spain()
# plot_pop_brazil()
# plot_pop_zimbabwe()
# plot_worldpopulation22()
# plot_continents22()
# tk_pop_countries()
