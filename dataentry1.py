#This program gets two values from a DB into lineEdits.
import sys
import os
import csv
from dataentry import *
from PyQt5 import QtWidgets, QtGui, QtCore

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'eqre1'); 

import sqlite3
con = sqlite3.connect('covar1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertest1)
     self.ui.pushButton_2.clicked.connect(self.insertest2)
     self.ui.pushButton_3.clicked.connect(self.insertest3)
     self.ui.pushButton_4.clicked.connect(self.csvcreate)
 

  def insertest1(self):
    with con:
      cur = con.cursor()
      vol = str(self.ui.lineEdit.text())
      open = str(self.ui.lineEdit_3.text())
      dlow = str(self.ui.lineEdit_4.text())
      dhigh = str(self.ui.lineEdit_5.text())
      close = str(self.ui.lineEdit_6.text())	
      cur.execute('INSERT INTO futures_data VALUES(?,?,?,?,?)',(open,dlow,dhigh,close,vol))
      con.commit()

  def insertest2(self):
    with con:
      cur = con.cursor()
      vol = str(self.ui.lineEdit_2.text())
      open = str(self.ui.lineEdit_9.text())
      dlow = str(self.ui.lineEdit_8.text())
      dhigh = str(self.ui.lineEdit_7.text())
      close = str(self.ui.lineEdit_10.text())	
      cur.execute('INSERT INTO futures_data VALUES(?,?,?,?,?)',(open,dlow,dhigh,close,vol))
      con.commit()

  def insertest3(self):
    with con:
      cur = con.cursor()
      vol = str(self.ui.lineEdit_13.text())
      open = str(self.ui.lineEdit_14.text())
      dlow = str(self.ui.lineEdit_12.text())
      dhigh = str(self.ui.lineEdit_11.text())
      close = str(self.ui.lineEdit_15.text())	
      cur.execute('INSERT INTO futures_data VALUES(?,?,?,?,?)',(open,dlow,dhigh,close,vol))
      con.commit() 

  def csvcreate(self):
    with con:
      cur = con.cursor()
      cur.execute('SELECT * FROM futures_data;')
      rows = cur.fetchall()
      fp = open('data1.csv', 'w')
      myFile = csv.writer(fp)
      myFile.writerows(rows)
      fp.close()
      con.commit()
     
        

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
