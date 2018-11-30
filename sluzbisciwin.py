#uwzględnianie zamian
#średnia służb z miesiąca,
#ze wszystkich plkików, suma poszczególnych
#losowanie ludzi do roboty
#wstawianie plusów (skala 1-3)
from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
#from PyQt5.QtGui import QIcon, QLi
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

import xlrd
grafik = xlrd.open_workbook("/home/mateusz/Pulpit/3Grudzień.xlsx").sheet_by_index(0)

class Sluzby(QWidget):
    def __init__(self, parent=None):
        super(Sluzby, self).__init__(parent)
        self.interfejs()

    def podaj_dzien():
        for col in range(grafik.ncols):
            print("ID:", col, "-", grafik.cell_value(4, col), "\t", end="")
        print("")
        print("Wprowadź id dnia: ")
        global dzien
        dzien = int(input())
        print("Służby z dnia: ", grafik.cell_value(4, dzien))

    def wyswietl_sluzby():
        sluzby = []
        for row in range(111):
            if grafik.cell_value(row, dzien) != "" and grafik.cell_value(row, dzien) != "O":
                sluzby.append([grafik.cell_value(row, dzien), grafik.cell_value(row, 2), grafik.cell_value(row, 3)])
        sluzby.sort()
        del sluzby[0]
        del sluzby[0]
        del sluzby[0]
        for dana in sluzby:
            print(dana[0], "- ", dana[1], " ", dana[2])

    def wyswietl_odwody(self):
        odwod = []
        dzien = 5
        i = 1
        for row in range(111):
            if grafik.cell_value(row, dzien) == "O":
                #odwod.append(str(grafik.cell_value(row, 2), grafik.cell_value(row, 3)])
                odwod.append("{}. {} {} ".format(i, grafik.cell_value(row, 2), grafik.cell_value(row, 3)))
                i+=1
        odwod.insert(0,"Dyżur w odwodzie:")
        col_width = max(len(word) for word in odwod)
        # for row in data:
        #     print "".join(word.ljust(col_width) for word in row)
        #self.etykieta4.setText(v for v in odwod)
        self.etykieta4.setText("\n".join(odwod))
        #self.etykieta4.


    def interfejs(self):
        etykieta1 = QLabel("Wprowadź id dnia: ", self)
        etykieta2 = QLabel("Odwód: ", self)
        etykieta3 = QLabel("Służby: ", self)
        self.etykieta4 = QLabel("", self)

        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 1)
        ukladT.addWidget(etykieta2, 2, 0)
        ukladT.addWidget(etykieta3, 2, 2)
        ukladT.addWidget(self.etykieta4, 3, 0)
        self.setLayout(ukladT)
        self.liczba1Edt = QLineEdit()
        self.wynik1Edt = QLineEdit()
        self.wynik2Edt = QLineEdit()

        ukladT.addWidget(self.liczba1Edt, 1, 1)
        ukladT.addWidget(self.wynik1Edt, 2, 1)
        ukladT.addWidget(self.wynik2Edt, 2, 3)
        wykonajBtn = QPushButton("&Wykonaj", self)
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())
        ukladH = QHBoxLayout()
        ukladH.addWidget(wykonajBtn)
        ukladT.addLayout(ukladH, 4, 0, 1, 4)
        ukladT.addWidget(koniecBtn, 5, 0, 1, 4)
        #self.showFullScreen()
        self.setGeometry(400, 200, 300, 100)
        #self.setWindowIcon(QIcon('/home/mateusz/Pyton/figure_1.jpg'))
        self.setWindowTitle("Służby")
        self.show()
        koniecBtn.clicked.connect(self.koniec)
        wykonajBtn.clicked.connect(self.dzialanie)
    def koniec(self):
       self.close()
    def dzialanie(self):

        nadawca = self.sender()
        dzien = 5
        #dzien = int(self.liczba1Edt.text())
        if nadawca.text() == "&Wykonaj":
            self.wyswietl_odwody()

        #     for col in range(grafik.ncols):
        #         print("ID:", col, "-", grafik.cell_value(4, col), "\t", end="")
        #     print("")
        #     print("Wprowadź id dnia: ")
        #     print("Służby z dnia: ", grafik.cell_value(4, dzien))
        #
        # self.wynik1Edt.setText(str("Służby z dnia: "))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Sluzby()
    sys.exit(app.exec_())