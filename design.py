import inspect
import os

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon

import mysql.connector
from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem, QHeaderView, QMessageBox, QMainWindow

import addDatabaseDesign
import changeConfDb
import createTable
import changeNameDbTableColumn


def messageInfromationShow(message):
    msg = QMessageBox()
    msg.setStyleSheet("background-color: #1E5162;")
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle('Information')
    msg.setText(message)
    msg.exec_()


def messageWarningShow(message):
    msg = QMessageBox()
    msg.setStyleSheet("background-color: #1E5162;")
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle('Warning')
    msg.setText(message)
    msg.exec_()


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
        self.downloadButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.downloadButton.setObjectName("downloadButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.downloadButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1364, 22))
        self.menubar.setObjectName("menubar")
        self.menuActionsConfiguration = QtWidgets.QMenu(self.menubar)
        self.menuActionsConfiguration.setObjectName('MenuConfiguration')
        self.actionAnnother_Connect = QtWidgets.QAction(MainWindow)
        self.actionAnnother_Connect.setObjectName("actionAnnother_Connect")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.makeChangesInSelectedDatabase = QtWidgets.QAction(MainWindow)
        self.makeChangesInSelectedDatabase.setObjectName("makeChangesInSelectedDatabase")
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
        self.menuActions.addAction(self.makeChangesInSelectedDatabase)
        self.menuActionsConfiguration.addAction(self.actionAnnother_Connect)
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuActionsConfiguration.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.downloadButton.clicked.connect(self.downloadAction)
        self.dbComboBox.activated.connect(self.updateListTables)
        self.listTables.activated.connect(self.fillTable)
        self.actionAdd_database.triggered.connect(self.createDatabase)
        self.password.textChanged.connect(self.passwordChange)
        self.table.itemChanged.connect(self.doChangesInTable)
        self.actionAdd_Row.triggered.connect(self.addRow_To_Table)
        self.actionRemove_Row.triggered.connect(self.remove_Selected_Row)
        self.actionAdd_table.triggered.connect(self.createTableForm)
        self.actionDelete_selected_database.triggered.connect(self.deleteDatabase)
        self.actionDelete_selected_table.triggered.connect(self.deleteTable)
        self.actionAnnother_Connect.triggered.connect(self.openConfWindow)
        self.makeChangesInSelectedDatabase.triggered.connect(self.makeChangesInSelectedDbForm)

        self.menuActions.setDisabled(True)
        self.downloadButton.setEnabled(False)
        self.actionAdd_Row.setEnabled(False)

        self.menuActions.setStyleSheet('background-color: #ADD8E6;')
        self.menuActionsConfiguration.setStyleSheet('background-color: #ADD8E6;')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelForRoot.setText(_translate("MainWindow", "Password for root"))
        self.downloadButton.setText(_translate("MainWindow", "Download mysql or check if download"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionAdd_database.setText(_translate("MainWindow", "CREATE DATABASE"))
        self.actionAdd_table.setText(_translate("MainWindow", "CREATE TABLE"))
        self.actionAdd_Row.setText(_translate("MainWindow", "ADD ROW"))
        self.actionRemove_Row.setText(_translate("MainWindow", "DELETE SELECTED ROW"))
        self.actionDelete_selected_database.setText(_translate("MainWindow", "DELETE SELECTED DATABASE"))
        self.actionDelete_selected_table.setText(_translate("MainWindow", "DELETE SELECTED TABLE"))
        self.actionAnnother_Connect.setText(_translate('MainWindow', 'Change connect configuration or connect without '
                                                                     'check download'))
        self.menuActionsConfiguration.setTitle(_translate('MainWindow', 'Configuration'))
        self.password.setPlaceholderText('Write root password here...')
        self.makeChangesInSelectedDatabase.setText(_translate('MainWindow', 'CHANGE DB NAME, TABLE, COLUMNS'))
        self.setWindowTitle('MySqlManager')

    # Check if download mysql, if not make download

    def downloadAction(self):
        messageInfromationShow('Download started, press \'OK\' and wait while MySQL will downloaded...\n'
                               '( make sure that the password is entered correctly )')

        text = os.popen('echo {0} | sudo -S apt list --installed'.format(self.password.text())).read()

        if text.__contains__('mysql'):
            messageInfromationShow('Mysql is installed')
        else:
            command = './mysql {0}'.format(self.password.text())
            os.system(command)

            text = os.popen('echo {0} | sudo -S apt list --installed'.format(self.password.text())).read()
            if not text.__contains__('mysql'):
                messageWarningShow('Install failed, try again with another password')
                return

            messageInfromationShow('Mysql is installed')

        self.ipDb = 'localhost'
        self.userDb = 'root'
        self.passwordDb = 'mysqlManagerPassword1_'
        self.portDb = 3306

        self.connectAndFillComboBox()

        self.passwordForRoot = self.password.text()
        self.hideRootInput()

    # action on delete row

    def remove_Selected_Row(self):
        if self.table.currentItem() is None:
            messageWarningShow('Row in not selected')
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
                    messageWarningShow(
                        'Unexpected update count received (Actual: {0} Expected: 1). All changes will be rolled back.'
                        .format(str(counter)))
                    return

                cursor.execute('DELETE FROM {0} WHERE {1}'.format(self.listTables.currentItem().text(),
                                                                  namesOfColumns))

                print('DELETE FROM {0} WHERE {1}'.format(self.listTables.currentItem().text(),
                                                         namesOfColumns))
        except Exception as e:
            messageWarningShow(str(e))
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
            messageWarningShow(str(e))
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

    def updateListTables(self):

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

        try:
            db = self.makeConnect()
        except Exception as e:
            messageWarningShow(str(e))
            return

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
                messageWarningShow(
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
                                                                               counter).text() if item[
                                                                                                      0] != column_to_change else
                                                               change_value_All[self.table.currentColumn()])
                    else:
                        change_value += '{0} = \'{1}\' AND '.format(item[0],
                                                                    self.table.item(self.table.currentRow(),
                                                                                    counter).text() if item[
                                                                                                           0] != column_to_change else
                                                                    change_value_All[self.table.currentColumn()])
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
                messageWarningShow(str(e))
                self.reFillTable()

            db.commit()

            self.table.setCurrentItem(None)

    def deleteDatabase(self):
        db = self.makeConnect()

        cursor = db.cursor()

        try:
            cursor.execute('DROP DATABASE {0};'.format(self.dbComboBox.currentText()))
        except Exception as e:
            messageWarningShow(str(e))

        self.connectAndFillComboBox()

    def deleteTable(self):
        if self.listTables.currentItem() is None:
            messageWarningShow('Table is not selected')
            return

        db = self.makeConnectWithDB()

        cursor = db.cursor()

        try:
            cursor.execute('DROP TABLE {0};'.format(self.listTables.currentItem().text()))
        except Exception as e:
            messageWarningShow(str(e))

        self.updateListTables()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)

    def makeConnect(self):
        return mysql.connector.connect(
            host=self.ipDb,
            user=self.userDb,
            password=self.passwordDb,
            port=self.portDb
        )

    def makeConnectWithDB(self):
        return mysql.connector.connect(
            host=self.ipDb,
            user=self.userDb,
            password=self.passwordDb,
            database=self.dbComboBox.currentText(),
            port=self.portDb
        )

    def reFillTable(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.fillTable()

    # back to main window

    def justGoBack(self):
        self.setupUi(self)
        self.connectAndFillComboBox()

        self.hideRootInput()

    def hideRootInput(self):
        self.downloadButton.setParent(None)
        self.labelForRoot.setParent(None)
        self.password.setParent(None)

    def createDatabase(self):
        self.newForm = addDatabaseDesign.Ui_AddDatabase()
        self.newForm.setupUi(self)
        self.setWindowTitle('MySqlManager')
        self.newForm.infoAboutEdit.setText('Enter a name for database')
        self.newForm.saveButton.clicked.connect(self.createDbAndGoBack)
        self.newForm.backButton.clicked.connect(self.justGoBack)

    def createDbAndGoBack(self):
        db = self.makeConnect()
        cursor = db.cursor()
        cursor.execute('CREATE DATABASE {0}'.format(str(self.newForm.inputEdit.text())))
        self.setupUi(self)
        self.connectAndFillComboBox()

        self.hideRootInput()

    def createTableForm(self):
        self.newForm = createTable.Ui_createTable()
        self.newForm.setupUi(self)
        self.newForm.databaseName = self.dbComboBox.currentText()
        self.setWindowTitle('MySqlManager')

        self.newForm.go_Back.clicked.connect(self.justGoBack)
        self.newForm.addColumn.clicked.connect(self.addColumnToNewTable)
        self.newForm.deleteColumn.clicked.connect(self.deleteColumn)
        self.newForm.create_Table.clicked.connect(self.createTable)

    def deleteColumn(self):
        count = len(self.newForm.array)

        if count == 0:
            return

        tempArray = []

        for itemId in range(count - 5, count):
            self.newForm.array.__getitem__(itemId).setParent(None)
            tempArray.append(self.newForm.array.__getitem__(itemId))

        for item in tempArray:
            self.newForm.array.remove(item)

    def createTable(self):
        if len(self.newForm.array) == 0:
            messageWarningShow('Table can not have 0 columns')
            return

        if self.newForm.tableName.text() == '':
            messageWarningShow('Table name can not be empty')
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
                        messageWarningShow('Column name can not be empty')
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
            messageWarningShow(str(e))

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

    def openConfWindow(self):
        self.newForm = changeConfDb.Ui_MainWindow()
        self.newForm.setupUi(self)
        self.setWindowTitle('MySqlManager')

        self.newForm.backButton.clicked.connect(self.justGoBack)
        self.newForm.Apply.clicked.connect(self.checkNewConnection)

    def checkNewConnection(self):
        try:
            db = mysql.connector.connect(
                host=self.newForm.hostDb.text(),
                user=self.newForm.userDb.text(),
                password=self.newForm.password.text(),
                port=self.newForm.portDb.text()
            )

        except Exception as e:
            messageWarningShow(str(e))
            return

        self.ipDb = self.newForm.hostDb.text()
        self.userDb = self.newForm.userDb.text()
        self.passwordDb = self.newForm.password.text()
        self.portDb = int(self.newForm.portDb.text())

        self.justGoBack()

    #  change database name, table name, column name
    def makeChangesInSelectedDbForm(self):
        self.newForm = changeNameDbTableColumn.Ui_MainWindow()
        self.newForm.setupUi(self)
        self.setWindowTitle('MySqlManager')

        try:
            self.newForm.databaseName = self.dbComboBox.currentText()
        except:
            print('it\'s okay')

        self.newForm.back_Button.clicked.connect(self.justGoBack)

        self.newForm.tableWidget.itemChanged.connect(self.makeChangesInSelectedDb)

        self.fillDbChangesTable()

    def fillDbChangesTable(self):
        self.newForm.tableWidget.itemChanged.disconnect()
        self.newForm.tableWidget.setRowCount(0)
        self.newForm.tableWidget.setColumnCount(0)

        db = self.makeConnect()
        db.database = self.newForm.databaseName

        cursor = db.cursor()

        cursor.execute('SHOW TABLES')

        allTables = []

        for table in cursor:
            allTables.append(table[0])

        max_count_columns = 0
        save_result_max = 0

        for table_name in allTables:

            cursor.execute('SHOW COLUMNS FROM {0}'.format(table_name))
            for column in cursor:
                max_count_columns += 1

            if max_count_columns > save_result_max:
                save_result_max = max_count_columns

            max_count_columns = 0

        self.newForm.tableWidget.setRowCount(len(allTables))
        self.newForm.tableWidget.setColumnCount(save_result_max + 2)

        self.newForm.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('DATABASE NAME'))
        self.newForm.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('TABLE NAME'))

        for i in range(2, save_result_max + 2):
            self.newForm.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem('COLUMN NAME'))

        self.newForm.tableWidget.setItem(0, 0, QTableWidgetItem(db.database))

        for i in range(len(allTables)):
            self.newForm.tableWidget.setItem(i, 1, QTableWidgetItem(allTables.__getitem__(i)))
            cursor.execute('SHOW COLUMNS FROM {0}'.format(allTables.__getitem__(i)))

            index_for_column = 2
            for column in cursor:
                self.newForm.tableWidget.setItem(i, index_for_column, QTableWidgetItem(column[0]))
                index_for_column += 1

        self.newForm.tableWidget.itemChanged.connect(self.makeChangesInSelectedDb)

    def makeChangesInSelectedDb(self):
        # self.newForm = changeNameDbTableColumn.Ui_MainWindow()
        # self.newForm.setupUi(self)
        # self.setWindowTitle('MySqlManager')

        if self.newForm.tableWidget.currentColumn() == 0:
            messageWarningShow('You can not change database name')
            self.fillDbChangesTable()
            return

        if self.newForm.tableWidget.currentColumn() == 1:

            db = self.makeConnect()
            db.database = self.newForm.databaseName

            cursor = db.cursor()

            cursor.execute('SHOW TABLES')

            counter = 0
            table_name_to_change = ''
            for table in cursor:
                if counter == self.newForm.tableWidget.currentItem().row():
                    table_name_to_change = table[0]
                counter += 1

            try:
                cursor.execute('RENAME TABLE {0} TO {1};'.format(table_name_to_change,
                                                                 self.newForm.tableWidget.currentItem().text()))
            except Exception as e:
                messageWarningShow(str(e))

            self.fillDbChangesTable()
            return

        db = self.makeConnect()

        db.database = self.newForm.tableWidget.item(0, 0).text()

        cursor = db.cursor(buffered=True)

        cursor.execute('SHOW COLUMNS FROM {0}'.format(
            self.newForm.tableWidget.item(self.newForm.tableWidget.currentItem().row(), 1).text()))

        current_column_name = ''
        column_information = ''
        couter_columns = 0
        for column in cursor:
            if couter_columns + 2 == self.newForm.tableWidget.currentItem().column():
                print(column)
                current_column_name = column[0]

                column_information += str(column[1]).replace('b', '').replace('\'', '')
                if str(column).__contains__('auto_increment'):
                    column_information += ' ' + str(column[len(column) - 1])
                if str(column).__contains__('YES'):
                    column_information += ' null'
                if str(column).__contains__('PRI'):
                    column_information += ' not null'

                print(column_information)
            couter_columns += 1

        if couter_columns + 2 <= self.newForm.tableWidget.currentItem().column():
            messageWarningShow('You can not change this ( not have a sense )')
        else:
            try:
                print()

                print('ALTER TABLE {0} CHANGE COLUMN {1} {2} {3};'.format(self.newForm.tableWidget.item(self.newForm.tableWidget.currentItem().row(), 1).text(),
                      current_column_name, self.newForm.tableWidget.currentItem().text(), column_information))
                cursor.execute('ALTER TABLE {0} CHANGE COLUMN {1} {2} {3};'.format(self.newForm.tableWidget.item(self.newForm.tableWidget.currentItem().row(), 1).text(),
                      current_column_name, self.newForm.tableWidget.currentItem().text(), column_information))
            except Exception as e:
                messageWarningShow(str(e))

        self.fillDbChangesTable()
