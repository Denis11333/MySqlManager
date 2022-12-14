from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 385)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.hostLable = QtWidgets.QLabel(self.centralwidget)
        self.hostLable.setObjectName("hostLable")
        self.verticalLayout.addWidget(self.hostLable)
        self.hostDb = QtWidgets.QLineEdit(self.centralwidget)
        self.hostDb.setObjectName("hostDb")
        self.verticalLayout.addWidget(self.hostDb)
        self.portDbLabel = QtWidgets.QLabel(self.centralwidget)
        self.portDbLabel.setObjectName("portDbLabel")
        self.verticalLayout.addWidget(self.portDbLabel)
        self.portDb = QtWidgets.QLineEdit(self.centralwidget)
        self.portDb.setObjectName("portDb")
        self.verticalLayout.addWidget(self.portDb)
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setObjectName("userLabel")
        self.verticalLayout.addWidget(self.userLabel)
        self.userDb = QtWidgets.QLineEdit(self.centralwidget)
        self.userDb.setObjectName("userDb")
        self.verticalLayout.addWidget(self.userDb)
        self.passwordLable = QtWidgets.QLabel(self.centralwidget)
        self.passwordLable.setObjectName("passwordLable")
        self.verticalLayout.addWidget(self.passwordLable)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.Apply = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Apply.setObjectName("Apply")
        self.verticalLayout.addWidget(self.Apply)
        self.backButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 22))
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
        self.hostLable.setText(_translate("MainWindow", "Host"))
        self.hostDb.setPlaceholderText(_translate("MainWindow", "Here your host"))
        self.portDbLabel.setText(_translate("MainWindow", "Port"))
        self.portDb.setPlaceholderText(_translate("MainWindow", "Here your port"))
        self.userLabel.setText(_translate("MainWindow", "User"))
        self.userDb.setPlaceholderText(_translate("MainWindow", "Here your user"))
        self.passwordLable.setText(_translate("MainWindow", "Password"))
        self.password.setPlaceholderText(_translate("MainWindow", "Here your password"))
        self.Apply.setText(_translate("MainWindow", "Apply configuration and connect"))
        self.backButton.setText(_translate("MainWindow", "Back"))
