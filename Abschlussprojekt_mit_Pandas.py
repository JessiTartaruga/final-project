# import all essential modules and libraries
import csv
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

fw = pd.read_csv('world_population.csv')    # lesen der Datei mit pandas

# print(f'Derzeit leben {fw["2022 Population"].sum():,} Menschen auf der Welt.')    # addiert Werte der Spalte 2022 Population

fw.columns = fw.columns.str.replace(' Population', '') # Verändern der Spaltennamen, ohne Population
cols = fw.columns    # Zuweisen der Spalten zu der Variable col
years = []    # leere Liste
total_pops = []    # leere Liste
col_list = fw.columns    # Zuweisen der Spalten aus der Datei zu col_list

for col in range(12,4,-1):    # Spalten 5-12 durchgehen: Population Data per year; reverse Reihenfolge
    sum = fw[col_list[col]].sum()    # Summe der einzelnen Spalten errechnen (ergibt world population)
    years.append(col_list[col])    # Liste years befüllen mit Spaltentiteln
    total_pops.append(sum)    # Liste total_pops befüllen mit Summen also Weltpopulation
# print(years)    # Optional: Gibt zur Kontrolle die Liste aus
# print(total_pops)    # Optional: Gibt zur Kontrolle die Liste aus

def plot_pop_year():
    '''Plottet Entwicklung der Weltbevökerung nach Jahren'''
    plt.plot(years, total_pops, 'o-g')    # Plot x=years, y=total_pops, als Punkte markiert, in Grün
    plt.title("Die Weltpopulation 1970 bis 2022", fontsize=16)    # Definiert den Titel der Figure
    plt.xlabel("Jahr", fontsize=11)    # Definiert Benennung der x-Achse
    plt.ylabel("Weltpopulation", fontsize=11)    # Definiert Benennung der y-Achse
    plt.grid()    # Gitternetz im Hintergrund der Figure
    plt.tight_layout()    # Verändert Layout, Figure erhält mehr Platz
    plt.show()    # Gibt die Figure aus

def plot_continents22():
    '''Pie-Chart: Daten für Weltbevölkerung 2022 gruppiert nach Kontinenten'''
    population2022=fw.groupby(by='Continent')['2022'].sum()    # Gruppiert Daten nach Kontinenten für Spalte '2022'
    fig=px.pie(values=population2022.values,    # Erzeugt Figure mit plotly.express, Werte kommen aus Kontinent-Daten
              names=population2022.index,    # Labels kommen aus Spaltenüberschriften der Daten
              # color_discrete_sequence=px.colors.sequential.RdBu,
              title= 'Weltbevölkerung nach Kontinenten in 2022'    # Titel der Figure
              )
    fig.update_traces(textinfo='label+percent+value', textfont_size=13) # Gibt neben Label(Continent) auch Percent&Value
    fig.show()

def plot_worldpopulation22():
    '''Plottet Population auf Weltkarte nach Einwohnern'''
    fig1 = px.choropleth(fw,                             # Erstellt eine Choropleth Map (besteht aus bunten Polygonen)
                         locations='Country',            # locations nimmt Werte aus Spalte 'Country'
                         locationmode='country names',   # ???
                         color='2022',                   # Farbe unterscheidet sich nach Zahlen in Spalte '2022'
                         color_continuous_scale=px.colors.sequential.Peach,    # Farbscale
                         # template='plotly_dark',
                         title = 'Weltbevökerung im Jahr 2022')    # Titel der Figure
    fig1.update_layout(font = dict(size = 17, family="Franklin Gothic"))    # Anpassen des Layouts
    fig1.show()    # Anzeigen der Figure

'''Versuch Bevölkerungsentwicklung je Land'''
# fw.columns = fw.columns.str.repla
# cols = fw.columns    # Zuweisen der Spalten zu der Variable col
# years = []    # leere Liste
# total_pops = []    # leere Liste
# col_list = fw.columns    # Zuweisen der Spalten aus der Datei zu col_list
#
# for col in range(12,4,-1):    # Spalten 5-12 durchgehen: Population Data per year; reverse Reihenfolge
#     sum = fw[col_list[col]].sum()    # Summe der einzelnen Spalten errechnen (ergibt world population)
#     years.append(col_list[col])    # Liste years befüllen mit Spaltentiteln
#     total_pops.append(sum)    # Liste total_pops befüllen mit Summen also Weltpopulation
# # print(years)    # Optional: Gibt zur Kontrolle die Liste aus
# # print(total_pops)    # Optional: Gibt zur Kontrolle die Liste aus

'''Gruppiert die Daten nach Ländern'''
fw_country = fw.groupby(by='Country').sum().reset_index()   # Gruppieren der Dateien nach der Spalte 'Country', neuer Index
# print(fw_country)    # Kontrolle: zeigt neue, gruppierte Tabelle nach Kontinenten an
 # Brazil, DR Congo, France, Turkey

countries = fw_country['Country']    # Übergibt 'Country' aus dem Dataframe an Variable fw_country
print(countries)    # data series element, nd array?
country = countries[0]    # selecting by integer location, row
selected_country = fw_country.loc[fw_country['Country']==country]    # loc = location, in Form eines dictionary-key
print(selected_country)
country1 = selected_country.iloc[:,9:1:-1]
# print(selected_country.iloc[:,9:1:-1])    # Zeilen und Spalten in integer und nicht in value, integer Positionen können angesprochen werden

plt.plot(country1(fw.columns), country1(fw.rows))
plt.show()
# plotten x = columns, y = rows

# x = [1970, 1980, 1990, 2000, 2010, 2015, 2020, 2022]    # Spaltennamen 1970, 1980, 1990, 2000, 2010, 2015, 2020, 2022
# y = []    # Werte aus den jeweiligen Spalten für das ausgewählte Land, range([12, 4, -1])
# for col in fw.columns(range(12, 4, -1)):
#     y.append(selected_country)
#
# print(x)
# print(y)
