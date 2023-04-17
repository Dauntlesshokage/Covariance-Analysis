# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataset.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 220, 121, 21))
        self.label.setStyleSheet("font: 9pt \"PMingLiU-ExtB\";\n"
"\n"
"color: rgb(144, 144, 144);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 210, 231, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(125, 125, 125);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 330, 93, 28))
        self.pushButton.setStyleSheet("font: 9pt \"PMingLiU-ExtB\";\n"
"selection-background-color: rgb(88, 255, 42);\n"
"font: 10pt \"PMingLiU-ExtB\";")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 0, 781, 481))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Users/anant/Desktop/dataset.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  Enter Dataset File"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
