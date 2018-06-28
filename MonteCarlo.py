# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oneProgram.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(575, 436)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 100, 451, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelPasar = QtWidgets.QLabel(self.layoutWidget)
        self.labelPasar.setEnabled(True)
        self.labelPasar.setObjectName("labelPasar")
        self.gridLayout.addWidget(self.labelPasar, 0, 0, 1, 1)
        self.labelBahan = QtWidgets.QLabel(self.layoutWidget)
        self.labelBahan.setObjectName("labelBahan")
        self.gridLayout.addWidget(self.labelBahan, 0, 1, 1, 1)
        self.comboPasar = QtWidgets.QComboBox(self.layoutWidget)
        self.comboPasar.setEnabled(False)
        self.comboPasar.setObjectName("comboPasar")
        self.gridLayout.addWidget(self.comboPasar, 1, 0, 1, 1)
        self.comboBahan = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBahan.setEnabled(False)
        self.comboBahan.setObjectName("comboBahan")
        self.gridLayout.addWidget(self.comboBahan, 1, 1, 1, 1)
        self.labelHari = QtWidgets.QLabel(self.layoutWidget)
        self.labelHari.setObjectName("labelHari")
        self.gridLayout.addWidget(self.labelHari, 2, 0, 1, 1)
        self.comboHari = QtWidgets.QComboBox(self.layoutWidget)
        self.comboHari.setEnabled(False)
        self.comboHari.setObjectName("comboHari")
        self.gridLayout.addWidget(self.comboHari, 3, 0, 1, 1)
        self.prosesButton = QtWidgets.QPushButton(self.layoutWidget)
        self.prosesButton.setEnabled(False)
        for hari in range(1, 31):
            self.comboHari.addItem(str(hari))
        self.prosesButton.setObjectName("prosesButton")
        self.gridLayout.addWidget(self.prosesButton, 3, 1, 1, 1)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 20, 451, 71))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.browsePath = QtWidgets.QLineEdit(self.widget)
        self.browsePath.setObjectName("browsePath")
        self.gridLayout_3.addWidget(self.browsePath, 0, 0, 1, 1)
        self.browseButton = QtWidgets.QPushButton(self.widget)
        icon = QtGui.QIcon.fromTheme("folder")
        self.browseButton.setIcon(icon)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout_3.addWidget(self.browseButton, 0, 1, 1, 1)
        self.importButton = QtWidgets.QPushButton(self.widget)
        self.importButton.setObjectName("importButton")
        self.gridLayout_3.addWidget(self.importButton, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Prediksi Monte Carlo"))
        self.labelPasar.setText(_translate("Dialog", "Pasar:"))
        self.labelBahan.setText(_translate("Dialog", "Bahan Pokok:"))
        self.labelHari.setText(_translate("Dialog", "Hari ke-:"))
        self.prosesButton.setText(_translate("Dialog", "Proses"))
        self.browseButton.setText(_translate("Dialog", "Browse"))
        self.importButton.setText(_translate("Dialog", "Import CSV"))

