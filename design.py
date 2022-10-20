import inspect
import os

from PyQt5 import QtCore, QtWidgets, QtGui

import mysql.connector
from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem, QHeaderView, QMessageBox, QMainWindow

import addDatabaseDesign
import createTable


# code need to rewrite, but hi is work

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1364, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.firstLayout = QtWidgets.QVBoxLayout()
        self.firstLayout.setObjectName("firstLayout")
        self.dbComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.dbComboBox.setObjectName("dbComboBox")
        self.firstLayout.addWidget(self.dbComboBox)
        self.listTables = QtWidgets.QListWidget(self.centralwidget)
        self.listTables.setObjectName("listTables")
        self.firstLayout.addWidget(self.listTables)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.firstLayout)
        self.secondLoyout = QtWidgets.QHBoxLayout()
        self.secondLoyout.setObjectName("secondLoyout")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.secondLoyout.addWidget(self.table)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.secondLoyout)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.labelForRoot = QtWidgets.QLabel(self.centralwidget)
        self.labelForRoot.setObjectName("labelForRoot")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelForRoot)
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setObjectName("downloadButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.downloadButton)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setObjectName("connectButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.connectButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1364, 22))
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
        self.actionAdd_Row.setObjectName("actionAdd_Row")
        self.actionRemove_Row = QtWidgets.QAction(MainWindow)
        self.actionRemove_Row.setObjectName("actionRemove_Row")
        self.actionDatabase_info_change = QtWidgets.QAction(MainWindow)
        self.actionDatabase_info_change.setObjectName("actionDatabase_info_change")
        self.actionchange_configuration = QtWidgets.QAction(MainWindow)
        self.actionchange_configuration.setObjectName("actionchange_configuration")
        self.actionDelete_selected_database = QtWidgets.QAction(MainWindow)
        self.actionDelete_selected_database.setObjectName("actionDelete_selected_database")
        self.actionDelete_selected_table = QtWidgets.QAction(MainWindow)
        self.actionDelete_selected_table.setObjectName("actionDelete_selected_table")
        self.menuActions.addAction(self.actionAdd_Row)
        self.menuActions.addAction(self.actionAdd_table)
        self.menuActions.addAction(self.actionAdd_database)
        self.menuActions.addAction(self.actionRemove_Row)
        self.menuActions.addAction(self.actionDelete_selected_table)
        self.menuActions.addAction(self.actionDelete_selected_database)
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.ipDb = 'localhost'
        self.userDb = 'root'
        self.passwordDb = 'mysqlManagerPassword1_'

        self.downloadButton.clicked.connect(self.downloadAction)
        self.connectButton.clicked.connect(self.connectAndFillComboBox)
        self.dbComboBox.activated.connect(self.updateWithComboBox)
        self.listTables.activated.connect(self.fillTable)
        self.actionAdd_database.triggered.connect(self.createDatabase)
        self.password.textChanged.connect(self.passwordChange)
        self.table.itemChanged.connect(self.doChangesInTable)
        self.actionAdd_Row.triggered.connect(self.addRow_To_Table)
        self.actionRemove_Row.triggered.connect(self.remove_Selected_Row)
        self.actionAdd_table.triggered.connect(self.createTableForm)
        self.actionDelete_selected_database.triggered.connect(self.deleteDatabase)
        self.actionDelete_selected_table.triggered.connect(self.deleteTable)

        self.connectButton.setDisabled(True)
        self.menuActions.setDisabled(True)
        self.downloadButton.setEnabled(False)
        self.actionAdd_Row.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelForRoot.setText(_translate("MainWindow", "Password for root"))
        self.downloadButton.setText(_translate("MainWindow", "Download mysql or check if download"))
        self.connectButton.setText(_translate("MainWindow", "connect or reconnect to database"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionAdd_database.setText(_translate("MainWindow", "Add DATABASE"))
        self.actionAdd_table.setText(_translate("MainWindow", "Add TABLE"))
        self.actionAdd_Row.setText(_translate("MainWindow", "Add ROW"))
        self.actionRemove_Row.setText(_translate("MainWindow", "Delete selected ROW"))
        self.actionDelete_selected_database.setText(_translate("MainWindow", "Delete selected DATABASE"))
        self.actionDelete_selected_table.setText(_translate("MainWindow", "Delete selected TABLE"))
        self.password.setPlaceholderText('Write root password here...')
        self.setWindowTitle('MySqlManager')


    # Check if download mysql, if not make download

    def downloadAction(self):
        self.messageInfromationShow('Download started, press \'OK\' and wait while MySQL will downloaded...\n'
                                    '( make sure that the password is entered correctly )')

        text = os.popen('echo {0} | sudo -S apt list --installed'.format(self.password.text())).read()

        if text.__contains__('mysql'):
            self.messageInfromationShow('Mysql is installed')
        else:
            command = './mysql {0}'.format(self.password.text())
            os.system(command)

            text = os.popen('echo {0} | sudo -S apt list --installed'.format(self.password.text())).read()
            if not text.__contains__('mysql'):
                self.messageWarningShow('Install failed, try again with another password')
                return

            self.messageInfromationShow('Mysql is installed')

        self.connectButton.setDisabled(False)
        self.password.setDisabled(True)

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

    # action on Add row

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

    def connectAndFillComboBox(self):
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
            change_value_All = []

            row_id = 0
            arrayValues = []
            for item in cursor:
                if row_id is self.table.currentRow():
                    change_value = item[self.table.currentColumn()]
                    change_value_All = item
                arrayValues.append(item)
                row_id += 1

            if str(change_value) == str(self.table.currentItem().text()):
                return None

            if arrayValues.count(change_value_All) > 1:
                self.messageWarningShow(
                    'Unexpected update count received (Actual: {0} Expected: 1). All changes will be rolled back.'
                    .format(arrayValues.count(change_value_All)))

                self.reFillTable()
                return

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
            else:
                cursor.execute('SHOW COLUMNS FROM {0}'.format(self.listTables.currentItem().text()))

                change_value = ''
                counter = 0
                for item in cursor:

                    if counter == self.table.columnCount() - 1:
                        change_value += '{0} = \'{1}\''.format(item[0],
                                                                    self.table.item(self.table.currentRow(),
                                                                    counter).text() if item[0] != column_to_change else change_value_All[self.table.currentColumn()])
                    else:
                        change_value += '{0} = \'{1}\' AND '.format(item[0],
                                                                    self.table.item(self.table.currentRow(),
                                                                    counter).text() if item[0] != column_to_change else change_value_All[self.table.currentColumn()])
                    counter += 1

            try:
                if not havePrimaryKey:
                    query = 'UPDATE {0} SET {1} = \'{2}\' WHERE {3};'.format(
                            self.listTables.currentItem().text(),
                            str(column_to_change),
                            self.table.currentItem().text(),
                            str(change_value))
                    print(query)
                    cursor.execute(query)
                else:
                    query = 'UPDATE {0} SET {1} = \'{2}\' WHERE {3} = \'{4}\';'.format(
                        self.listTables.currentItem().text(),
                        str(column_to_change),
                        self.table.currentItem().text(),
                        str(columnNamePrimary),
                        str(change_value))
                    print(query)
                    cursor.execute(query)
            except Exception as e:
                self.messageWarningShow(str(e))
                self.reFillTable()

            db.commit()

            self.table.setCurrentItem(None)

    # open form with create table

    def createTableForm(self):
        self.newForm = createTable.Ui_createTable()
        self.newForm.setupUi(self)
        self.newForm.databaseName = self.dbComboBox.currentText()
        self.setWindowTitle('MySqlManager')

        self.newForm.go_Back.clicked.connect(self.justGoBack)
        self.newForm.addColumn.clicked.connect(self.addColumnToNewTable)
        self.newForm.deleteColumn.clicked.connect(self.deleteColumn)
        self.newForm.create_Table.clicked.connect(self.createTable)

    # add new column action
    def addColumnToNewTable(self):
        columnName = QtWidgets.QLineEdit(self.newForm.scrollAreaWidgetContents)
        columnName.setPlaceholderText('Column name')

        type_of_column = QtWidgets.QComboBox(self.newForm.scrollAreaWidgetContents)
        type_of_column.setEditable(True)
        type_of_column.addItem('varchar(30)')
        type_of_column.addItem('int')

        primary_key = QtWidgets.QComboBox(self.newForm.scrollAreaWidgetContents)
        primary_key.setEditable(True)
        primary_key.addItem('Not a primary key')
        primary_key.addItem('Primary key')
        primary_key.addItem('Primary key auto_increment')

        additionalText = QtWidgets.QLineEdit(self.newForm.scrollAreaWidgetContents)
        additionalText.setPlaceholderText('Parameters for example varchar( your param )')

        line = QtWidgets.QFrame(self.newForm.scrollAreaWidgetContents)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.newForm.tableLayout.addWidget(columnName)
        self.newForm.tableLayout.addWidget(type_of_column)
        self.newForm.tableLayout.addWidget(primary_key)
        self.newForm.tableLayout.addWidget(additionalText)
        self.newForm.tableLayout.addWidget(line)

        self.newForm.array.append(columnName)
        self.newForm.array.append(type_of_column)
        self.newForm.array.append(primary_key)
        self.newForm.array.append(additionalText)
        self.newForm.array.append(line)

    # delete column action
    def deleteColumn(self):
        count = len(self.newForm.array)
        tempArray = []

        for itemId in range(count - 5, count):
            self.newForm.array.__getitem__(itemId).setParent(None)
            tempArray.append(self.newForm.array.__getitem__(itemId))

        for item in tempArray:
            self.newForm.array.remove(item)

    # create table action

    def createTable(self):
        if len(self.newForm.array) == 0:
            self.messageWarningShow('Table can not have 0 columns')
            return

        if self.newForm.tableName.text() == '':
            self.messageWarningShow('Table name can not be empty')
            return

        AllColumnsArray = []
        columnArray = []
        counterForArraysColumns = 0

        for item in self.newForm.array:
            if isinstance(item, QtWidgets.QLineEdit):
                columnArray.append('param' if item.text() == '' else item.text())
                print('param' if item.text() == '' else item.text())
                if item.placeholderText() == 'Column name':
                    if item.text() == '':
                        self.messageWarningShow('Column name can not be empty')
                        return

            if isinstance(item, QtWidgets.QComboBox):
                columnArray.append(item.currentText())
                print(item.currentText())

            counterForArraysColumns += 1
            print(counterForArraysColumns)
            if counterForArraysColumns % 5 == 0 and counterForArraysColumns > 4:
                print(columnArray)
                AllColumnsArray.append(columnArray.copy())
                columnArray.clear()

        print(AllColumnsArray)

        print(self.newForm.databaseName)

        db = mysql.connector.connect(
            host=self.ipDb,
            user=self.userDb,
            password=self.passwordDb,
            database=self.newForm.databaseName
        )

        cursor = db.cursor()

        createString = ''

        try:
            for array in AllColumnsArray:
                if array[1].__contains__('varchar'):
                    if array[3] != 'param' and array[3].isnumeric():
                        array[1] = array[1].replace('30', array[3])

                if array[1].__contains__('int'):
                    array[3] = ''

                createString += '{0} {1}'.format(array[0], array[1])

                if array[2] == 'Primary key auto_increment':
                    createString += ' primary key auto_increment'

                if array[2] == 'Primary key':
                    createString += ' primary key'

                createString += ', '

            print('CREATE TABLE {0} ({1});'.format(self.newForm.tableName.text(), createString[:-2]))
            cursor.execute('CREATE TABLE {0} ({1});'.format(self.newForm.tableName.text(), createString[:-2]))

            self.justGoBack()
        except Exception as e:
            self.messageWarningShow(str(e))

    # delete database action

    def deleteDatabase(self):
        db = self.makeConnect()

        cursor = db.cursor()

        try:
            cursor.execute('DROP DATABASE {0};'.format(self.dbComboBox.currentText()))
        except Exception as e:
            self.messageWarningShow(str(e))

        self.connectAndFillComboBox()

    def deleteTable(self):
        if self.listTables.currentItem() is None:
            self.messageWarningShow('Table is not selected')
            return

        db = self.makeConnectWithDB()

        cursor = db.cursor()

        try:
            cursor.execute('DROP TABLE {0};'.format(self.listTables.currentItem().text()))
        except Exception as e:
            self.messageWarningShow(str(e))

        self.updateWithComboBox()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)

    # create database action

    def createDatabase(self):
        self.newForm = addDatabaseDesign.Ui_AddDatabase()
        self.newForm.setupUi(self)
        self.setWindowTitle('MySqlManager')
        self.newForm.infoAboutEdit.setText('Enter a name for database')
        self.newForm.saveButton.clicked.connect(self.createDbAndGoBack)
        self.newForm.backButton.clicked.connect(self.justGoBack)

    # create and back to main window

    def createDbAndGoBack(self):
        db = self.makeConnect()
        cursor = db.cursor()
        cursor.execute('CREATE DATABASE {0}'.format(str(self.newForm.inputEdit.text())))
        self.setupUi(self)
        self.connectAndFillComboBox()

        self.unBlock()

    # back to main window
    def justGoBack(self):
        self.setupUi(self)
        self.connectButton.setDisabled(False)
        self.connectAndFillComboBox()

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
        msg.setStyleSheet("background-color: #1E5162;")
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Warning')
        msg.setText(message)
        msg.exec_()

    def messageInfromationShow(self, message):
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #1E5162;")
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
