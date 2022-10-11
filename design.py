import os

from PyQt5 import QtCore, QtWidgets

import mysql.connector
from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem, QHeaderView
import addDatabaseDesign


# code need to rewrite, but hi is work

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(870, 520, 191, 31))
        self.password.setObjectName("password")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(480, 500, 201, 51))
        self.downloadButton.setAutoFillBackground(False)
        self.downloadButton.setObjectName("downloadButton")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(260, 500, 221, 51))
        self.connectButton.setObjectName("connectButton")
        self.listTables = QtWidgets.QListWidget(self.centralwidget)
        self.listTables.setGeometry(QtCore.QRect(0, 30, 261, 521))
        self.listTables.setObjectName("listTables")
        self.dbComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.dbComboBox.setGeometry(QtCore.QRect(0, 0, 261, 31))
        self.dbComboBox.setObjectName("DbComboBox")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(260, 0, 801, 501))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.CheckDownload = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckDownload.setGeometry(QtCore.QRect(690, 510, 181, 31))
        self.CheckDownload.setObjectName("CheckDownload")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(870, 500, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 22))
        self.menubar.setObjectName("menubar")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_database = QtWidgets.QAction(MainWindow)
        self.actionAdd_database.setObjectName("actionAdd_database")
        self.actionAdd_table = QtWidgets.QAction(MainWindow)
        self.actionAdd_table.setObjectName("actionAdd_table")
        self.menuActions.addAction(self.actionAdd_database)
        self.menuActions.addAction(self.actionAdd_table)
        self.menubar.addAction(self.menuActions.menuAction())

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.ipDb = 'localhost'
        self.userDb = 'root'
        self.passwordDb = 'mysqlManagerPassword1_'

        self.downloadButton.clicked.connect(self.downloadAction)
        self.connectButton.clicked.connect(self.mysqlConnect)
        self.dbComboBox.activated.connect(self.updateWithComboBox)
        self.listTables.activated.connect(self.getCurrentItemFromWidget)
        self.table.horizontalHeader().sectionClicked.connect(self.Prikol)
        self.actionAdd_database.triggered.connect(self.createDatabase)
        self.password.textChanged.connect(self.passwordChange)
        self.table.itemChanged.connect(self.doChangesInTable)

        self.connectButton.setDisabled(True)
        self.menuActions.setDisabled(True)
        self.CheckDownload.setEnabled(False)
        self.downloadButton.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.downloadButton.setText(_translate("MainWindow", "Download\n"
                                                             "\n"
                                                             "check if downlaod"))
        self.connectButton.setText(_translate("MainWindow", "connect"))
        self.CheckDownload.setText(_translate("MainWindow", "Download"))
        self.lineEdit.setText(_translate("MainWindow", "Password from root :"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionAdd_database.setText(_translate("MainWindow", "Add database"))
        self.actionAdd_table.setText(_translate("MainWindow", "Add table"))

    def downloadAction(self):

        text = os.popen('echo ' + self.password.text() + '| sudo -S apt list --installed').read()

        if text.__contains__('mysql'):
            self.CheckDownload.setChecked(True)
            self.connectButton.setDisabled(False)
        else:
            command = './mysql ' + self.password.text()
            os.system(command)
            self.connectButton.setDisabled(False)

    def createDatabase(self):
        self.newForm = addDatabaseDesign.Ui_AddDatabase()
        self.newForm.setupUi(self)
        self.newForm.infoAboutEdit.setText('Enter a name for database')
        self.newForm.saveButton.clicked.connect(self.goBack)
        self.newForm.backButton.clicked.connect(self.justGoBack)

    def goBack(self):
        db = self.makeConnect()
        cursor = db.cursor()
        cursor.execute('CREATE DATABASE ' + str(self.newForm.inputEdit.text()))
        self.setupUi(self)
        self.mysqlConnect()

    def justGoBack(self):
        self.setupUi(self)
        self.CheckDownload.setChecked(True)
        self.connectButton.setDisabled(False)
        self.mysqlConnect()

    def passwordChange(self):
        self.downloadButton.setEnabled(True)

    def Prikol(self, index):
        print(index)

    def getCurrentItemFromWidget(self):
        db = self.makeConnectWithDB()

        cursor = db.cursor()

        cursor.execute("SHOW COLUMNS FROM " + self.listTables.currentItem().text())

        count_of_columns = 0
        for column in cursor:
            count_of_columns += 1

        self.table.setColumnCount(count_of_columns)

        cursor.execute("SHOW COLUMNS FROM " + self.listTables.currentItem().text())

        column_id = 0
        for column in cursor:
            self.table.setHorizontalHeaderItem(column_id, QTableWidgetItem(column[0]))
            column_id += 1

        cursor.execute("SELECT COUNT(*) FROM " + self.listTables.currentItem().text())

        row_of_count = cursor.fetchall()
        self.table.setRowCount(row_of_count[0][0])

        cursor.execute('SELECT * FROM ' + self.listTables.currentItem().text())

        items_count = 0
        for items in cursor:
            print(items)
            columns_index = 0
            for item in items:
                self.table.setItem(items_count, columns_index, QTableWidgetItem(str(item)))
                columns_index += 1
            items_count += 1

    def updateWithComboBox(self):

        self.listTables.clear()

        db = self.makeConnectWithDB()

        cursor = db.cursor()

        cursor.execute("SHOW TABLES")

        for table_name in cursor:
            print(table_name)
            self.listTables.addItem(QListWidgetItem(table_name[0]))

    def mysqlConnect(self):
        db = self.makeConnect()

        cursor = db.cursor()

        cursor.execute("SHOW DATABASES")

        for database_name in cursor:
            print(database_name)
            self.dbComboBox.addItem(database_name[0])

        mydbWithDb = self.makeConnectWithDB()

        cursor = mydbWithDb.cursor()

        cursor.execute("SHOW TABLES")

        for table_name in cursor:
            print(table_name)
            self.listTables.addItem(QListWidgetItem(table_name[0]))

        self.menuActions.setDisabled(False)

    def doChangesInTable(self):
        if self.table.currentItem() is not None:
            db = self.makeConnectWithDB()

            cursor = db.cursor(buffered=True)

            cursor.execute("SHOW COLUMNS FROM " + self.listTables.currentItem().text())

            column_to_change = ''

            column_id = 0
            for column in cursor:
                if self.table.currentColumn() is column_id:
                    column_to_change = column[0]
                    break

                column_id += 1

            cursor.execute("SELECT * FROM " + self.listTables.currentItem().text())

            change_value = ''

            row_id = 0
            for item in cursor:
                if row_id is self.table.currentRow():
                    change_value = item[self.table.currentColumn()]
                row_id += 1

            print(column_to_change, change_value, self.table.currentItem().text())

            if str(change_value) == str(self.table.currentItem().text()):
                return None

            if str(change_value).isnumeric():
                cursor.execute(
                    'UPDATE ' + self.listTables.currentItem().text() + ' SET ' + str(
                        column_to_change) + "=" + self.table.currentItem().text() + '' +
                    ' WHERE ' + str(column_to_change) + '=' + str(change_value) + ';'
                )
                print(
                    'UPDATE ' + self.listTables.currentItem().text() + ' SET ' + str(
                        column_to_change) + "=" + self.table.currentItem().text() + '' +
                    ' WHERE ' + str(column_to_change) + '=' + str(change_value) + ';'
                )
            else:
                cursor.execute(
                    'UPDATE ' + self.listTables.currentItem().text() + ' SET ' + column_to_change + "=\'" + self.table.currentItem().text() + '\'' +
                    ' WHERE ' + column_to_change + '=\'' + change_value + '\';')

                print(
                    'UPDATE ' + self.listTables.currentItem().text() + ' SET ' + column_to_change + " =\'" + self.table.currentItem().text() + '\'' +
                    ' WHERE ' + column_to_change + ' =\'' + change_value + '\';')

            db.commit()

            self.table.setCurrentItem(None)


    def makeConnect(self):
        return mysql.connector.connect(
            host=self.ipDb,
            user=self.userDb,
            password=self.passwordDb,
        )

    def makeConnectWithDB(self):
        return mysql.connector.connect(
            host=self.ipDb,
            user=self.userDb,
            password=self.passwordDb,
            database=self.dbComboBox.currentText()
        )
