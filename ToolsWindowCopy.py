# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToolsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import mysql.connector
from Baza import Baza
import traceback
import cgitb

cgitb.enable(format='text')

class Ui_TechWindow(object):
    def __init__(self, base):
        self.dtbase = base

    def setupUi(self, TechWindow):
        TechWindow.setObjectName("TechWindow")
        TechWindow.resize(490, 432)
        self.centralwidget = QtWidgets.QWidget(TechWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wybor_Akcji = QtWidgets.QListWidget(self.centralwidget)
        self.wybor_Akcji.setGeometry(QtCore.QRect(20, 70, 121, 61))
        self.wybor_Akcji.setObjectName("wybor_Akcji")
        item = QtWidgets.QListWidgetItem()
        self.wybor_Akcji.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.wybor_Akcji.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.wybor_Akcji.addItem(item)
        self.label_Akcja = QtWidgets.QLabel(self.centralwidget)
        self.label_Akcja.setGeometry(QtCore.QRect(30, 40, 71, 21))
        self.label_Akcja.setObjectName("label_Akcja")
        self.label_Relacja = QtWidgets.QLabel(self.centralwidget)
        self.label_Relacja.setGeometry(QtCore.QRect(180, 40, 51, 21))
        self.label_Relacja.setObjectName("label_Relacja")
        self.label_Dane = QtWidgets.QLabel(self.centralwidget)
        self.label_Dane.setGeometry(QtCore.QRect(30, 170, 47, 13))
        self.label_Dane.setObjectName("label_Dane")
        self.Guzik_Zatwierdzajacy = QtWidgets.QPushButton(self.centralwidget)
        self.Guzik_Zatwierdzajacy.setGeometry(QtCore.QRect(320, 350, 75, 23))
        self.Guzik_Zatwierdzajacy.setObjectName("Guzik_Zatwierdzajacy")
        self.wybor_Relacji = QtWidgets.QListWidget(self.centralwidget)
        self.wybor_Relacji.setGeometry(QtCore.QRect(160, 70, 121, 120))
        self.wybor_Relacji.setObjectName("wybor_Relacji")


        # Ustawianie ilości elementów listy relacji do wyboru
        amount = len(Baza.getTableNamesFromDb('testdb'))
        for i in range(amount):
            item = QtWidgets.QListWidgetItem()
            self.wybor_Relacji.addItem(item)

        self.Tablica_Danych = QtWidgets.QTableWidget(self.centralwidget)
        self.Tablica_Danych.setGeometry(QtCore.QRect(10, 190, 291, 192))
        self.Tablica_Danych.setObjectName("Tablica_Danych")
        self.Tablica_Danych.setColumnCount(2)
        for i in range(2):
            item = QtWidgets.QTableWidgetItem()
            self.Tablica_Danych.setHorizontalHeaderItem(i, item)

        # Ustawienie odpowiednio dużej ilości wierszy w tabeli do wpisywania danych
        self.Tablica_Danych.setRowCount(20)
        for i in range(20):
            item = QtWidgets.QTableWidgetItem()
            self.Tablica_Danych.setVerticalHeaderItem(i, item)


        self.Tablica_Danych.setHorizontalHeaderItem(0, item)
        # self.Tablica_Danych.setHorizontalHeaderItem(1, item)
        TechWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TechWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 21))
        self.menubar.setObjectName("menubar")
        TechWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TechWindow)
        self.statusbar.setObjectName("statusbar")
        TechWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TechWindow)
        QtCore.QMetaObject.connectSlotsByName(TechWindow)

    def retranslateUi(self, TechWindow):
        _translate = QtCore.QCoreApplication.translate
        TechWindow.setWindowTitle(_translate("TechWindow", "MainWindow"))
        __sortingEnabled = self.wybor_Akcji.isSortingEnabled()
        self.wybor_Akcji.setSortingEnabled(False)
        item = self.wybor_Akcji.item(0)
        item.setText(_translate("TechWindow", "Dodaj dane"))
        item = self.wybor_Akcji.item(1)
        item.setText(_translate("TechWindow", "Usuń dane"))
        item = self.wybor_Akcji.item(2)
        item.setText(_translate("TechWindow", "Modyfikuj dane"))
        self.wybor_Akcji.setSortingEnabled(__sortingEnabled)
        self.label_Akcja.setText(_translate("TechWindow", "Acja:"))
        self.label_Relacja.setText(_translate("TechWindow", "Relacja:"))
        self.label_Dane.setText(_translate("TechWindow", "Dane:"))
        self.Guzik_Zatwierdzajacy.setText(_translate("TechWindow", "Zatwierdź"))
        __sortingEnabled = self.wybor_Relacji.isSortingEnabled()
        self.wybor_Relacji.setSortingEnabled(False)


        # Ustawienie listy relacji do wyboru
        tables = Baza.getTableNamesFromDb('testdb')
        it = 0
        print(tables)
        for i in tables:
            print(i)
            item = self.wybor_Relacji.item(it)
            item.setText(_translate("TechWindow", tables[it]))
            it += 1


        self.wybor_Relacji.setSortingEnabled(__sortingEnabled)
        item = self.Tablica_Danych.horizontalHeaderItem(0)
        item.setText(_translate("TechWindow", "Dane"))

        # Tu aktywowane są reakcje na kliknięcia
        self.Guzik_Zatwierdzajacy.clicked.connect(self.getChoice)
        self.wybor_Relacji.clicked.connect(self.UpdateXXX)
        self.wybor_Akcji.clicked.connect(self.UpdateAkcje)

    def UpdateAkcje(self):
        item1 = self.wybor_Akcji.currentItem()
        item1 = item1.text()

        _translate = QtCore.QCoreApplication.translate

        print('przed testem "Modyfikuj dane"')

        if item1 == "Modyfikuj dane":
            item = self.Tablica_Danych.horizontalHeaderItem(0)
            item.setText(_translate("TechWindow", "Stare Dane"))
            item = self.Tablica_Danych.horizontalHeaderItem(1)
            item.setText(_translate("TechWindow", "Nowe Dane"))

        else:
            item = self.Tablica_Danych.horizontalHeaderItem(0)
            item.setText(_translate("TechWindow", "Dane"))
            item = self.Tablica_Danych.horizontalHeaderItem(1)
            item.setText(_translate("TechWindow", ""))


        print('po teście "Modyfikuj dane"')

    # Wypełnianie tabeli do wpisywania danych nazwami kolumn w zależności od wybranej relacji
    def UpdateXXX(self):
        item1 = self.wybor_Relacji.currentItem()
        item1 = item1.text()
        # print(item1)
        self.updateDane(item1)

    def updateDane(self,table):
        columns = Baza.getColumnNamesFromTable(self.dtbase,table)
        numC = len(columns)

        _translate = QtCore.QCoreApplication.translate

        # Wypełnianie tabeli... implementacja
        for i in range(20):
            if (numC - i) > 0:
                item = self.Tablica_Danych.verticalHeaderItem(i)
                item.setText(_translate("TechWindow", columns[i]))
            else:
                item = self.Tablica_Danych.verticalHeaderItem(i)
                item.setText(_translate("TechWindow", ""))
        item1 = self.Tablica_Danych.horizontalHeaderItem(0)
        # item.setText(_translate("TechWindow", "Dane"))
        item1.setText("Nowe Dane")

    #wybór dostępnych opcji
    def getChoice(self):
        try:
            item1 = self.wybor_Akcji.currentItem()
            item1 = item1.text()
            item2 = self.wybor_Relacji.currentItem()
            item2 = item2.text()



            # items - wartości wpiasne prze użytkownika
            items = []
            it = len(Baza.getColumnNamesFromTable(self.dtbase, item2))
            for i in range(it):
                if (self.Tablica_Danych.item(i, 0) is not None):
                    if self.Tablica_Danych.item(i, 0).text() == '':
                        items.append(None)
                    else:
                        items.append(self.Tablica_Danych.item(i, 0).text())
                else:
                    items.append(None)
            print('items  :',items)


            if item1 == "Dodaj dane":
                Baza.insert(self.dtbase, item2, items)
            print('after insert checkpoint')

            if item1 == "Usuń dane":
                Baza.delete(self.dtbase, item2, items)
            print('after delete checkpoint')


        except Exception:
            traceback.print_exc()
            print('cuśik poszedu nie tak')
