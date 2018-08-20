import pandas as pd
import numpy as np
import random
import math
import datetime
from PrediksiMulti import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class PrediksiMultiPasar(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = MultiUI()
        self.ui.setupUi(self)
        self.ui.browseButton.clicked.connect(self.browseButtonClicked)
        self.ui.importButton.clicked.connect(self.importButtonClicked)
        self.ui.prosesButton.clicked.connect(self.prosesButtonClicked)

    def browseButtonClicked(self):
        import os
        filePath = QFileDialog.getOpenFileName(self, 'Pilih File', os.curdir,'*.csv')
        global fileHandle
        fileHandle = filePath[0]
        fileHandle.replace("\t","\\t")
        self.ui.browsePath.insert(filePath[0])
    
    def importButtonClicked(self):
        print(fileHandle)
        self.changeEnable()
        self.df = pd.read_csv(str(fileHandle))
        bahanList = self.df.columns[2:].tolist()
        self.ui.comboBahan.addItems(bahanList)

    def changeEnable(self):
        self.ui.browseButton.setEnabled(False)
        self.ui.browsePath.setEnabled(False)
        self.ui.importButton.setEnabled(False)
        self.ui.comboBahan.setEnabled(True)
        self.ui.comboHari.setEnabled(True)
        self.ui.prosesButton.setEnabled(True)

    def perhitungan(self, pasars, df, bahanPilihan, hariPilihan, index):
        df2 = df.loc[[pasars[index]],[bahanPilihan]].reset_index().copy()
        listHarga = df2[bahanPilihan].values
        minPrice = listHarga.min()
        maxPrice = listHarga.max()
        jumBaris = len(listHarga)
        selisih = maxPrice - minPrice
        jumBarisInterval = round(math.sqrt(jumBaris))
        selisihInterval = round(selisih/jumBarisInterval)
        selisihInterval

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

        dfprob = pd.DataFrame({'bawah':interA, 'atas':interB, 'frekuensi':freqList})
        dfprob['prob'] = dfprob['frekuensi']/jumBaris
        dfprob['prob kumulatif'] = dfprob['prob'].cumsum()

        dfprob = dfprob[dfprob.frekuensi != 0]
        jumRN = 50
        dfRN = pd.DataFrame()

        for x in range(jumRN):
            tesRN = []
            for y in range(hariPilihan):
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
                    if (round(y,3) in iv) == True:
                        RNavg.append(rerata[z])
            newdfRN['RN'+str(x)] = RNavg
        newdfRN['mean'] = newdfRN.mean(axis=1)
        prediksi = (newdfRN['mean'].values).tolist()

        for i in range(len(prediksi)):
            self.ui.tabel.setItem(i, index, QTableWidgetItem(str(prediksi[i])))
    
    def prosesButtonClicked(self):
        bahanPilihan = self.ui.comboBahan.currentText()
        hariPilihan = int(self.ui.comboHari.currentText())

        df = pd.read_csv(str(fileHandle), index_col=[1])
        pasars = df.index.unique().values.tolist()
        tanggal = df['Tanggal'].unique().tolist()
        tanggal = tanggal[-1]
        tanggal = datetime.datetime.strptime(tanggal, '%Y/%m/%d')

        tanggalan = []
        for i in range(hariPilihan):
            tanggal += datetime.timedelta(days=1)
            tanggalan.append(tanggal.strftime("%Y/%m/%d"))

        #konfigurasi tabel
        self.ui.tabel.setColumnCount(len(pasars))
        self.ui.tabel.setRowCount(hariPilihan)
        self.ui.tabel.setVerticalHeaderLabels(tanggalan)
        self.ui.tabel.setHorizontalHeaderLabels(pasars)

        for index in range(len(pasars)):
            self.perhitungan(pasars, df, bahanPilihan, hariPilihan, index)

        
        
        
        
        
        
        


    