#form pertama: browse.py

import sys

import pandas as pd
from MonteCarlo import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MonteCarlo(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.browseButton.clicked.connect(self.browseButtonClicked)
        self.ui.importButton.clicked.connect(self.importButtonClicked)

    def browseButtonClicked(self):
        import os
        filePath = QFileDialog.getOpenFileName(self, 
                                                       'Pilih File',
                                                       os.curdir,
                                                      '*.csv')
        global fileHandle 
        fileHandle = filePath[0]
        fileHandle.replace("\t","\\t")
        self.ui.browsePath.insert(filePath[0])

    def importButtonClicked(self):
        print(fileHandle)
        #with open(fileHandle) as f:
           # content = f.read().splitlines()
           # print(content)
        self.changeEnable()
        self.df = pd.read_csv(str(fileHandle))
        pasarList = self.df.Pasar.unique().tolist()
        bahanList = self.df.columns[2:].tolist()
        self.ui.comboPasar.addItems(pasarList)
        self.ui.comboBahan.addItems(bahanList)

    def changeEnable(self):
        self.ui.browseButton.setEnabled(False)
        self.ui.browsePath.setEnabled(False)
        self.ui.importButton.setEnabled(False)
        self.ui.comboPasar.setEnabled(True)
        self.ui.comboBahan.setEnabled(True)
        self.ui.comboHari.setEnabled(True)
        self.ui.prosesButton.setEnabled(True)
    
if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MonteCarlo()
    form.show()
    a.exec_()