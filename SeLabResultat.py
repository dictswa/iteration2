
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton
import sys
from loginside import ui_login

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ui_login()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())

