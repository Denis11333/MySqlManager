from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createTable(object):

    def setupUi(self, MainWindow):
        self.array = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 556)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 822, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.tableLayout.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.addColumn = QtWidgets.QPushButton(self.centralwidget)
        self.addColumn.setObjectName("addColumn")
        self.verticalLayout.addWidget(self.addColumn)
        self.deleteColumn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteColumn.setObjectName("deleteColumn")
        self.verticalLayout.addWidget(self.deleteColumn)
        self.create_Table = QtWidgets.QPushButton(self.centralwidget)
        self.create_Table.setObjectName("create_Table")
        self.verticalLayout.addWidget(self.create_Table)
        self.go_Back = QtWidgets.QPushButton(self.centralwidget)
        self.go_Back.setObjectName("go_Back")
        self.verticalLayout.addWidget(self.go_Back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tableName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.tableName.setPlaceholderText('Table name')

        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.tableLayout.addWidget(self.tableName)
        self.tableLayout.addWidget(self.line)

        self.databaseName = ''

        for item in self.array:
            self.tableLayout.addWidget(item)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addColumn.setText(_translate("MainWindow", "Add column"))
        self.create_Table.setText(_translate("MainWindow", "Create table"))
        self.go_Back.setText(_translate("MainWindow", "Go back"))
        self.deleteColumn.setText(_translate('MainWindow', 'Delete column'))


