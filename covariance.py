# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covariance.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 888)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 260, 241, 41))
        self.pushButton.setStyleSheet("border-color: rgb(255, 23, 15);\n"
"color: rgb(7, 7, 7);\n"
"background-color: rgb(255, 213, 87);\n"
"selection-background-color: rgb(105, 255, 64);\n"
"font: 9pt \"PMingLiU-ExtB\";\n"
"selection-background-color: rgb(42, 255, 84);\n"
"selection-color: rgb(28, 255, 25);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 330, 241, 41))
        self.pushButton_2.setStyleSheet("border-color: rgb(35, 86, 255);\n"
"background-color: rgb(255, 213, 87);\n"
"font: 9pt \"PMingLiU-ExtB\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 470, 241, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 213, 87);\n"
"font: 9pt \"PMingLiU-ExtB\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 400, 241, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 213, 87);\n"
"font: 9pt \"PMingLiU-ExtB\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 540, 241, 41))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 213, 87);\n"
"font: 9pt \"PMingLiU-ExtB\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, -10, 701, 851))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Users/anant/Desktop/share.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covariance of Futures Data"))
        self.pushButton.setText(_translate("MainWindow", "Store and Export Data From Database"))
        self.pushButton_2.setText(_translate("MainWindow", "Covariance of gold open & high prices"))
        self.pushButton_3.setText(_translate("MainWindow", "Silver Futures Covarinace matrix"))
        self.pushButton_4.setText(_translate("MainWindow", "Covariance of gold & silver futures"))
        self.pushButton_5.setText(_translate("MainWindow", "Heat Map"))
