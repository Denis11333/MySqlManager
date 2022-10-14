import os

from PyQt5 import QtCore, QtWidgets

import mysql.connector
from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem, QHeaderView, QMessageBox

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
        self.labelForRoot = QtWidgets.QLabel(self.centralwidget)
        self.labelForRoot.setGeometry(QtCore.QRect(870, 500, 191, 20))
        self.labelForRoot.setObjectName("lineEdit")
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
        self.actionAdd_Row = QtWidgets.QAction(MainWindow)
        self.actionAdd_Row.setObjectName('actionAdd_Row')
        self.actionRemove_Row = QtWidgets.QAction(MainWindow)
        self.actionRemove_Row.setObjectName("actionRemove_Row")
        self.menuActions.addAction(self.actionAdd_database)
        self.menuActions.addAction(self.actionAdd_table)
        self.menuActions.addAction(self.actionAdd_Row)
        self.menuActions.addAction(self.actionRemove_Row)
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
        self.listTables.activated.connect(self.fillTable)
        self.actionAdd_database.triggered.connect(self.createDatabase)
        self.password.textChanged.connect(self.passwordChange)
        self.table.itemChanged.connect(self.doChangesInTable)
        self.actionAdd_Row.triggered.connect(self.addRow_To_Table)
        self.actionRemove_Row.triggered.connect(self.remove_Selected_Row)

        self.connectButton.setDisabled(True)
        self.menuActions.setDisabled(True)
        self.CheckDownload.setEnabled(False)
        self.downloadButton.setEnabled(False)
        self.actionAdd_Row.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MySqlManager"))
        self.downloadButton.setText(_translate("MainWindow", "Download\n"
                                                             "\n"
                                                             "check if download"))
        self.connectButton.setText(_translate("MainWindow", "Connect\n\nreconnect"))
        self.CheckDownload.setText(_translate("MainWindow", "Download"))
        self.labelForRoot.setText(_translate("MainWindow", "Password for root : "))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionAdd_database.setText(_translate("MainWindow", "Add database"))
        self.actionAdd_table.setText(_translate("MainWindow", "Add table"))
        self.actionAdd_Row.setText(_translate('MainWindow', "Add row"))
        self.actionRemove_Row.setText(_translate('MainWindow', 'Delete selected row'))

    # Check if download mysql, if not make download

    def downloadAction(self):
        self.messageInfromationShow('Download started, press \'OK\' and wait while MySQL will downloaded...\n'
                                    '( make sure that the password is entered correctly )')

        text = os.popen('echo {0} | sudo -S apt list --installed'.format(self.password.text())).read()

        if text.__contains__('mysql'):
            self.CheckDownload.setChecked(True)
            self.connectButton.setDisabled(False)
            self.messageInfromationShow('Mysql is installed')
        else:
            command = './mysql {0}'.format(self.password.text())
            os.system(command)

            text = os.popen('echo {0} | sudo -S apt list --installed'.format(self.password.text())).read()
            if text.__contains__('mysql'):
                self.messageWarningShow('Install failed, try again with another password')
                return

            self.connectButton.setDisabled(False)
            self.messageInfromationShow('Mysql is installed')


    # action on delete

    def remove_Selected_Row(self):
        if self.table.currentItem() is None:
            self.messageWarningShow('Row in not selected')
            return

        db = self.makeConnectWithDB()

        cursor = db.cursor()

        cursor.execute(
            'select column_name, case when column_key= \'PRI\' then \'Primary\' else \'Not primary\' end as Output '
            'from information_schema.columns  where table_schema =\'{0}\' and `table_name` = \'{1}\';'
            .format(self.dbComboBox.currentText(), self.listTables.currentItem().text()))

        print(
            'select column_name, case when column_key= \'PRI\' then \'Primary\' else \'Not primary\' end as Output '
            'from information_schema.columns  where table_schema =\'{0}\' and `table_name` = \'{1}\';'
            .format(self.dbComboBox.currentText(), self.listTables.currentItem().text()))

        havePrimaryKey = False
        columnNamePrimary = ''
        for item in cursor:
            print(item)
            if str(item[1]) == 'Primary':
                havePrimaryKey = True
                columnNamePrimary = str(item[0])

        try:
            if havePrimaryKey:
                numberOfPrimaryColumn = 0
                headercount = self.table.columnCount()
                for x in range(headercount):
                    columnName = self.table.horizontalHeaderItem(x).text()
                    if columnNamePrimary == columnName:
                        numberOfPrimaryColumn = x

                if numberOfPrimaryColumn != self.table.currentColumn():
                    change_value = self.table.item(self.table.currentRow(), numberOfPrimaryColumn).text()
                print('{0} {1}'.format(columnNamePrimary,
                                       self.table.item(self.table.currentRow(), numberOfPrimaryColumn).text()))

                cursor.execute('DELETE FROM {0} WHERE {1} = {2};'
                               .format(self.listTables.currentItem().text(),
                                       columnNamePrimary,
                                       self.table.item(self.table.currentRow(), numberOfPrimaryColumn).text()))

                print('DELETE FROM {0} WHERE \'{1}\' = \'{2}\';'
                      .format(self.listTables.currentItem().text(),
                              columnNamePrimary,
                              self.table.item(self.table.currentRow(), numberOfPrimaryColumn).text()))
            else:
                cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

                namesOfColumns = ''
                counter = 0
                for item in cursor:
                    print(item)
                    print(self.table.item(self.table.currentRow(), counter).text())

                    if counter == self.table.columnCount() - 1:
                        namesOfColumns += '{0} = \'{1}\';'.format(item[0],
                                                                  self.table.item(self.table.currentRow(),
                                                                                  counter).text())
                    else:
                        namesOfColumns += '{0} = \'{1}\' AND '.format(item[0],
                                                                      self.table.item(self.table.currentRow(),
                                                                                      counter).text())
                    counter += 1

                cursor.execute('SELECT * FROM {0} WHERE {1}'.format(self.listTables.currentItem().text(),
                                                                    namesOfColumns))
                counter = 0
                for item in cursor:
                    counter += 1

                if counter > 1:
                    self.messageWarningShow(
                        'Unexpected update count received (Actual: {0} Expected: 1). All changes will be rolled back.'
                        .format(str(counter)))
                    return

                cursor.execute('DELETE FROM {0} WHERE {1}'.format(self.listTables.currentItem().text(),
                                                                  namesOfColumns))

                print('DELETE FROM {0} WHERE {1}'.format(self.listTables.currentItem().text(),
                                                         namesOfColumns))
        except Exception as e:
            self.messageWarningShow(str(e))
            self.reFillTable()

        db.commit()
        self.reFillTable()

    def addRow_To_Table(self):
        db = self.makeConnectWithDB()

        cursor = db.cursor()

        cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

        columnValues = []
        insertValues = []

        for item in cursor:
            columnValues.append(item[0])
            if str(item[1]).__contains__('int') or str(item[1]).__contains__('bigint'):
                insertValues.append('0')
            elif str(item[1]).__contains__('varchar'):
                insertValues.append('\'\'')

        columnValuesStr = ''
        insertValuesStr = ''
        for item in range(0, len(columnValues)):
            if item == (len(columnValues) - 1):
                columnValuesStr += columnValues.__getitem__(item)
                insertValuesStr += insertValues.__getitem__(item)
                break

            columnValuesStr += columnValues.__getitem__(item) + ', '
            insertValuesStr += insertValues.__getitem__(item) + ', '

        try:
            cursor.execute('INSERT INTO {0} ({1}) VALUES ({2});'.format(self.listTables.currentItem().text(),
                                                                        columnValuesStr, insertValuesStr))

            print('INSERT INTO {0} ({1}) VALUES ({2})'.format(self.listTables.currentItem().text(),
                                                              columnValuesStr, insertValuesStr))

            db.commit()

            self.reFillTable()
        except Exception as e:
            self.messageWarningShow(str(e))
            self.reFillTable()

    def passwordChange(self):
        self.downloadButton.setEnabled(True)

    # fill table ( get information from selected table )

    def fillTable(self):
        self.actionAdd_Row.setEnabled(True)

        db = self.makeConnectWithDB()

        cursor = db.cursor()

        cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

        count_of_columns = 0
        for column in cursor:
            count_of_columns += 1

        self.table.setColumnCount(count_of_columns)

        cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

        column_id = 0
        for column in cursor:
            self.table.setHorizontalHeaderItem(column_id, QTableWidgetItem(column[0]))
            column_id += 1

        cursor.execute('SELECT COUNT(*) FROM {0}'.format(self.listTables.currentItem().text()))

        row_of_count = cursor.fetchall()
        self.table.setRowCount(row_of_count[0][0])

        cursor.execute('SELECT * FROM {0}'.format(self.listTables.currentItem().text()))

        items_count = 0
        for items in cursor:
            print(items)
            columns_index = 0
            for item in items:
                self.table.setItem(items_count, columns_index, QTableWidgetItem(str(item)))
                columns_index += 1
            items_count += 1

    # Insert all databases in combobox

    def updateWithComboBox(self):

        self.listTables.clear()

        db = self.makeConnectWithDB()

        cursor = db.cursor()

        cursor.execute('SHOW TABLES')

        for table_name in cursor:
            print(table_name)
            self.listTables.addItem(QListWidgetItem(table_name[0]))

    # make first connection and check him

    def mysqlConnect(self):
        self.dbComboBox.clear()
        self.listTables.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)

        db = self.makeConnect()

        cursor = db.cursor()

        cursor.execute('SHOW DATABASES')

        for database_name in cursor:
            print(database_name)
            self.dbComboBox.addItem(database_name[0])

        mydbWithDb = self.makeConnectWithDB()

        cursor = mydbWithDb.cursor()

        cursor.execute('SHOW TABLES')

        for table_name in cursor:
            print(table_name)
            self.listTables.addItem(QListWidgetItem(table_name[0]))

        self.menuActions.setDisabled(False)

    # make changes in database when something will changed

    def doChangesInTable(self):
        if self.table.currentItem() is not None:
            db = self.makeConnectWithDB()

            cursor = db.cursor(buffered=True)

            cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

            column_to_change = ''

            column_id = 0
            for column in cursor:
                if self.table.currentColumn() is column_id:
                    column_to_change = column[0]
                    break

                column_id += 1

            cursor.execute('SELECT * FROM {0}'.format(self.listTables.currentItem().text()))

            change_value = ''

            row_id = 0
            arrayValues = []
            for item in cursor:
                if row_id is self.table.currentRow():
                    change_value = item[self.table.currentColumn()]
                arrayValues.append(item[self.table.currentColumn()])
                row_id += 1

            if str(change_value) == str(self.table.currentItem().text()):
                return None

            cursor.execute(
                'select column_name, case when column_key= \'PRI\' then \'Primary\' else \'Not primary\' end as Output '
                'from information_schema.columns  where table_schema = \'{0}\' and `table_name` = \'{1}\';'
                .format(self.dbComboBox.currentText(), self.listTables.currentItem().text()))

            print(
                'select column_name, case when column_key= \'PRI\' then \'Primary\' else \'Not primary\' end as Output '
                'from information_schema.columns  where table_schema = \'{0}\' and `table_name` = \'{1}\';'
                .format(self.dbComboBox.currentText(), self.listTables.currentItem().text()))

            havePrimaryKey = False
            columnNamePrimary = ''
            for item in cursor:
                print(item)
                if str(item[1]) == 'Primary':
                    havePrimaryKey = True
                    columnNamePrimary = str(item[0])

            if havePrimaryKey:
                numberOfPrimaryColumn = 0
                headercount = self.table.columnCount()
                for x in range(headercount):
                    columnName = self.table.horizontalHeaderItem(x).text()
                    if columnNamePrimary == columnName:
                        numberOfPrimaryColumn = x

                if numberOfPrimaryColumn != self.table.currentColumn():
                    change_value = self.table.item(self.table.currentRow(), numberOfPrimaryColumn).text()

            if arrayValues.count(change_value) > 1 and havePrimaryKey is False:
                self.messageWarningShow(
                    'Unexpected update count received (Actual: {0} Expected: 1). All changes will be rolled back.'
                    .format(str(arrayValues.count(change_value))))

                self.reFillTable()
                return

            try:
                cursor.execute('UPDATE {0} SET {1} = \'{2}\' WHERE {3} = \'{4}\';'.format(
                    self.listTables.currentItem().text(),
                    str(column_to_change),
                    self.table.currentItem().text(),
                    str(columnNamePrimary) if havePrimaryKey else str(column_to_change),
                    str(change_value))
                )

                print('UPDATE {0} SET {1} = \'{2}\' WHERE {3} = \'{4}\';'.format(
                    self.listTables.currentItem().text(),
                    str(column_to_change),
                    self.table.currentItem().text(),
                    str(columnNamePrimary) if havePrimaryKey else str(column_to_change),
                    str(change_value))
                )
            except Exception as e:
                self.messageWarningShow(str(e))
                self.reFillTable()

            db.commit()

            self.table.setCurrentItem(None)

    #
    # need think something better
    #

    def createDatabase(self):
        self.newForm = addDatabaseDesign.Ui_AddDatabase()
        self.newForm.setupUi(self)
        self.newForm.infoAboutEdit.setText('Enter a name for database')
        self.newForm.saveButton.clicked.connect(self.goBack)
        self.newForm.backButton.clicked.connect(self.justGoBack)

    #
    # need think something better
    #

    def goBack(self):
        db = self.makeConnect()
        cursor = db.cursor()
        cursor.execute('CREATE DATABASE {0}'.format(str(self.newForm.inputEdit.text())))
        self.setupUi(self)
        self.mysqlConnect()

        self.unBlock()

    #
    # need think something better
    #

    def justGoBack(self):
        self.setupUi(self)
        self.CheckDownload.setChecked(True)
        self.connectButton.setDisabled(False)
        self.mysqlConnect()

        self.unBlock()

    # create connection to database

    def makeConnect(self):
        return mysql.connector.connect(
            host=self.ipDb,
            user=self.userDb,
            password=self.passwordDb,
        )

    # create connection to database with database

    def makeConnectWithDB(self):
        return mysql.connector.connect(
            host=self.ipDb,
            user=self.userDb,
            password=self.passwordDb,
            database=self.dbComboBox.currentText()
        )

    # show warning about error

    def messageWarningShow(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Warning')
        msg.setText(message)
        msg.exec_()

    def messageInfromationShow(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Information')
        msg.setText(message)
        msg.exec_()

    # right refill table

    def reFillTable(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.fillTable()
    def unBlock(self):
        self.connectButton.setDisabled(False)
        self.downloadButton.setDisabled(False)