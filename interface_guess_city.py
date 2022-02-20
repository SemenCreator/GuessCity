from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choice_1 = QtWidgets.QPushButton(self.centralwidget)
        self.choice_1.setGeometry(QtCore.QRect(10, 390, 381, 23))
        self.choice_1.setText("")
        self.choice_1.setObjectName("choice_1")
        self.choice_2 = QtWidgets.QPushButton(self.centralwidget)
        self.choice_2.setGeometry(QtCore.QRect(400, 390, 381, 23))
        self.choice_2.setText("")
        self.choice_2.setObjectName("choice_2")
        self.choice_3 = QtWidgets.QPushButton(self.centralwidget)
        self.choice_3.setGeometry(QtCore.QRect(10, 420, 381, 23))
        self.choice_3.setText("")
        self.choice_3.setObjectName("choice_3")
        self.choice_4 = QtWidgets.QPushButton(self.centralwidget)
        self.choice_4.setGeometry(QtCore.QRect(400, 420, 381, 23))
        self.choice_4.setText("")
        self.choice_4.setObjectName("choice_4")
        self.next_town = QtWidgets.QPushButton(self.centralwidget)
        self.next_town.setGeometry(QtCore.QRect(10, 450, 771, 23))
        self.next_town.setObjectName("start_game")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guess City"))
        self.next_town.setText(_translate("MainWindow", "Следующий"))
