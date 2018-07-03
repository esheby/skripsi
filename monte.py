#form pertama: browse.py

import sys

import pandas as pd
import numpy as np
import random
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
        self.ui.prosesButton.clicked.connect(self.prosesButtonClicked)

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

    def prosesButtonClicked(self):
        pasarPilihan = self.ui.comboPasar.currentText()
        bahanPilihan = self.ui.comboBahan.currentText()
        self.df = pd.read_csv(str(fileHandle), index_col=[1])
        self.df2 = self.df.loc[[pasarPilihan],[bahanPilihan]].reset_index().copy()
        self.total = self.df2[bahanPilihan].sum()
        print(self.total)
        self.df2['Prob'] = self.df2[bahanPilihan] / self.total
        self.df2['Prob Kumulatif'] = self.df2['Prob'].cumsum()
        print(self.df2)
        self.df2['Interval Akhir'] = self.df2['Prob Kumulatif']

        self.df3 = self.df2['Interval Akhir']
        self.interval = self.df3.iloc[:].values
        self.interval = (self.interval * 100).round()

        self.angkaRandom = []
        for self.i in range(int(self.ui.comboHari.currentText())):
            self.angkaRandom.append(random.randrange(0,self.df3.count()))
        self.angkaRandom

        self.c = 0
        self.listPrediksi = []
        self.listPenanda = []
        for self.y in range(len(self.angkaRandom)):
            for self.x in range(self.df3.count()):
                if self.x == 0:
                    self.iv = (pd.Interval(left=0, right=(self.interval[self.x]), closed ='both'))
                    self.x+=1
                    if (self.angkaRandom[self.y] in self.iv) == True:
                        self.listPenanda.append(self.x)
                        break
                    continue
                elif (self.interval[self.x]-self.interval[self.x-1]) == 1:
                    self.iv = (pd.Interval(left=(self.interval[self.x]), right=(self.interval[self.x]), closed ='both'))
                    self.x+=1
                    if (self.angkaRandom[self.y] in self.iv) == True:
                        self.listPenanda.append(self.x)
                        break
                    continue
                else:
                    self.iv = (pd.Interval(left=(self.interval[self.x-1]), right=(self.interval[self.x]), closed ='both'))
                    self.x+=1
                    if (self.angkaRandom[self.y] in self.iv) == True:
                        self.listPenanda.append(self.x)
                        break
        
        self.df4 = self.df.loc[[pasarPilihan],[bahanPilihan]].reset_index().copy()
        harga_beras = self.df4.iloc[:,1].values

        for self.penanda in self.listPenanda:
            self.listPrediksi.append(harga_beras[self.penanda])
            
        QMessageBox.information(self, 'Harga', repr(self.listPrediksi))

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MonteCarlo()
    form.show()
    a.exec_()