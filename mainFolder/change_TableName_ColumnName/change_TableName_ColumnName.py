import mainFolder as func
from PyQt5.QtWidgets import QTableWidgetItem


def makeChangesInSelectedDbForm(self):
    self.newForm = func.change_TableName_ColumnName_design.Ui_MainWindow()
    self.newForm.setupUi(self)
    self.setWindowTitle('MySqlManager')

    try:
        self.newForm.databaseName = self.dbComboBox.currentText()
    except:
        print('it\'s okay')

    self.newForm.back_Button.clicked.connect(lambda: func.help_Methods.justGoBack(self))

    self.newForm.tableWidget.itemChanged.connect(lambda: makeChangesInSelectedDb(self))

    fillDbChangesTable(self)


def fillDbChangesTable(self):
    self.newForm.tableWidget.itemChanged.disconnect()
    self.newForm.tableWidget.setRowCount(0)
    self.newForm.tableWidget.setColumnCount(0)

    db = func.help_Methods.makeConnect(self)
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

    self.newForm.tableWidget.itemChanged.connect(lambda: makeChangesInSelectedDb(self))


def makeChangesInSelectedDb(self):
    if self.newForm.tableWidget.currentColumn() == 0:
        func.warnings.messageWarningShow('You can not change database name')
        fillDbChangesTable(self)
        return

    if self.newForm.tableWidget.currentColumn() == 1:

        db = func.help_Methods.makeConnect(self)
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
            func.warnings.messageWarningShow(str(e))

        fillDbChangesTable(self)
        return

    db = func.help_Methods.makeConnect(self)

    db.database = self.newForm.tableWidget.item(0, 0).text()

    cursor = db.cursor(buffered=True)

    cursor.execute('SHOW COLUMNS FROM {0}'.format(
        self.newForm.tableWidget.item(self.newForm.tableWidget.currentItem().row(), 1).text()))

    current_column_name = ''
    column_information = ''
    counter_columns = 0
    for column in cursor:
        if counter_columns + 2 == self.newForm.tableWidget.currentItem().column():
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
        counter_columns += 1

    if counter_columns + 2 <= self.newForm.tableWidget.currentItem().column():
        func.warnings.messageWarningShow('You can not change this ( not have a sense )')
    else:
        try:
            print('ALTER TABLE {0} CHANGE COLUMN {1} {2} {3};'.format(
                self.newForm.tableWidget.item(self.newForm.tableWidget.currentItem().row(), 1).text(),
                current_column_name, self.newForm.tableWidget.currentItem().text(), column_information))
            cursor.execute('ALTER TABLE {0} CHANGE COLUMN {1} {2} {3};'.format(
                self.newForm.tableWidget.item(self.newForm.tableWidget.currentItem().row(), 1).text(),
                current_column_name, self.newForm.tableWidget.currentItem().text(), column_information))
        except Exception as e:
            func.warnings.messageWarningShow(str(e))

    fillDbChangesTable(self)
