# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 179)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(30, 50, 401, 91))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.button1Pasar = QtWidgets.QPushButton(self.splitter)
        self.button1Pasar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button1Pasar.setObjectName("button1Pasar")
        self.buttonBanyakPasar = QtWidgets.QPushButton(self.splitter)
        self.buttonBanyakPasar.setObjectName("buttonBanyakPasar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Prediksi Monte Carlo"))
        self.button1Pasar.setText(_translate("Dialog", "Prediksi 1 Pasar"))
        self.buttonBanyakPasar.setText(_translate("Dialog", "Prediksi Banyak Pasar"))

