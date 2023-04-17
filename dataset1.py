import sys
import os
import csv
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from dataset import *
from PyQt5 import QtWidgets, QtGui, QtCore

class myclass(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.inserttest)

    def inserttest(self):
        data = pd.read_csv(self.ui.lineEdit.text())

        plt.figure(figsize=(50, 50))
        print(data.corr())

        sns.heatmap(data.corr(),annot=True)
        plt.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = myclass()
    myapp.show()
    sys.exit(app.exec_())
