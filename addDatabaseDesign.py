from PyQt5 import QtCore, QtWidgets


class Ui_AddDatabase(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(340, 80, 141, 41))
        self.saveButton.setObjectName("saveButton")
        self.inputEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEdit.setGeometry(QtCore.QRect(30, 130, 301, 71))
        self.inputEdit.setObjectName("infoAboutEdit")
        self.infoAboutEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.infoAboutEdit.setGeometry(QtCore.QRect(30, 80, 301, 31))
        self.infoAboutEdit.setObjectName("lineEdit")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(340, 160, 141, 41))
        self.backButton.setObjectName("backButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveButton.setText(_translate("MainWindow", "Apply and go back"))
        self.backButton.setText(_translate("MainWindow", "just back"))
