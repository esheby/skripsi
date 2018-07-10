#form pertama: browse.py

import sys

import pandas as pd
import numpy as np
import random
import math
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
        
        #df adalah baca csv
        df = pd.read_csv(str(fileHandle),index_col=[1])
        #df2 adalah dataframe dimana yang dipilih adalah [nama pasar] dan [nama barang]
        df2 = df.loc[[pasarPilihan],[bahanPilihan]].reset_index().copy()
        #listHarga adalah dimana data [nama barang] diurutkan dari angka paling kecil ke paling besar
        listHarga = df2[bahanPilihan].values
        
        #Buat variabel tabel interval
        minPrice=listHarga.min()
        maxPrice=listHarga.max()
        jumBaris=len(listHarga)
        selisih = maxPrice - minPrice
        jumBarisInterval = round(math.sqrt(jumBaris))
        selisihInterval = round(selisih/jumBarisInterval)
        selisihInterval


        #a = interval bagian bawah
        #b = interval bagian atas
        a = []
        b = []
        for x in range(int(jumBarisInterval)):
            if x == 0:
                a.append(minPrice)
                b.append(minPrice + selisihInterval)
            elif x == jumBarisInterval-1:
                a.append(b[-1]+1)
                b.append(maxPrice)
            else:
                a.append(b[-1]+1)
                b.append(a[-1] + selisihInterval)
        #diubah menjadi array
        interA = np.array(a)
        interB = np.array(b)
        print(interA)
        print(interB)

        freqList = []
        for x in range(jumBarisInterval):
            counter = 0
            iv = pd.Interval(left=interA[x], right=interB[x], closed='both')
            for prices in listHarga:
                if (prices in iv) == True:
                    counter += 1
            freqList.append(counter)
        
        #dibuat dataframe bernama dfprob
        dfprob = pd.DataFrame({'bawah':interA, 'atas':interB, 'frekuensi':freqList})
        dfprob['prob'] = dfprob['frekuensi']/jumBaris
        dfprob['prob kumulatif'] = dfprob['prob'].cumsum()

        dfprob = dfprob[dfprob.frekuensi != 0]
        hari = 5
        jumRN = 50
        dfRN = pd.DataFrame()

        for x in range(jumRN):
            tesRN = []
            for y in range(hari):
                tesRN.append(random.uniform(0,1))
                y+=1
            dfRN['RN'+str(x)] = tesRN
            x+=1

        probInter = np.round((dfprob['prob kumulatif']).values,3)
        #a = interval bagian bawah
        #b = interval bagian atas
        a = []
        b = []
        for x in range(len(probInter)):
            if x == 0:
                a.append(0)
                b.append(probInter[x])
                x+=1
            else:
                a.append(b[-1]+0.001)
                b.append(probInter[x])
                x+=1

        bawprob = np.array(a)
        atprob = np.array(b)

        rerata = []
        rerata = (((dfprob['atas'] - dfprob['bawah'])/2)+dfprob['bawah']).values

        newdfRN = pd.DataFrame()
        for x in range(jumRN):
            RNavg = []
            for y in dfRN['RN'+str(x)]:
                for z in range(len(probInter)):
                    iv = pd.Interval(left=bawprob[z], right=atprob[z], closed='both')
                    if (round(y) in iv) == True:
                        RNavg.append(rerata[z])
            newdfRN['RN'+str(x)] = RNavg
        newdfRN['mean'] = newdfRN.mean(axis=1)
        prediksi = newdfRN['mean'].values

        QMessageBox.information(self, 'Prediksi', repr(prediksi))

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MonteCarlo()
    form.show()
    a.exec_()