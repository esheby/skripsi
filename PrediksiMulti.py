# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiProgram.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MultiUI(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(536, 518)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 108, 441, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelBahan = QtWidgets.QLabel(self.layoutWidget)
        self.labelBahan.setObjectName("labelBahan")
        self.gridLayout.addWidget(self.labelBahan, 0, 1, 1, 1)
        self.comboBahan = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBahan.setEnabled(False)
        self.comboBahan.setObjectName("comboBahan")
        self.gridLayout.addWidget(self.comboBahan, 1, 1, 1, 1)
        self.prosesButton = QtWidgets.QPushButton(self.layoutWidget)
        self.prosesButton.setEnabled(False)
        self.prosesButton.setObjectName("prosesButton")
        self.gridLayout.addWidget(self.prosesButton, 3, 1, 1, 1)
        self.labelHari = QtWidgets.QLabel(self.layoutWidget)
        self.labelHari.setObjectName("labelHari")
        self.gridLayout.addWidget(self.labelHari, 0, 0, 1, 1)
        self.comboHari = QtWidgets.QComboBox(self.layoutWidget)
        self.comboHari.setEnabled(False)
        self.comboHari.setObjectName("comboHari")
        for hari in range(1, 31):
            self.comboHari.addItem(str(hari))
        self.gridLayout.addWidget(self.comboHari, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 30, 441, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.browsePath = QtWidgets.QLineEdit(self.layoutWidget1)
        self.browsePath.setObjectName("browsePath")
        self.gridLayout_3.addWidget(self.browsePath, 0, 0, 1, 1)
        self.browseButton = QtWidgets.QPushButton(self.layoutWidget1)
        icon = QtGui.QIcon.fromTheme("folder")
        self.browseButton.setIcon(icon)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout_3.addWidget(self.browseButton, 0, 1, 1, 1)
        self.importButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.importButton.setObjectName("importButton")
        self.gridLayout_3.addWidget(self.importButton, 1, 0, 1, 2)
        self.tabel = QtWidgets.QTableWidget(Dialog)
        self.tabel.setGeometry(QtCore.QRect(40, 230, 441, 251))
        self.tabel.setObjectName("tabel")
        self.tabel.setColumnCount(0)
        self.tabel.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Prediksi Monte Carlo"))
        self.labelBahan.setText(_translate("Dialog", "Bahan Pokok:"))
        self.prosesButton.setText(_translate("Dialog", "Proses"))
        self.labelHari.setText(_translate("Dialog", "Hari ke-:"))
        self.browseButton.setText(_translate("Dialog", "Browse"))
        self.importButton.setText(_translate("Dialog", "Import CSV"))

