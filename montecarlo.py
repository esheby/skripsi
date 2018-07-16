import sys

from Menu import *
from FormPrediksiSatu import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MenuForm(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.ui.button1Pasar.clicked.connect(self.button1PasarClicked)

    def button1PasarClicked(self):
        self.form1 = MenuForm()
        self.form2 = PrediksiSatuPasar()
        self.form2.show()
        self.form1.hide()


if __name__ == "__main__":
    a = QApplication(sys.argv)

    form = MenuForm()
    form.show()

    a.exec_()