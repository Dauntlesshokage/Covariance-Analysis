import sys
import csv
import os
from covariance import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('covar1')

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'wilcox1'); 

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.dentry)
     self.ui.pushButton_2.clicked.connect(self.cv1)
     self.ui.pushButton_3.clicked.connect(self.cv2)
     self.ui.pushButton_4.clicked.connect(self.cv3)
     self.ui.pushButton_5.clicked.connect(self.htmap)

  def dentry(self):
    os.system("python dataentry1.py")

  def cv1(self):
    os.system("python covar1.py")

  def cv2(self):
    os.system("python covar3.py")
	
  def cv3(self):
    os.system("python covar4.py")
	
  def htmap(self):
    os.system("python covar5.py")
	
        

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
