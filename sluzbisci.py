import xlrd
import os
from itertools import chain
import re
from pydoc import help
import easygui
#path = easygui.fileopenbox()
path = "/home/mateusz/Pulpit/MARZEC2.xlsx"
grafik = xlrd.open_workbook(path).sheet_by_index(0)

class Rozkaz:

    def __init__(self):
        self.dzien = 21
        self.sluzby = []
        self.odwod = []
        self.wolne = []

    def podaj_dzien(self):
        for col in range(grafik.ncols):
            print("ID:", col, "-", grafik.cell_value(4, col))
        print("Wprowadź id dnia: ")
        self.dzien = int(input())
        print("Służby z dnia: ", grafik.cell_value(4, self.dzien))

    def slozby(self):
        for row in range(111):
            if grafik.cell_value(row, self.dzien) != "" and grafik.cell_value(row, self.dzien) != "O":
                self.sluzby.append([grafik.cell_value(row, self.dzien), grafik.cell_value(row, 2), grafik.cell_value(row, 3)])
        self.sluzby.sort()
        del self.sluzby[0]
        del self.sluzby[0]
        del self.sluzby[0]
        self.sluzby.insert(0, ["Slużby: ","",len(self.sluzby)])
        for x in self.sluzby:
            if x[0] == "D":
                self.sluzby.remove(x)
                self.sluzby.insert(len(self.sluzby)-1, x)

    def odwody(self):
        i = 1
        for row in range(111):
            if grafik.cell_value(row, self.dzien) == "O":
                self.odwod.append("{}. {} {} ".format(i, grafik.cell_value(row, 2), grafik.cell_value(row, 3)))
                i += 1
        self.odwod.insert(0, "Dyżur w odwodzie - " +str(len(self.odwod)))

    def wolnesz(self):
        for row in range(111):
            if grafik.cell_value(row, self.dzien) == "":
                if grafik.cell_value(row, 2):
                    self.wolne.append("0 {} {} ".format(grafik.cell_value(row, 2), grafik.cell_value(row, 3)))
        self.wolne.insert(0, "Przepustki - " +str(len(self.wolne)))

    def zapisz(self):
        with open("/home/mateusz/Pulpit/sluzby.txt", "w") as text_file:
            print(path, file=text_file)
            print("Służby z dnia: ", grafik.cell_value(4, self.dzien), file=text_file)
            for i in self.odwod:
                print(i, file=text_file)
            print("\n", file=text_file)
            for dana in self.sluzby:
                print(dana[0], "- ", dana[1], " ", dana[2], file=text_file)
            print("\n", file=text_file)
            for i in self.wolne:
                print(i, file=text_file)
            text_file.close()
            # for i, dana in zip(self.odwod, self.sluzby):
            #     print(i, "\t \t", dana[0], "- ", dana[1], " ", dana[2], file=text_file)
            # print("*"*80, file=text_file)

    def otworz(self):
        os.system('xdg-open /home/mateusz/Pulpit/sluzby.txt')
#test = Rozkaz()

class Student:
    def __init__(self):
        self.imie = ''
        self.nazwisko = ''
        self.row = 0
        self.odwod = 0
        self.dyzurka = 0
        self.podzial = 0
        self.miasto = 0
        self.biuro = 0

czain = chain(range(5,36), range(43,72), range(80, 110))
students = []
for i in czain:
#    x = Student()
#    x.imie = grafik.cell_value(i, 3)
#    x.nazwisko = grafik.cell_value(i, 2)
#    x.row = i
    students.append(i)
#biuro = r'B\w+'
#b = re.compile(biuro)
#miasto = r'M'
#m = re.compile(miasto)
#podzial = r'[SP][^D]?$'
#p = re.compile(podzial)
#dyz = r'\w?D'
#d = re.compile(dyz)
#for i in students:
for dni in range(4,grafik.ncols):
    for i in students:
        #print(grafik.cell_value(i,dni))
        if grafik.cell_value(i, dni) == "PD":
            print(grafik.cell_value(4, dni))
            print("PD",grafik.cell_value(i, 2),grafik.cell_value(i, 3))
        if grafik.cell_value(i, dni) == "D":
            print("D",grafik.cell_value(i, 2),grafik.cell_value(i, 3))
    #if grafik.cell_value(i.row, dni):
#            if p.match(grafik.cell_value(i.row, dni)):
#                i.podzial+=1
    #if d.match(grafik.cell_value(i.row, dni)):
                #i.dyzurka+=1
        #print(dni, i.nazwisko)
#            elif b.match(grafik.cell_value(i.row, dni)):
#                i.biuro+=1
#            elif m.match(grafik.cell_value(i.row, dni)):
#                i.miasto+=1
#            else:
#                i.odwod+=1
#students.sort(key=lambda x:x.nazwisko)
#with open("/home/mateusz/Pulpit/sluzy.txt", "w") as text_file:
#    for i in students:
#        print(i.imie, i.nazwisko, 'o=', i.odwod, '; d=', i.dyzurka, '; m=', i.miasto, '; p=', i.podzial, file=text_file)
#    text_file.close()
#del grafik
#test.podaj_dzien()

#test.odwody()

#test.slozby()
#test.wolnesz()
#test.zapisz()

#test.otworz()
