from PyQt5 import uic, QtWidgets


def verif():
    ch = windows.l1.text()
    windows.l3.setText(ch)


app = QtWidgets.QApplication([])
windows = uic.loadUi("/home/scorpion/python/gui/divisibilite/div.ui")
windows.show()
windows.b2.clicked.connect(verif)
app.exec_()
