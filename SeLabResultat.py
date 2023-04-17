
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton
import sys
from loginside import ui_login

app = QtWidgets.QApplication(sys.argv)
MainWindow = ui_login()
MainWindow.show()
sys.exit(app.exec())

