import xlrd
import os
from pydoc import help
import easygui
path = easygui.fileopenbox()
grafik = xlrd.open_workbook(path).sheet_by_index(0)
#path = "/wrzesień"
#grafik = xlrd.open_workbook("/home/mateusz/Pulpit/13Wrzesień.xlsx").sheet_by_index(0)

class Rozkaz:

    def __init__(self):
        self.dzien = 5
        self.sluzby = []
        self.odwod = []

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

    def zapisz(self):
        with open("/home/mateusz/Pulpit/sluzby.txt", "w") as text_file:
            print(path, file=text_file)
            print("Służby z dnia: ", grafik.cell_value(4, self.dzien), file=text_file)
            for i in self.odwod:
                print(i, file=text_file)
            print("\n", file=text_file)
            for dana in self.sluzby:
                print(dana[0], "- ", dana[1], " ", dana[2], file=text_file)
            text_file.close()
            # for i, dana in zip(self.odwod, self.sluzby):
            #     print(i, "\t \t", dana[0], "- ", dana[1], " ", dana[2], file=text_file)
            # print("*"*80, file=text_file)

    def otworz(self):
        os.system('xdg-open /home/mateusz/Pulpit/sluzby.txt')
test = Rozkaz()

test.podaj_dzien()

test.odwody()

test.slozby()

test.zapisz()

test.otworz()

print("Process finished successful")
