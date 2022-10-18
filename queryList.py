from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 217)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.All_query = QtWidgets.QLabel(self.centralwidget)
        self.All_query.setObjectName("All_query")
        self.gridLayout.addWidget(self.All_query, 0, 0, 1, 1)
        self.queryShowLine = QtWidgets.QTextEdit(self.centralwidget)
        self.queryShowLine.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.queryShowLine, 1, 0, 1, 1)
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setObjectName("Back")
        self.gridLayout.addWidget(self.Back, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.queryShowLine.setReadOnly(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.All_query.setText(_translate("MainWindow", "Query list"))
        self.Back.setText(_translate("MainWindow", "Back"))
