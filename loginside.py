# Form implementation generated from reading ui file 'loginside-kopi.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton
import sys

brugere={'læge1':'kodeord1','læge2':'kodeord2','læge3':'kodeord3'} #definere liste af eksisterende brugere

#widget
class ui_login(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(260, 150, 351, 211))
        self.groupBox.setStyleSheet("background-color: rgb(150, 221, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(150, 221, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(120, 80, 171, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 110, 171, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(150, 221, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgb(150, 221, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(60, 150, 113, 32))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 150, 113, 32))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Funktionalitet
        self.pushButton_2.released.connect(self.handle_login) #When the button is released the handle_login function will run
    def handle_login(self):
        '''function that handles the login process'''
        brugernavn=self.lineEdit.text() #Defining login variables
        kodeord=self.lineEdit_2.text()

        if brugernavn in brugere.keys() and kodeord==brugere[brugernavn]: #Conditional checking that the user exists and the password corresponds to the user
            from sogefterpatient import ui_sogefterpatient
            import sys
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = ui_sogefterpatient()
            ui.setupUi(MainWindow)
            MainWindow.show()
            app.exec()
        else:
            print('fail')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Kodeord:"))
        self.label.setText(_translate("MainWindow", "Log ind på den elekroniske patient journal"))
        self.label_2.setText(_translate("MainWindow", "Brugernavn:"))
        self.pushButton.setText(_translate("MainWindow", "Opret"))
        self.pushButton.setShortcut(_translate("MainWindow", "Backspace"))
        self.pushButton_2.setText(_translate("MainWindow", "Log ind"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
