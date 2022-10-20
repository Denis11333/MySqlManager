from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddDatabase(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 210)
        MainWindow.setWindowTitle('OK')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoAboutEdit = QtWidgets.QLabel(self.centralwidget)
        self.infoAboutEdit.setObjectName("label")
        self.verticalLayout.addWidget(self.infoAboutEdit)
        self.inputEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.inputEdit)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 22))
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
        self.infoAboutEdit.setText(_translate("MainWindow", "TextLabel"))
        self.saveButton.setText(_translate("MainWindow", "Apply and go back"))
        self.backButton.setText(_translate("MainWindow", "just back"))

